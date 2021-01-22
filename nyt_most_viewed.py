from requests import get
import json

url='https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key=55CCF627GGGUDrAeClzdXjmCUU4cGGXF'
nyt = get(url).json()
data = json.dumps(nyt, sort_keys=True, indent=4)

for x in range(0, 5):
    print(nyt['results'][x]['title'])
