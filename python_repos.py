import requests

#wykonanie wywołania api i zachowanie otrzymanej odpowiedzi
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'} #używana przez githuba wersja api
r = requests.get(url,headers=headers) #kod stanu 200 wskazuje na żądanie zakończone sukcesem, odpowiedź jest w formacie json
print(f"Kod stanu: {r.status_code}")
#umieszczenie odpowiedzi API w zmiennej
response_dict = r.json()    #zamieniamy zmienną z postaci json na słownik
print(f"Całkowita liczba repozytoriów: {response_dict['total_count']}")

#przetworzenie informacji o repozytoriach
repo_dicts = response_dict['items']
print(f"Liczba zwróconych repozytoriów: {len(repo_dicts)}")

print("\nwybrane informacje o każdym repozytorium: ")
for repo in repo_dicts:
    print(f"Nazwa: {repo['name']}")
    print(f"Właściciel: {repo['owner']['login']}")
    print(f"Gwiazdki: {repo['stargazers_count']}")
    print(f"Repozytorium: {repo['html_url']}")
    print(f"Opis: {repo['description']}")

#przeanalizowanie pierwszego repozytorium
# repo_dict = repo_dicts[0]

# print(f"\nWybrane informacje o pierwszym repozytorium:")
# print(f"Nazwa: {repo_dict['name']}")
# print(f"Właściciel: {repo_dict['owner']['login']}")
# print(f"Gwiazdki: {repo_dict['stargazers_count']}")
# print(f"Repozytorium: {repo_dict['html_url']}")
# print(f"Utworzone: {repo_dict['created_at']}")
# print(f"Uaktualnione: {repo_dict['updated_at']}")
# print(f"Opis: {repo_dict['description']}")