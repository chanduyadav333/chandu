import os

import requests
import time

img_urls = [
'https://www.peakpx.com/en/search?q=ntr'
]

t1 = time.perf_counter()

for img_url in img_urls:
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

finish = time.perf_counter()
#print(f'Finised in {finish - start} seconds')