import csv
import requests
import re
import os

url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
response = requests.get(url).json()
posts = response["result"]["results"]

valid_posts = []


for post in posts:
    if int(post["xpostDate"][:4]) >= 2015:
        urls = re.findall('https?://[\w/.-]+\.jpg', post["file"], re.IGNORECASE)
        valid_posts.append([post["stitle"], post["address"][5:8], post["longitude"], post["latitude"], urls[0]])


with open("data.csv", 'w') as file:
    writer = csv.writer(file)

    for post in valid_posts:
        writer.writerow(post)