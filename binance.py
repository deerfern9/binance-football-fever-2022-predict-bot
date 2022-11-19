from random import choice
import requests
import time
from config import accounts

print("Telegram канал автора: @asiimov_near")

with open("proxy.txt", "r") as file:
    proxies = file.readlines()

predicts = {'D01': {'M01': [[0, 1], [0, 0], [1, 1], [1, 0], [1, 1], [1, 1]]}, 'D02': {'M02': [[1, 0], [2, 0], [0, 0], [1, 1], [3, 0], [1, 0], [2, 0]], 'M03': [[0, 1], [0, 1], [0, 2], [0, 2], [1, 1], [0, 0], [0, 1]], 'M04': [[1, 0], [1, 1], [1, 1], [0, 0], [0, 1]]}, 'D03': {'M05': [[1, 0], [2, 0], [2, 0], [2, 0], [3, 0], [3, 0]], 'M06': [[1, 0], [1, 0], [2, 0], [3, 0], [2, 0], [0, 0], [2, 1]], 'M07': [[1, 0], [0, 0], [1, 1], [1, 1], [0, 1]], 'M08': [[1, 0], [2, 0], [2, 1], [3, 0]]}, 'D04': {'M09': [[0, 1], [0, 0], [1, 1], [0, 2], [0, 1]], 'M10': [[1, 0], [2, 0], [2, 1], [1, 1]], 'M11': [[1, 0], [2, 0], [2, 0], [3, 0]],'M12': [[1, 0], [2, 0], [2, 1], [1, 1]]}, 'D05': {'M13': [[1, 0], [2, 0], [2, 1], [0, 0], [1, 1], [1, 0], [2, 0]],'M14': [[1, 0], [2, 0], [1, 0], [1, 1], [0, 0], [2, 1]],'M15': [[1, 0], [1, 0], [2, 0], [2, 0], [0, 0], [2, 0], [2, 1]],'M16': [[1, 0], [2, 0], [2, 0], [1, 0], [2, 1]]}, 'D06': {'M17': [[1, 0], [0, 1], [0, 0], [1, 1]],'M18': [[0, 1], [0, 0], [1, 1]],'M19': [[1, 0], [2, 0], [1, 1], [2, 1], [1, 0]],'M20': [[1, 0], [1, 0], [2, 0], [2, 0], [0, 0], [2, 1]]}, 'D07': {'M21': [[1, 0], [0, 1], [0, 0], [1, 1], [1, 1], [0, 0]],'M22': [[1, 0], [2, 0], [2, 1], [1, 1], [1, 0], [2, 0]],'M23': [[1, 0], [1, 1], [0, 0], [2, 0], [2, 1], [1, 0], [1, 0]],'M24': [[1, 0], [1, 0], [2, 0], [2, 0], [1, 1], [2, 1]]}, 'D08': {'M25': [[1, 0], [1, 0], [2, 0], [2, 1], [0, 0], [1, 1], [2, 0]],'M26': [[1, 0], [2, 0], [2, 1], [1, 1], [1, 0], [2, 0]],'M27': [[1, 0], [2, 0], [2, 1], [1, 1], [1, 0]],'M28': [[1, 0], [0, 0], [1, 1], [0, 1], [1, 1]]}, 'D09': {'M29': [[0, 1], [0, 2], [1, 1], [0, 0], [0, 1], [1, 2]],'M30': [[1, 0], [0, 0], [1, 1], [0, 1], [1, 1], [0, 0]],'M31': [[1, 0], [2, 0], [2, 1], [1, 1], [1, 0]],'M32': [[1, 0], [0, 0], [1, 1], [2, 1], [2, 0], [1, 1]]}, 'D10': {'M33': [[1, 0], [2, 0], [3, 0], [2, 1], [2, 0], [1, 0]],'M34': [[1, 0], [0, 0], [0, 1], [1, 1], [1, 1], [1, 1]],'M35': [[1, 1], [0, 1], [0, 2], [1, 2], [0, 1], [0, 2]],'M36': [[1, 1], [0, 1], [1, 2], [1, 1]]}, 'D11': {'M37': [[1, 1], [0, 1], [0, 2], [1, 2], [0, 1], [0, 2]],'M38': [[0, 1], [0, 2], [0, 3], [1, 2], [0, 1], [0, 2]],'M39': [[0, 1], [1, 1], [0, 2], [1, 2], [0, 1]],'M40' : [[0, 1], [0, 2], [1, 2], [1, 1], [0, 1]]}, 'D12': {'M41': [[1, 1], [0, 1], [1, 2], [1, 1]], 'M42': [[1, 0], [1, 1], [0, 1], [1, 1], [0, 0] ], 'M43': [[0, 1], [0, 2], [1, 2], [0, 3], [0, 2]], 'M44': [[1, 1], [0, 1], [0, 2], [1, 2], [0, 1]]}}

for n, list1 in enumerate(accounts):
    headers = {
        'authority': 'www.binance.com',
        'accept': '*/*',
        'accept-language': 'uk',
        'clienttype': 'web',
        'csrftoken': list1[1],
        'cookie': list1[0],
        'referer': 'https://www.binance.com/en/fan-token/football-fever-2022/match/detail/D09?utm_source=fan-token&registerChannel=ft_BFF',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
    }
    p = proxies[n].replace('\n', '')

    proxy = {'http': f'http://{p}/',
             'https': f'http://{p}/'}

    for day, matches in predicts.items():
        t = []
        for match, predict in matches.items():
            predict = choice(predict)
            t.append({
                'worldcupMatchId': match,
                'teamAScore': predict[0],
                'teamBScore': predict[1],
                'winnerTeam': None,
            })
        json_data = {
            'matchDayId': day,
            'scoreInfos': t
        }

        response = requests.post('https://www.binance.com/bapi/nft/v1/friendly/nft/fantoken/worldcup/daily-challenge/user-predict-match-day', proxies=proxy, headers=headers, json=json_data)
        print(response.text)

        pID = response.json()['data']['predictId']
        json_data1 = {
            'predictId': pID,
        }

        response = requests.post('https://www.binance.com/bapi/nft/v1/friendly/nft/fantoken/worldcup/daily-challenge/polling-user-predict-match-day', proxies=proxy, headers=headers, json=json_data1)

        print(response.text)
    print(p)
    time.sleep(15)

