import json, requests

def get_api_data(url):
    response = requests.get(url=url)
    json_dict  = response.json()
    json_list = []
    for e in json_dict:
        json_list.append((e,json_dict[e]))
    return json_list

