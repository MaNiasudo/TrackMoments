
import datetime
import requests
import json

headers = {
    "Content-Type": "application/json",
    "trakt-api-version": "2",
    "trakt-api-key": "910ed21e23b3f0f2db1a0c44708db843d951cef85121085c5366a33a62fceb0a"
}

username = "efazati"  # نام کاربری Trakt.tv
def url(get_url):
    get_url = input("Enter a url")
    return get_url

url = f"https://api.trakt.tv/users/{username}/history"


response = requests.get( url, headers=headers )

data = response.json()


for item in data[:10]:  # آخرین 10 مورد
    type_ = item["type"]
    watched_at = item["watched_at"]

    if type_ == "movie":
        title = item["movie"]["title"]
        year = item["movie"]["year"]
        print(f"🎬 Movie: {title} ({year}) watched at {watched_at}")
    elif type_ == "episode":
        show = item["show"]["title"]
        season = item["episode"]["season"]
        number = item["episode"]["number"]
        print(f"📺 {show} S{season:02}E{number:02} watched at {watched_at}")