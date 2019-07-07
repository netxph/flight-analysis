import zipfile
import requests
import os
import bz2

def main():

    if not os.path.exists('data'):
        os.makedirs('data')

    if not os.path.exists('download'):
        os.makedirs('download')

    for year in range(1987, 2009):
        url = f'http://stat-computing.org/dataexpo/2009/{year}.csv.bz2'
        print(f'Downloading {url}...')
        r = requests.get(url)

        bz2_file = f'download/{year}.csv.bz2'
        print(f'Writing to {bz2_file}')
        with open(bz2_file, 'wb') as f:
            f.write(r.content)

        csv_file = f'data/{year}.csv'
        print(f'Extracting to {csv_file}')
        bz2_comp = bz2.BZ2File(bz2_file, 'rb')
        with open(csv_file, 'wb') as f:
            f.write(bz2_comp.read())

        print('Done.')

if __name__ == '__main__':
    main()
