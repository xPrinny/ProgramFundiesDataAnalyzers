import requests
import csv

def get_top_twitch_streamers(clientID, tokenKey):
    headers = {
        'Client-ID': clientID,
        'Token': tokenKey,
    }
    params = {
        'platform': 'twitch',
        'time': '7-days',
    }
    try:
        r = requests.get("https://streamscharts.com/api/jazz/channels",params= params,headers=headers)
        data = r.json()
        if data is not None:
            return data["data"]
        else:
            raise Exception
    except:
        print("error")
        return False

# #put in csv
# def export_json_csv(json,file_name):
#     keysList = list(json[0].keys())
#     f = csv.writer(open(file_name, "w"))
#     f.writerow(keysList)
#     #for each row in json
#     for x in json:
#         xlist = []
#         #add row into list as per keys list
#         for i in range(0,len(keysList)):
#             xlist.append(x[keysList[i]])
#         #write into list
#         f.writerow(xlist)

# #not in use, if return > 0 = true
# def check_csv_exist(key,value,file_name):
#     x = 0
#     reader = csv.DictReader(open(file_name))
#     for row in reader:
#         if row[key] == value :
#             x += 1
#     return x