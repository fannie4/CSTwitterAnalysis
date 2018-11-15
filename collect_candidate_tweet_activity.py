def collect_retweet(id_user):
    connexion = twitter_setup()
    nbdetweets=100
    //on cherche à faire apparaitre 100 retweets
    for tweet in tweepy.Cursor(api.search,id_user).items(nbdetweets):
        try:
            tweet.retweet()
            print("Tweet retweeté :")
        except StopIteration:
            break
            