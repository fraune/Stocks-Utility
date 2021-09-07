import json

import requests


def download():
    print("Hello. Input a stock ticker to download from Fidelity.")
    x = input("  ticker: ")
    get_data(x)


def get_data(ticker):
    url = f'https://fastquote.fidelity.com/service/marketdata/historical/chart/json?productid=research&symbols={ticker}&startDate=1970/01/01&endDate=2021/09/05&barWidth=Daily&extendedHours=N&quoteType=R&corpActions=Y&timestamp=start&uuid=6debdc8c-aea9-11e3-962f-9bc8b53daa77&callback=null'
    result = requests.get(url)
    json_response = convert_fidelity_text_response_to_json(result.text)
    response_dict = json.loads(json_response)

    juicy_data = response_dict.get('Symbol')[0].get('BarList').get('BarRecord')
    with open(f'data/{ticker}.json', 'w') as outfile:
        json.dump(juicy_data, outfile)


def convert_fidelity_text_response_to_json(text: str):
    # remove callback junk
    if text.startswith('\nnull(\n') and text.endswith('\n)\n'):
        return text[7:-3]
    else:
        print('The text received was in an unrecognized format.')
        raise ValueError('The text received was in an unrecognized format.')
