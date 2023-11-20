import requests
from PIL import Image
from io import BytesIO


def download(query: str, pages: int):
    header = {
        'Authorization': 'ct41HkrcdJ7MRH2Suli4YFGI3R88ZkKhEYCCqx23c2CDflDT4tHwQHgg'}
    params = {
        'query': query,
        'per_page': 1
    }
    url = f"https://api.pexels.com/v1/search"

    while pages >= 1:
        params['page'] = pages
        r = requests.get(url, headers=header, params=params)
        if r.status_code == 200:
            _r = r.json()
            for i in _r.get('photos'):
                _img_url = i.get('src').get('original')
                resp = requests.get(_img_url)
                print(_img_url)

                image = Image.open(BytesIO(resp.content))
                image.save(f'media/{query}_{pages}.{_img_url.split(".")[-1]}')
        else:
            print(r.text)
        pages = pages - 1


def main() -> None:
    query = input('Query: ')
    pages = int(input('Pages: '))
    download(query, pages)


main()
