import requests
from qiniu import Auth, put_file


# def up_photo(key, file_path, bucket_name):
#     access_key = 'KgHe4AAvPJStXOlhxGB3ds-3ndsUxS-wypBwKAgW'
#     secret_key = '6l1ujW79c4Zwo5XmpznDLTdQLaobW3As3r9fnol1'
#
#     q = Auth(access_key, secret_key)
#
#     token = q.upload_token(bucket_name, key, 3600)
#
#     ret, info = put_file(token, key, file_path)
#
#     return info.status_code, ret.get('key')


def sm_photo(path):
    url = "https://sm.ms/api/v2/upload?inajax=1"

    proxies = {'http': '159.138.55.160:25596'}

    file = open(path, 'rb')

    smfile = {'smfile': file, 'file_id': 0}

    header = {'Authorization': "D1YVhkeJPPgMILWFi8zDTJkvCPwJnmtE"}

    results = requests.get('http://lumtest.com/myip.json', proxies=proxies)

    print(results.json())
    results = requests.post(url, headers=header, proxies=proxies, files=smfile)

    dict_info = results.json()
    print(dict_info)
    data = dict_info.get('data')

    code = dict_info.get('code')

    if code == 'exception':
        return 'F'
    elif code != 'success':
        return False
    else:
        url = data.get('url')
        return url
