# from bs4 import BeautifulSoup
# import requests
# from urllib.parse import urljoin
# import tweepy
# import time
# from django.shortcuts import render
# from django.http import HttpResponse 

# def sportslab():
#     url = "https://www.sportskeeda.com/nfl/news"
#     base = "https://www.sportskeeda.com" 

#     result = requests.get(url)

#     doc = BeautifulSoup(result.text,"html.parser")
#     feed = doc.find_all("div", class_="feed-item-secondary")[:5]

#     tweet_texts = []

#     for f in feed:
#         a_tag = f.find("a", href = True)
#         link = urljoin(base, a_tag["href"]) + "#key2=905920"
#         title = a_tag.text
#         tweet_text = f"{title}\n{link}"
#         tweet_texts.append(tweet_text)
#     return tweet_texts
    
# def tennis():
#     url = "https://www.sportskeeda.com/tennis/news"
#     base = "https://www.sportskeeda.com" 

#     result = requests.get(url)

#     doc = BeautifulSoup(result.text,"html.parser")
#     feed = doc.find_all("div", class_="feed-item-secondary")[:5]

#     tweet_texts = []

#     for f in feed:
#         a_tag = f.find("a", href = True)
#         link = urljoin(base, a_tag["href"]) + "#key2=905920"
#         title = a_tag.text
#         tweet_text = f"{title}\n{link}"
#         tweet_texts.append(tweet_text)
#     return tweet_texts
      
# def wwe():
#     url = "https://www.sportskeeda.com/wwe/news"
#     base = "https://www.sportskeeda.com" 

#     result = requests.get(url)

#     doc = BeautifulSoup(result.text,"html.parser")
#     feed = doc.find_all("div", class_="feed-item-secondary")[:5]

#     tweet_texts = []

#     for f in feed:
#         a_tag = f.find("a", href = True)
#         link = urljoin(base, a_tag["href"]) + "#key2=905920"
#         title = a_tag.text
#         tweet_text = f"{title}\n{link}"
#         tweet_texts.append(tweet_text)
#     return tweet_texts
    
# def football():
#     url = "https://www.sportskeeda.com/football/news"
#     base = "https://www.sportskeeda.com" 

#     result = requests.get(url)

#     doc = BeautifulSoup(result.text,"html.parser")
#     feed = doc.find_all("div", class_="feed-item-secondary")[:5]

#     tweet_texts = []

#     for f in feed:
#         a_tag = f.find("a", href = True)
#         link = urljoin(base, a_tag["href"]) + "#key2=905920"
#         title = a_tag.text
#         tweet_text = f"{title}\n{link}"
#         tweet_texts.append(tweet_text)
#     return tweet_texts     
# # -----------------------------
# # 3. Posting function
# # -----------------------------
# # from django.http import StreamingHttpResponse
# # def post_to_twitter(tweets, creds):
# # # Authenticate with v2 Client
# #     client = tweepy.Client(
# #         consumer_key=creds["API_KEY"],
# #         consumer_secret=creds["API_SECRET"],
# #         access_token=creds["ACCESS_TOKEN"],
# #         access_token_secret=creds["ACCESS_SECRET"]
# #     )
# #     MAX_LENGTH = 100 
    
# #     def event_stream():
# #         for tweet_text in tweets:
# #             try:
# #                 client.create_tweet(text=tweet_text)
# #                 msg = f"✅ Posted: {tweet_text}"[:MAX_LENGTH]
# #                 yield f"data: {msg}\n\n"  # SSE format
# #                 print(msg)
# #                 time.sleep(65)  # delay between tweets
# #             except Exception as e:
# #                 error_msg = f"❌ Error posting: {e}"
# #                 yield f"data: {error_msg}\n\n"
# #                 print(error_msg)
# #     return StreamingHttpResponse(event_stream(), content_type = "text/event-stream")

# from django.http import StreamingHttpResponse

# def post_tweets_stream(request, account):
#     # Map account to scraper and creds
#     if account == "sportslab":
#         tweets = sportslab()
#         creds = sportslab_creds
#     elif account == "tennis":
#         tweets = tennis()
#         creds = tennis_updates5_creds
#     elif account == "wrestling4u0":
#         tweets = wwe()
#         creds = wwe_creds
#     elif account == "football":
#         tweets = football()
#         creds = football_creds
#     else:
#         return StreamingHttpResponse("❌ Invalid account selected.\n", content_type="text/event-stream")
    
#     # Tweepy client
#     client = tweepy.Client(
#         consumer_key=creds["API_KEY"],
#         consumer_secret=creds["API_SECRET"],
#         access_token=creds["ACCESS_TOKEN"],
#         access_token_secret=creds["ACCESS_SECRET"]
#     )

#     def event_stream():
#         for tweet_text in tweets:
#             try:
#                 client.create_tweet(text=tweet_text)
#                 yield f"data: ✅ Posted: {tweet_text}\n\n"
#                 time.sleep(65)
#             except Exception as e:
#                 yield f"data: ❌ Error posting: {e}\n\n"

#     return StreamingHttpResponse(event_stream(), content_type="text/event-stream")



# # -----------------------------
# # 1. Twitter API credentials
# # -----------------------------
# sportslab_creds = {
#     "API_KEY": "pPfQT1FHPKiYvVQSTOX2RYN65",
#     "API_SECRET": "FtiTWE6MA2ZRkd4QUm6FAKaTaEC8rfHHjJIzRj2dBJBvzYhtP4",
#     "ACCESS_TOKEN": "713029236756520960-z4ibkj12ykjpMXQCG0pkiWZtZwiQatj",
#     "ACCESS_SECRET": "zNeGbXWHYje0z0jDc9Se12C31M35zaIt89lPeZRlhbD9g",
# }

# tennis_updates5_creds = {
#     "API_KEY": "oIO6XVjigEvb1ZTncxAy8kER3",
#     "API_SECRET": "EV6em4nuAGDGlXZeejYg7k6oti5BxyVOiM1LwnfTkrnTDJSKfC",
#     "ACCESS_TOKEN": "1625067990621499393-aibTO3RM4c3LrvpDyGAUUauThDojwx",
#     "ACCESS_SECRET": "4D5n4PJ2xFxzlKhnq65UjHrqrQtx0V2gn7t1VHlcX3m3k",
# }

# wwe_creds = {
#     "API_KEY": "THkJu27h9DZ0NhKk6chLUVpOj",
#     "API_SECRET": "yLDcSUvwNFYnvXQebHJ4aPwyT39DA5HBynhpbOC78U6iEBhg5C",
#     "ACCESS_TOKEN": "717010499347435521-QP1kWvyps5dS7JuIaD3NGqxLjbEu2C8",
#     "ACCESS_SECRET": "FJTcwD3T7fUrWWkrAHEhuffDsEHthVuGgBzlz9pWWTtTb",
# }

# football_creds = {
#     "API_KEY": "Lo84o9AnFwDV2qHSZ9do9OV5b",
#     "API_SECRET": "OXXrkodbMbPRKxxQVOVhr1nWK5BdGMfLTwyrN7q8N3VCdfFgjn",
#     "ACCESS_TOKEN": "1586587260723466240-bn4F2mbknWNl7KAH7cRpA7nJsneRf9",
#     "ACCESS_SECRET": "rZuTkKALpSsbiR3MFKNERiGTzO43g8XfOI612Kxu0CqNy",
# }
# # Create your views here.
# def home(request):
#     return render(request, "home.html")
#     # status_message = ""
#     # if request.method == "POST":
#     #     if request.POST.get("account") == "sportslab":
#     #         result = sportslab()
#     #         status_message = post_to_twitter(result, sportslab_creds)
#     #     elif request.POST.get("account") == "tennis":
#     #         result = tennis()
#     #         status_message = post_to_twitter(result, tennis_updates5_creds)
#     #     elif request.POST.get("account") == "wrestling4u0":
#     #         result = wwe()
#     #         status_message = post_to_twitter(result, wwe_creds)
#     #     elif request.POST.get("account") == "football":
#             # result = football()
#             # status_message = post_to_twitter(result, football_creds)
            
   
   
   
#    ------------------------------------------
from django.shortcuts import render
from django.http import StreamingHttpResponse
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
import tweepy
import time

# -----------------------------
# Twitter API credentials
# -----------------------------
sportslab_creds = {
    "API_KEY": "pPfQT1FHPKiYvVQSTOX2RYN65",
    "API_SECRET": "FtiTWE6MA2ZRkd4QUm6FAKaTaEC8rfHHjJIzRj2dBJBvzYhtP4",
    "ACCESS_TOKEN": "713029236756520960-z4ibkj12ykjpMXQCG0pkiWZtZwiQatj",
    "ACCESS_SECRET": "zNeGbXWHYje0z0jDc9Se12C31M35zaIt89lPeZRlhbD9g",
}

tennis_updates5_creds = {
    "API_KEY": "oIO6XVjigEvb1ZTncxAy8kER3",
    "API_SECRET": "EV6em4nuAGDGlXZeejYg7k6oti5BxyVOiM1LwnfTkrnTDJSKfC",
    "ACCESS_TOKEN": "1625067990621499393-aibTO3RM4c3LrvpDyGAUUauThDojwx",
    "ACCESS_SECRET": "4D5n4PJ2xFxzlKhnq65UjHrqrQtx0V2gn7t1VHlcX3m3k",
}

wwe_creds = {
    "API_KEY": "THkJu27h9DZ0NhKk6chLUVpOj",
    "API_SECRET": "yLDcSUvwNFYnvXQebHJ4aPwyT39DA5HBynhpbOC78U6iEBhg5C",
    "ACCESS_TOKEN": "717010499347435521-QP1kWvyps5dS7JuIaD3NGqxLjbEu2C8",
    "ACCESS_SECRET": "FJTcwD3T7fUrWWkrAHEhuffDsEHthVuGgBzlz9pWWTtTb",
}

football_creds = {
    "API_KEY": "Lo84o9AnFwDV2qHSZ9do9OV5b",
    "API_SECRET": "OXXrkodbMbPRKxxQVOVhr1nWK5BdGMfLTwyrN7q8N3VCdfFgjn",
    "ACCESS_TOKEN": "1586587260723466240-bn4F2mbknWNl7KAH7cRpA7nJsneRf9",
    "ACCESS_SECRET": "rZuTkKALpSsbiR3MFKNERiGTzO43g8XfOI612Kxu0CqNy",
}

# -----------------------------
# Scraper function
# -----------------------------
def scrape_articles(url, base="https://www.sportskeeda.com", limit=5):
    result = requests.get(url)
    doc = BeautifulSoup(result.text, "html.parser")
    feed = doc.find_all("div", class_="feed-item-secondary")[:limit]

    tweets = []
    for f in feed:
        a_tag = f.find("a", href=True)
        if a_tag:
            link = urljoin(base, a_tag["href"]) + "#key2=905920"
            title = a_tag.text.strip()
            tweets.append(f"{title}\n{link}")
    return tweets

def sportslab(): return scrape_articles("https://www.sportskeeda.com/nfl/news")
def tennis(): return scrape_articles("https://www.sportskeeda.com/tennis/news")
def wwe(): return scrape_articles("https://www.sportskeeda.com/wwe/news")
def football(): return scrape_articles("https://www.sportskeeda.com/football/news")

# -----------------------------
# Views
# -----------------------------
def home(request):
    return render(request, "home.html")

def post_tweets_stream(request, account):
    account = account.strip().lower()

    if account == "sportslab":
        tweets = sportslab()
        creds = sportslab_creds
    elif account == "tennis":
        tweets = tennis()
        creds = tennis_updates5_creds
    elif account == "wrestling4u0":
        tweets = wwe()
        creds = wwe_creds
    elif account == "football":
        tweets = football()
        creds = football_creds
    else:
        return StreamingHttpResponse("data: ❌ Invalid account selected.\n\n",
                                     content_type="text/event-stream")

    client = tweepy.Client(
        consumer_key=creds["API_KEY"],
        consumer_secret=creds["API_SECRET"],
        access_token=creds["ACCESS_TOKEN"],
        access_token_secret=creds["ACCESS_SECRET"]
    )

    def event_stream():
        yield "data: 🔹 Starting posting...\n\n"
        for tweet_text in tweets:
            try:
                client.create_tweet(text=tweet_text)
                yield f"data: ✅ Posted: {tweet_text}\n\n"
                time.sleep(65)  # delay between tweets
            except Exception as e:
                yield f"data: ❌ Error posting: {e}\n\n"

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")
