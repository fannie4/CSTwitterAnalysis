def collect_candidate(nom_candidat):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = nom_candidat, count = 200)
    for status in statuses:
        print(status.text)
    return statuses

