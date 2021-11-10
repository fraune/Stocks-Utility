import json
from enum import Enum

import requests


class Frequency(Enum):
    y = "Yearly"
    m = "Monthly"
    d = "Daily"


def download():
    print("Hello. What would you like to download from Fidelity?")
    ticker = input("  ticker: ")
    frequency_character = input("  frequency (y/m/d): ")
    frequency_string = Frequency[frequency_character].value
    get_data(ticker, frequency_string)


# TODO: Save to file as JSON or load series
# TODO: Add more param options for user
def get_data(ticker: str, frequency: str):
    url = f'https://fastquote.fidelity.com/service/marketdata/historical/chart/json?productid=research&symbols={ticker}&startDate=1970/01/01&endDate=2021/09/05&barWidth={frequency}&extendedHours=N&quoteType=R&corpActions=Y&timestamp=start&uuid=6debdc8c-aea9-11e3-962f-9bc8b53daa77&callback=null'
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
