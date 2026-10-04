import requests


def goi_api(url):
    try:
        response = requests.get(url)
        return response.json()

    except requests.exceptions.RequestException:
        print("Loi ket noi, khong goi duoc API")
        return None


ket_qua1 = goi_api("https://api.chucknorris.io/jokes/random")
print(ket_qua1)

key_qua2 = goi_api("https://khong-ton-tai-123456.com")
print(key_qua2)