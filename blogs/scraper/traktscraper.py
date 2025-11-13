
from datetime import datetime
import requests
import json
import sys

sys.path.append('/app')
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from blogs.models import Activity,Integration


def traktscraper(url,user):

    headers = {
    "Content-Type": "application/json",
    "trakt-api-version": "2",
    "trakt-api-key": "910ed21e23b3f0f2db1a0c44708db843d951cef85121085c5366a33a62fceb0a"
}

    response = requests.get( url, headers=headers )
    data = response.json()


    results = []

    for item in data[:10]:
        type_ = item.get("type")
        watched_at = datetime.fromisoformat(item.get("watched_at").replace("Z", "+00:00")).date()

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

        })


        Activity.objects.update_or_create(
            user=user,
            activity_type='watching',
            backend='trakts',
            url=url,
            title=title,                             
            defaults={
                'created_at': watched_at,             
                'activity_detail': {                 
                    "type": type_,
                    "season": season,
                    "number": number,
                    "source": "trakts"
                },
            }
        )


def run():
    # get all integrations where type_choice == 'goodreads'
    integrations = Integration.objects.filter(integration_type='trakt')
    for integration in integrations:
        user = integration.user
        url = integration.integration_url
        print(f"🔍 Scraping trakt for {user.username} ({url})")
        traktscraper(url, user)

    print("🎉 All Goodreads data saved successfully!")

if __name__ == "__main__":
    run()



