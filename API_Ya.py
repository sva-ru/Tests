import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def upload(self, dir_name: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/"
        headers = self.get_headers()
        params = {"path": dir_name}
        # response = requests.get(upload_url, headers=headers, params=params)
        # print(response.status_code)
        # if response.status_code == 404:
        response = requests.put(upload_url, headers=headers, params=params)
        return response.status_code

# if __name__ == '__main__':
#     uploader = YaUploader('111111111')
#     print(uploader.upload('test'))