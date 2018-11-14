import tweepy

# We import our access keys:

# Consume:
CONSUMER_KEY    = 'nwVs6YNP10O0vzWOHkVJ0eDgR'
CONSUMER_SECRET = 'aVcA7nuqLFc1CVb3uWCM4yEZYOP5qIjWHyOZ3fsZ3EOiqhoxnU'

# Access:
ACCESS_TOKEN  = '928109258-XDscdmCehF5ZRStwObVkFaTleR90q96nk5hJ3Zqh'
ACCESS_SECRET = 'pJksbGMEPtjtkmAa2Yu4594dIdt5nrNrxCAhqCJOdQcRk'


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

print(twitter_setup())

//on collecte les tweets relatifs à Emmanuel Macron, dans lesquels il a été identifié
def collect():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=50)
    for tweet in tweets:
        print(tweet.text)
        
print (collect())

//on collecte les tweets avec des mots clés relatifs au nom du candidat 
//ouvre les fichiers et renvoie les mots clés dans une liste
//le numéro du candidat est utile comme l'user_id

def get_candidate_queries(num_candidate,file_path):
    connexion=twitter_setup
    file_path = open("keywords_candidate_num_candidate.txt","hastag_candidate_num_candidate.txt", "r")
    for words in file_path :
        if user_id=14445328
        tweets1= connexion.search("num_candidate") 
        
        print(tweets1)
           


//On collecte les tweets des personnes qui ont parlé de cet user_id, et en renvoient 200
def collect_by_user(user_id):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    for status in statuses:
        print(status.text)
    return statuses
    

print (collect_by_user(151304840))



from tweepy.streaming import StreamListener
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        if  str(status) == "420":
            print(status)
            print("You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

//renvoie en continu et en temps réel les tweets qui sont publiés et qui concernent Macron
def collect_by_streaming():

    connexion = twitter_setup()
    listener = StdOutListener()
    stream=tweepy.Stream(auth = connexion.auth, listener=listener)
    stream.filter(track=['Emmanuel Macron'])

print(collect_by_streaming)





