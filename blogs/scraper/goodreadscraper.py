from bs4 import BeautifulSoup
import datetime
import requests
import json
import psycopg2
from db import cursor,conn

today_date = datetime.datetime.now()
today_month = today_date.strftime("%b")


# Since we were getting 403 errors from the website then we had to give it a User agent header 
# otherwise we didn't have to write this code

headers = { 
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}
# we send a requests.get to the website that we want to scrap
#if we get 200 respons that mean we got the information / if its 403 it means accese denied 


url = 'https://www.goodreads.com/review/list/5387467-mohammad-efazati'
response = requests.get( url, headers=headers ).text
soup = BeautifulSoup(response , "lxml")

scraped_data=[]

books = soup.find_all("tr", class_="bookalike review")  # go in tr tag that are boxes with that class

for book in books : # Iterate on all of those boks
    book_name = book.find('a', title=True)['title']  #find their name that are in a tags
    authorname = book.find("td", class_='field author').find('a').text
    # author_tag = book.find("td", class_='field author') #find td tags and then find a tags inside those td tags
    # authorname  = author_tag.find('a').text
    date_tag = book.find('span', class_='date_read_value') # Since there is none datetime in the web we have to give it a rule so if there was none just bring back none 
    read_date = date_tag.get_text(strip=True) if date_tag else None
    
    if read_date is not None:
      book_data = {
         'Title':book_name,
         'Author':authorname,
         'read_data':read_date,
            'metadata':{
               'url':url,
            }
      }
      scraped_data.append(book_data)

insert_query = """
    INSERT INTO blogs_books (title, author, read_data, url)
    VALUES (%s, %s, %s, %s);
"""

for book in scraped_data:
    cursor.execute(
        insert_query,
        (
            book["Title"],
            book["Author"],
            book["read_data"],  # or None
            book["metadata"]["url"],
        )
    )

conn.commit()
cursor.close()
conn.close()

print("✅ Data successfully inserted into PostgreSQL")