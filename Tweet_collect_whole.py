def collect_whole():
    connexion = twitter_setup()
    tweets = connexion.search *
    for tweet in tweets:
        print(tweet.text)
        
print (collect_whole())
