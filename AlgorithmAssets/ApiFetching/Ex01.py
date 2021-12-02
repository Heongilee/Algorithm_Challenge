from datetime import datetime
import requests, json, sys, arrow, matplotlib.pyplot as plt, numpy as np

'''
# requirements.txt

arrow
'''
class Connection():
    def __init__(self, protocol, dns, context_path):
        self.protocol = protocol
        self.dns = dns
        self.context_path = context_path
        
        self.API_PREFIX = self.protocol + "://" + self.dns + self.context_path + "?"

    def request_get(self, **query_params):
        request_url = self.API_PREFIX
        for k, v in query_params.items():
            request_url += str(k) + "=" + str(v) + "&"
        request_url = request_url[:len(request_url) - 1]
        return json.loads(requests.get(request_url).text)

if __name__ == '__main__':
    c = Connection("http", "openapi.data.go.kr", "/openapi/service/rest/Covid19/getCovid19InfStateJson")
    response = c.request_get(
        ServiceKey = "53%2BVGqHRUDSOrCV%2FwXCt%2BxN5qubVlN5yNl%2BgDtEt%2B7uyT%2FKCBB07j0iiZPsXlQvI4zEOUgA7JoCJXmE3Y2AvSw%3D%3D", 
        _type = "json",
        pageNo = 1, 
        numOfRows = 5,
        startCreateDt = "".join(map(str, str(arrow.now().shift(days=-5).date()).split("-"))),
        endCreateDt = 20991231
    )
    
    try:
        item = response['response']['body']['items']['item']
        dates = [item[i]['createDt'].split(" ")[0] for i in range(len(item) - 1)]
        values = [item[i]['decideCnt'] - item[i + 1]['decideCnt'] for i in range(len(item) - 1)]
    except TypeError as e1:
        print("ERROR : 파싱 에러")
        sys.exit(0)
    except KeyError as e2:
        print("ERROR : 데이터 길이 부족")
        sys.exit(0)
    
    # matplotlib로 데이터 시각화
    x = np.arange(5)
    if len(dates) < 5:
        dates = [0] + dates
    plt.title("New cases of COVID-19")
    plt.bar(dates, values, color = ['dodgerblue'] + ['gray' for _ in range(len(dates) - 1)])
    for i, d in enumerate(dates):
        color = 'dodgerblue' if i == 0 else 'gray'
        plt.text(d, values[i], values[i],
                fontsize = 9,
                color=color,
                horizontalalignment='center',  # horizontalalignment (left, center, right)
                verticalalignment='bottom')    # verticalalignment (top, center, bottom)
    # plt.xticks(x, dates)
    plt.show()    