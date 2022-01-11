import ftplib
import os

FTP_HOST = 'ftp.nasdaqtrader.com'
MAIN_LIST = 'nasdaqlisted.txt'
ALTERNATIVE_LIST = 'otherlisted.txt'


def update_ticker_lists():
    ftp = ftplib.FTP()
    ftp.connect(FTP_HOST)
    ftp.login()
    ftp.cwd('/SymbolDirectory')
    ftp.retrbinary(f'RETR {MAIN_LIST}', open(f'data/{MAIN_LIST}', 'wb').write)
    ftp.retrbinary(f'RETR {ALTERNATIVE_LIST}', open(f'data/{ALTERNATIVE_LIST}', 'wb').write)

    # The last line of each file contains a metadata record and new line. You might want to delete two lines off the end
    # if you plan on analyzing this data or running an algorithm on it.

    # delete_last_line_of_file(f'data/{MAIN_LIST}')
    # delete_last_line_of_file(f'data/{ALTERNATIVE_LIST}')


# Unfinished line deleting code below (only deletes one line at a time)
def delete_last_line_of_file(filepath: str):
    with open(filepath, 'r+', encoding='utf-8') as file:
        # Move the pointer (similar to a cursor in a text editor) to the end of the file
        file.seek(0, os.SEEK_END)

        # This code means the following code skips the very last character in the file -
        # i.e. in the case the last line is null we delete the last line
        # and the penultimate one
        pos = file.tell() - 1

        # Read each character in the file one at a time from the penultimate
        # character going backwards, searching for a newline character
        # If we find a new line, exit the search
        while pos > 0 and file.read(1) != '\n':
            pos -= 1
            file.seek(pos, os.SEEK_SET)

        # So long as we're not at the start of the file, delete all the characters ahead
        # of this position
        if pos > 0:
            file.seek(pos, os.SEEK_SET)
            file.truncate()
