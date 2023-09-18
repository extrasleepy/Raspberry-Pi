import requests

url = "https://dad-jokes.p.rapidapi.com/random/joke"

headers = {
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
    'x-rapidapi-key': "Your Key"
    }

response = requests.request("GET", url, headers=headers)
total=response.json()
print(total)
setup = total['body'][0]['setup']
print(setup)
punchline = total['body'][0]['punchline']
print(punchline)
