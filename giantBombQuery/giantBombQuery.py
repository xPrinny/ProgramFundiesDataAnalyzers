import requests
from pathlib import Path

# Declaring variables
gameList = []
offsetQuery = 0
apiKey = ''

# If file exist, read file for first line to see offset.
if list(Path().glob('gameList.txt')):
    with open('gameList.txt', encoding='utf-8', errors='ignore') as f:
        offsetQuery = int(f.readline())
        gameList = list(eval(f.readline()))

# Setting POST request
url = 'https://www.giantbomb.com/api/games'
headers = {
    'User-Agent': 'Scrapping for school project'
}
paramsValue = {
    'api_key': apiKey,
    'format': 'json',
    'field_list': 'name',
    'offset': offsetQuery
}

# First GET request
GETOut = requests.get(url, params=paramsValue, headers=headers).json()

# Save total amount of results
totalGames = GETOut['number_of_total_results']
offsetQuery += 100
gameList += GETOut['results'] 

# Loop GET request as many times till it finishes or rate limited
try:
    while totalGames > offsetQuery:
        GETOut = requests.get(url, params={
            'api_key': apiKey,
            'format': 'json',
            'field_list': 'name',
            'offset': offsetQuery}, headers=headers)
        GETOut = GETOut.json()
        if GETOut['results']:
            gameList += GETOut['results']
            offsetQuery += 100
        else:
            break
except Exception as e:
    print(GETOut)

with open('gameList.txt', 'w', encoding='utf-8', errors='ignore') as text_file:
    # Add current Query to first like
    text_file.write(str(offsetQuery) + '\n')

    for x in gameList:
        # Convert to raw, escape all quotes, replace double quote and change it to single quote, remove escape from quote at start, remove escape from quote at the end of 'name'
        if "'" in x['name']:
            text_file.write('r"' + str(x).replace("'", "\\\\'").replace('"', '\'').replace('{\\\\', '{').replace('\\\\\':', '\':') + '"')
        else:
            text_file.write(str(x))

with open('gameList.txt', encoding='utf-8', errors='ignore') as f:
    # Skip first line
    f.readline()
    gameList = f.readline()

# Reopen and remove all raw quotes and fix format
with open('gameList.txt', 'w', encoding='utf-8', errors='ignore') as text_file:
    gameList = gameList.replace('r"', '').replace('"', '').replace('}{', '}, {')

    # Add current Query to first like
    text_file.write(str(offsetQuery) + '\n')
    text_file.write(gameList)