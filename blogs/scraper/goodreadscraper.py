from bs4 import BeautifulSoup
import datetime
import requests
import sys
from datetime import datetime


sys.path.append('/app')
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blogs.models import Integration, Books 



# Since we were getting 403 errors from the website then we had to give it a User agent header 
# otherwise we didn't have to write this code
def scrape_goodreads(url, user):
    headers = { 
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        )
    }
    # we send a requests.get to the website that we want to scrap
    #if we get 200 respons that mean we got the information / if its 403 it means accese denied 

   

    response = requests.get( url, headers=headers ).text

    soup = BeautifulSoup(response , "lxml")
    books = soup.find_all("tr", class_="bookalike review")  # go in tr tag that are boxes with that class

    for book in books : # Iterate on all of those boks
        title = book.find('a', title=True)['title']  #find their name that are in a tags
        author = book.find("td", class_='field author').find('a').text
        date_tag = book.find('span', class_='date_read_value') # Since there is none datetime in the web we have to give it a rule so if there was none just bring back none 
        read_date = date_tag.get_text(strip=True) if date_tag else None
        if not read_date:
            continue
        try:
            read_data = datetime.strptime(read_date, "%b %d, %Y").date()
        except ValueError:
    # skip if format doesn't match
            continue

   
        if not Books.objects.filter(read_data=read_data,user=user,author=author,title=title).exists():
            Books.objects.create(
                title=title,
                author=author,
                read_data=read_data,    
                url=url,
                user=user
            )

def run():
    # get all integrations where type_choice == 'goodreads'
    integrations = Integration.objects.filter(integration_type='goodreads')

    for integration in integrations:
        user = integration.user
        url = integration.integration_url
        print(f"🔍 Scraping Goodreads for {user.username} ({url})")
        scrape_goodreads(url, user)

    print("🎉 All Goodreads data saved successfully!")

if __name__ == "__main__":
    run()
