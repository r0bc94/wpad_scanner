import requests
import asyncio

from typing import List, Tuple

TLDFILE = 'tlds.txt'
OUTFILE = 'results.txt'


def get_tlds_from_file(filename: str) -> List[str]:
    tlds = []
    with open(filename, 'r') as fil:
        tlds = fil.readlines()

    return [tld.replace('\n', '') for tld in tlds]

async def get_wpad_for_tld(tld: str) -> Tuple[str, bytearray]:
    url = f'http://wpad{tld}/wpad.dat'
    try:
        response = await asyncio.to_thread(requests.get, url, timeout=10)
    except requests.exceptions.ConnectionError:
        print(f'Connection to {url} failed')
        return '', bytearray()

    except requests.exceptions.Timeout:
        print(f'Connection to {url} failed: Timeout')
        return '', bytearray()

    if response.status_code != 200 and response.status_code != 201:
        print(url + ' returned error code: ' + str(response.status_code))
    
    print('successfully obtained wpad.dat file from ' + url)
    return url, response.content

async def main():
    results = []
    for tld in get_tlds_from_file(TLDFILE):
        result = get_wpad_for_tld(tld)
        results.append(result)

    results_bytes = await asyncio.gather(*results)

    print('Done, writing results to ' + OUTFILE)
    with open(OUTFILE, 'w') as outfile:
        for result in results_bytes: 
            if not result[0]:
                continue

            outfile.write('- - - - - - - - - - - -')
            outfile.write(result[0])
            outfile.write('- - - - - - - - - - - -\n')
            outfile.write(result[1].decode())
            outfile.write('\n')

print('start scanning for wpad files..')
# print(repr(get_tlds_from_file(TLDFILE)))
asyncio.run(main())
