import requests


def download(q, p):
    header = {
        'Authorization': 'ct41HkrcdJ7MRH2Suli4YFGI3R88ZkKhEYCCqx23c2CDflDT4tHwQHgg'}
    while p >= 1:
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={p}"
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            _r = r.json()
            for i in _r.get('photos'):
                print(i.get('url'))
        else:
            print(r.text)
        p = p - 1


def main() -> None:
    query = input('Query: ')
    page = int(input('Pages: '))
    download(query, page)


main()
