#!/usr/bin/env python3

import sys
import csv

def read_csv():

    with open('input.txt', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_list = list(csv_reader)
        offline_count = 0

        for row in csv_list:
            if row[1] == ' Offline':
                offline_count += 1
        # print(f'Found ({offline_count}) offline drives')
        print(f'Found (' + str(offline_count) + ') offline drives:\n')

        for row in csv_list:
            if row[1] == ' Offline':
                i=0

                title = list(row[0])
                del title[0:6]
                title.insert(4,":")

                print(''.join(title))

                while i < 11:
                    if i > 1:
                        print('\t' + row[i])
                    i += 1
                # offline_count += 1


def main():
        read_csv()

if __name__ == '__main__':
    main()