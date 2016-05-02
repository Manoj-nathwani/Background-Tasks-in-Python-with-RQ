import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return '---> ' + str(len(resp.text.split()))
