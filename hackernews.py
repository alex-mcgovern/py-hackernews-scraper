import argparse
import requests
import json
import validators

parser = argparse.ArgumentParser()
parser.add_argument("--posts")
arg = parser.parse_args()

# logic to handle integers outside desired range
try:
    i = int(arg.posts)
    if (i > 100):
        i = 100
        print("invalid entry for --posts: " + arg.posts + " changed to 100")
    if (i < 1):
        i = 1
        print("invalid entry for --posts: " + arg.posts + " changed to 1")

# handle any non-integers and provide feedback to user
except:
    print("invalid entry for --posts: " + arg.posts + " terminating program")
    print("HINT: you need to enter a positive integer <=100")
    exit()

# GET & decode from endpoint
pullTopStories = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?')
topStories = pullTopStories.json()

# array to store fetched data
results = []

for itemNo in range(0, i):
    pullStoryInfo = requests.get('https://hacker-news.firebaseio.com/v0/item/' + f"{topStories[itemNo]}" + '.json?')
    storyInfo = json.loads(pullStoryInfo.text)
    for item in storyInfo:
        itemInfo = {}

        #ensures title is not an empty string & limits title to 256 characters
        if storyInfo["title"]:
            itemInfo["title"] = storyInfo["title"][:256]
        else:
            itemInfo["title"] = "Couldn't load a title"

        #validate uri using validators package, simple and easy to implement
        #validates uri, still passes invalid uri's with feedback to user if invalid
        try:
            if validators.url(storyInfo["url"]):
                itemInfo["uri"] = storyInfo["url"]
            else:
                itemInfo["uri"] = "(failed validation) " + storyInfo["url"]

        #handle HN self-posts without external uri
        except:
            itemInfo["uri"] = "self-post from HN"

        #ensures author is not an empty string & limits title to 256 characters
        if storyInfo["by"]:
            itemInfo["author"] = storyInfo["by"][:256]
        else:
            itemInfo["author"] = "Couldn't load an author"

        #testing confirms returned value is an integer >=0
        itemInfo["points"] = storyInfo["score"]

        #logic to handle posts without comments
        try:
            itemInfo["comments"] = len(storyInfo["kids"])
        except:
            itemInfo["comments"] = 0

        #logic ensures rank is >= 1 based on sorting presented by HN API
        itemInfo["rank"] = itemNo + 1

    results.append(itemInfo)

#output JSON file with basic formatting
with open("/src/hackerNewsTopPosts.json", "w") as json_file:
    json.dump(results, json_file, indent=4, sort_keys=True)
print("Operation successful, pulled " + f"{i}" + " post(s) and wrote hackerNewsTopPosts.json to specified directory")
