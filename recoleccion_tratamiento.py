import json, requests

def get_api_data(url):
    response = requests.get(url=url)
    json_dict  = response.json()
    json_list = []
    for e in json_dict:
        json_list.append((e,json_dict[e]))
    return json_list

if __name__ == "__main__":
    
    #test1
    print('Test1\n---------')
    print(get_api_data('https://invelonjobinterview.herokuapp.com/api/test1'))
    print('\n\n')

    #test2
    print('Test2\n---------')
    print(get_api_data('https://invelonjobinterview.herokuapp.com/api/test2'))
    print('\n\n')