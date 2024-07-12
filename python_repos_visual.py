import requests

from plotly.graph_objs import Bar
from plotly import offline

#wykonanie wywołania api i zachowanie otrzymanej odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} #używana przez githuba wersja api
r = requests.get(url,headers=headers) #kod stanu 200 wskazuje na żądanie zakończone sukcesem, odpowiedź jest w formacie json
print(f"Kod stanu: {r.status_code}")
#umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()    #zamieniamy zmienną z postaci json na słownik
repo_dicts = response_dict['items']
repo_names,stars,labels = [],[],[]

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

#utworzenie wizualizacji
data = [{
    'type':'bar',
    'x':repo_names,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]
my_layout = {
    'title' : 'Oznaczone największą liczbą gwiazdek projekty pythona w serwisie Github',
    'titlefont':{'size':28},
    'xaxis' : {
        'title':'Repozytorium',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
        },
    'yaxis' : {
        'title':'Ilość gwiazdek',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
        },

}

fig = {'data':data,'layout':my_layout}
offline.plot(fig, filename='python_repos.html')