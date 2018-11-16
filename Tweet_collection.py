import pandas as pd
import tweepy
import json
import numpy as np
import matplotlib.pyplot as plt



# We import our access keys:

# Consume:
CONSUMER_KEY    = 'nwVs6YNP10O0vzWOHkVJ0eDgR'
CONSUMER_SECRET = 'aVcA7nuqLFc1CVb3uWCM4yEZYOP5qIjWHyOZ3fsZ3EOiqhoxnU'

# Access:
ACCESS_TOKEN  = '928109258-XDscdmCehF5ZRStwObVkFaTleR90q96nk5hJ3Zqh'
ACCESS_SECRET = 'pJksbGMEPtjtkmAa2Yu4594dIdt5nrNrxCAhqCJOdQcRk'

#on ouvre le fichier json
with open('collected_tweet_1976143068.json')as json_data:
    data_dict=json.load(json_data)
    print(data_dict)



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

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="french",rpp=50)
    return tweets

"""print (collect())"""

"""on crér une fonction collet qui permet de transformer le fichier json en dataframe, en s'appuuant sur la fonction collect précdente qui renvoit une liste de tweets"""
"""on rentre dans le dictionnaire et la clé du dictionnaire devient le numéro de la colonne"""
"""on a un dataframe mais qu'il faut modifier pour l'avoir sous forme de tableau exploitable"""
def collect_as_DF():
    file=collect()
    searched_tweets=[status._json for status in file]
    json_file=json.dumps([object for object in searched_tweets])
    """dumps: pour enregistrer"""
    tweets=pd.read_json(json_file)
    print(tweets)

"""permet de créer le data frame de tweets et le renvoie sous forme de data (tableau à plusieurs colonnes"""
"""les colonnes sont len, l'ID, le data, la source, les likes, et RT'S"""

def collect_to_pandas_dataframe():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]
    # Max RTs:
    print("Le tweet avec le plus de retweets est : \n{}".format(data['tweet_textual_content'][rt]))
    print("Avec un nombre de retweet : {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))
    return data

'''print(collect_to_pandas_dataframe())'''

"""renvoie la moyenne du nombre de retweet"""
def mean_rt(df):
    print ("Le nombre moyen de retweets est : ")
    print(df['RTs'].mean())

df=collect_to_pandas_dataframe()

'''print(mean_rt(df))'''

"""renvoie la moyenne du nombre de likes par retweet"""
def mean_likes_rt(df):
    print("Le nombre moyen de likes est :")

'''print(mean_likes_rt(df))'''

def max_rt(df):
    print("Le nombre max de likes est :")
    print(df['RTs'].max())
print(max_rt(df))

"""tracé du nombre de retweets par tweet"""
def plot_rt(df):
    df["RTs"].plot()
    plt.ylabel("Nombre de retweets pour chaque tweet")
    plt.xlabel("Numéro du tweet")
    plt.title("Nombre de retweets en fonction du numéro du tweet")
    plt.show()

'''print(plot_rt(df))'''

#Fonctionnalité 6 : visualisation de l'évolution d'une caractéristique

'''Exemple:'''
tfav = pd.Series(data=df['Likes'].values, index=df['Date'])
tret = pd.Series(data=df['RTs'].values, index=df['Date'])

# Likes vs retweets visualization:
tfav.plot(figsize=(16,4), label="Likes", legend=True)
tret.plot(figsize=(16,4), label="Retweets", legend=True)

print(plt.show())

#On compare le nombre de retweet des posts d'Emmanuel Macron et ceux d'Edouard Philippe

#première fonction qui renvoie les tweets postés par Emmanuel Macron
def collect_tweets_by_Macron():
    connexion = twitter_setup()
    tweets = connexion.search(user = "EmmanuelMacron",language="fr",rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]
    # Max RTs:
    print("Le tweet avec le plus de retweets est : \n{}".format(data['tweet_textual_content'][rt]))
    print("Avec un nombre de retweet : {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))
    return data









