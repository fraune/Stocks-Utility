from analyze.analyze import analyze
from convert.convert import convert
from download.download import download


def welcome():
    print('Welcome.')
    print('  1 = download')
    print('  2 = convert')
    print('  3 = analyze')
    choice = input('What would you like to do: ')

    int_choice = int(choice)
    if int_choice == 1:
        download()
    elif int_choice == 2:
        convert()
    elif int_choice == 3:
        analyze()
