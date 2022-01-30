from pytwitterscraper import TwitterScraper

tw = TwitterScraper()
profile = tw.get_profile(name="kabu01")
print(profile.__dict__)

tweets = tw.get_tweets(profile.id, count=20)
for tweet in tweets.contents:
    print(tweet)
