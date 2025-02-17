import requests
import json

def main():
    address = 'localhost'
    port = '62698'
    res = requests.get('http://' + address + ':' + port + '/v1/timers/current')
    print(res.text)

if __name__=="__main__":
    main()