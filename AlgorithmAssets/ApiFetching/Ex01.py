# 파이썬 언어 특성상 %를 읽는데에서 문제가 생기는듯...
# http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=53%2BVGqHRUDSOrCV%2FwXCt%2BxN5qubVlN5yNl%2BgDtEt%2B7uyT%2FKCBB07j0iiZPsXlQvI4zEOUgA7JoCJXmE3Y2AvSw%3D%3D/pageNo=1/numOfRows10/_typejson/startCreateDt20200120/endCreateDt20200120
# http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=53%2BVGqHRUDSOrCV%2FwXCt%2BxN5qubVlN5yNl%2BgDtEt%2B7uyT%2FKCBB07j0iiZPsXlQvI4zEOUgA7JoCJXmE3Y2AvSw%3D%3D&pageNo=1&numOfRows=10&_type=json&startCreateDt=20200120&endCreateDt=20201222

import requests
import json

def requestGet(host, path, payload):
    url = host + "/" + path
    url += "?serviceKey=" + payload['serviceKey']
    url += "&pageNo=" + payload['pageNo']
    url += "&numOfRows" + payload['numOfRows']
    url += "&_type" + payload['_type']
    url += "&startCreateDt" + payload['startCreateDt']
    url += "&endCreateDt" + payload['endCreateDt']
    
    return requests.get(url=url)

if __name__ == '__main__':
    payload = {
        'serviceKey': '53%2BVGqHRUDSOrCV%2FwXCt%2BxN5qubVlN5yNl%2BgDtEt%2B7uyT%2FKCBB07j0iiZPsXlQvI4zEOUgA7JoCJXmE3Y2AvSw%3D%3D',
        'pageNo': '1',
        'numOfRows': '10',
        '_type': 'json',
        'startCreateDt': '20200120',
        'endCreateDt': '20200120'
    }
    res = requestGet("http://openapi.data.go.kr", "openapi/service/rest/Covid19/getCovid19SidoInfStateJson", payload)
    # print(res.json()['response']['body']['items']['item'][0])
    print(res.status_code)