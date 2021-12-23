import datetime

import pandas
import seaborn

FIDELITY_DATE_FORMAT = "%Y/%m/%d-%H:%M:%S"


def analyze():
    print('What downloaded ticker data would you like to analyze?')
    ticker = input('  ticker: ')
    data = pandas.read_json(f'data/{ticker}.json')
    converted_timestamps = data["lt"].map(lambda s: datetime.datetime.strptime(s, FIDELITY_DATE_FORMAT))
    data["lt"] = converted_timestamps

    seaborn.displot(data, x="lt", y="cl")
