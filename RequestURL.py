import requests


def request_web(url, headers='none', encode = 'utf-8',check_string="headers"):
    request = requests.get(url)
    request.encoding=encode

    if request.status_code == 200:
        if check_string in request.text:
            print('All functional without headers')
            return request
        else:
            status = 'half-way'
    else:
        status = 'half-way'

    if status == 'half-way':
        if headers == 'none':
            print('Request Headers, Please input headers')
            return None
        else:
            request = requests.get(url, headers=headers)
            request.encoding=encode
            if check_string in request.text:
                print("All functional with headers")
                return request
            else:
                print('status 200 with headers, but not full html')
                return None
