import json


def convert():
    print('What downloaded ticker data would you like to convert to CSV?')
    ticker = input('  ticker: ')
    with open(f'data/{ticker}.json') as json_file:
        data = json.load(json_file)

    # now that we have data, we can convert to csv maybe?
    keys = data[0].keys()
    # keys_extra_quotes = map(lambda x: f'\'{x}\'', keys)
    csv_header = ','.join(keys)
    csv_header = f'{csv_header}\n'

    file_object = open(f'data/{ticker}.csv', 'a')
    file_object.write(csv_header)
    for day in data:
        if day['lt'].endswith('-00:00:00'):
            day['lt'] = day['lt'][:-9]
        day_data = []
        for key in keys:
            day_data.append(day[key])
        day_string = ','.join(day_data)
        day_string = f'{day_string}\n'
        file_object.write(day_string)

    file_object.close()
