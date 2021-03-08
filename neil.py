import requests
import json
import random
from  time import sleep
import argparse

api_key = "698bcb7032d2e85929e90bdbc49d6bf4"

parser = argparse.ArgumentParser()
parser.add_argument('words', type=str, nargs='+')

args = parser.parse_args()

words = args.words

out = ['']*len(words)

# GET SYNONYMS

for i, word in enumerate(words):

    
    req_string = f"https://words.bighugelabs.com/api/2/{api_key}/{word}/json"
    response = requests.get(req_string)
    
    if response.status_code != 200:
        print(f'warning: "{word}" had a problem')
        out[i] = word
    else:
        data = response.json()
        candidates = []
        for v in data.values():
            for a in v['syn']:
                candidates.append(a)
        out[i] = random.choice(candidates)

print(' '.join(out))
    

