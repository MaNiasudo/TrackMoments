
import datetime
import requests
import json
import sys

sys.path.append('/app')
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blogs.models import Activity,Integration


 # نام کاربری Trakt.tv
def traktscraper(url_c,user):

    headers = {
    "Content-Type": "application/json",
    "trakt-api-version": "2",
    "trakt-api-key": "910ed21e23b3f0f2db1a0c44708db843d951cef85121085c5366a33a62fceb0a"
}

    url = f"https://api.trakt.tv/users/{url_c}/history"
    response = requests.get( url, headers=headers )
    data = response.json()


    results = []

    for item in data[:10]:
        type_ = item.get("type")
        watched_at = item.get("watched_at")

        if type_ == "movie": 
            movie = item.get("movie", {})
            title = movie.get("title")
            season = None
            number = None
        elif type_ == "episode":
            show = item.get("show", {})
            episode = item.get("episode", {})
            title = show.get("title")
            season = episode.get("season")
            number = episode.get("number")
        else:
            continue

        results.append({
            "type": type_,
            "title": title,
            "season": season,
            "number": number,
            "watched_at": watched_at
        })


    Activity.objects.create(
            user=user,
            activity_type='trakt',
            activity_details= results ,
            url=url

        )




def run():
    # get all integrations where type_choice == 'goodreads'
    integrations = Integration.objects.filter(integration_type='trakt')
    for integration in integrations:
        user = integration.user
        url_c = integration.integration_url
        print(f"🔍 Scraping trakt for {user.username} ({url_c})")
        traktscraper(url_c, user)

    print("🎉 All Goodreads data saved successfully!")

if __name__ == "__main__":
    run()





# for item in data[:10]:  # آخرین 10 مورد
#     type_ = item["type"]
#     watched_at = item["watched_at"]

#     if type_ == "movie":
#         title = item["movie"]["title"]  
#         season = item["movie"]["season"]
#         print(f"🎬 Movie: {title} ({season}) watched at {watched_at}")
#     elif type_ == "episode":
#         show = item["show"]["title"]
#         season = item["episode"]["season"]
#         number = item["episode"]["number"]
#         print(f"📺 {show} S{season:02}E{number:02} watched at {watched_at}")