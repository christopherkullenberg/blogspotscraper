"""
This script scrapes a Blogspot blog by iterating back in its history.

Usage:
    1. Set url variable to the Blogspot URL you want as point of departure.
    2. Press CTRL-C when you want to stop it.

Note: Your IP-number may be temporarily banned from the Blogger service if over-used.
Use on your own risk.
"""

import requests
import io
import re
from bs4 import BeautifulSoup

#Set url to Blogger blog between the single quotation marks
#For examle url = 'http://german-podcast.blogspot.se/2013/01/new-vocitach-android-app-with-more-than.html'
url = ''

counter = 0

while True:
    r = requests.get(url)
    file_like_obj = io.StringIO(r.text) #Turns the requested output into a file like objet
    lines = file_like_obj.read()
    for l in lines:
        counter += 1 #Update the counter from proper filenames
        soup = BeautifulSoup(lines)
        findID = re.findall(r'post-body-(.*)\' itemprop', lines) #This retrieves each post's unique ID-number for the text.
        print(findID[0]) #for debugging
        div = soup.find(id="post-body-" + findID[0]) #This retrieves each post content
        print(div)
        with open(str(counter) + ".html", "w") as outputfile: #open file
            outputfile.write(str(div)) #write to file
            matchObj = re.findall(r'blog-pager-older-link\' href=\'(.*)\' id', lines) # This extract the "Older" post
            next_url = matchObj[0]
            print("Next URL for scraping: " + next_url)
            print("Press CTRL-C to exit the program.")
            url = next_url # This changes the variable in the beginning of the script
            break
