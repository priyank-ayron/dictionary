from django.shortcuts import render
import requests
from bs4 import BeautifulSoup


# Create your views here.
def index(request):
    return render(request, 'index.html')


def search(request):
    word = request.GET['word']
    res = requests.get('https://www.dictionary.com/browse/'+word)
    res2 = requests.get('https://api.api-ninjas.com/v1/thesaurus?word='+word, headers = {'X-Api-Key':'ORO+XkgIJtfRhrGCkJPMlQ==1Hb9yFiTFm7qY5zB'})
    if res:
        soup = BeautifulSoup(res.text, 'lxml')

        meaning = soup.find_all('div', {'value':'1'})
        meaning1 = meaning[0].getText()
    else:
        word = 'Sorry, ' + word + ' Is Not Found In Our Database'
        meaning1 = ''

    if res2:
        res2 = res2.json()
        se = res2['synonyms']
        ae = res2['antonyms']
    else:
        se = ''
        ae = ''

    results = {
        'word': word,
        'meaning': meaning1,
    }

    return render(request, 'search.html', {'se': se, 'ae': ae, 'results': results})