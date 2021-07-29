import json

import bs4
import pandas as pd
import requests
import datetime
import sys


class OpenAPI :
    def date_range(self):
        dates = []
        for i in range(7):
            now = datetime.datetime.now()
            now7 = now - datetime.timedelta(days=i)
            dates.append(now7.strftime('%Y-%m-%d'))
        return dates

    def decide(self):
        now = datetime.datetime.now()
        endDt = now.strftime('%Y%m%d')
        now7 = now - datetime.timedelta(days=7)
        startDt = now7.strftime('%Y%m%d')

        url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
        result = requests.get(url);
        response = result.text.encode('utf-8');
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
        rows = xml_obj.find_all('item');

        result = []         # 최종 리스트
        nameList = []       # 컬럼 명

        rowsLen = len(rows);    # item의 개수
        for i in range(rowsLen) :
            item = rows[i].find_all();
            itemData = []  # 아이템의 데이터
            for j in range(len(item)) :
                if i == 0 :
                    nameList.append(item[j].name);
                text = item[j].text;
                itemData.append(text);
            result.append(itemData);

        data = pd.DataFrame(result, columns=nameList);
            # Index(['accDefRate', 'accExamCnt', 'accExamCompCnt', 'careCnt', 'clearCnt',
            #        'createDt', 'deathCnt', 'decideCnt', 'examCnt', 'resutlNegCnt', 'seq',
            #        'stateDt', 'stateTime', 'updateDt'],
            #       dtype='object')
        data = data.astype({'decideCnt':int});
        data_li = data['decideCnt'].to_list();

        results = {
            'datas' : data_li,
            'dates' : OpenAPI().date_range()
        }

        print(results)
        return results

    def clear(self):
        now = datetime.datetime.now()
        endDt = now.strftime('%Y%m%d')
        now7 = now - datetime.timedelta(days=7)
        startDt = now7.strftime('%Y%m%d')

        url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
        result = requests.get(url);
        response = result.text.encode('utf-8');
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
        rows = xml_obj.find_all('item');

        result = []         # 최종 리스트
        nameList = []       # 컬럼 명

        rowsLen = len(rows);    # item의 개수
        for i in range(rowsLen) :
            item = rows[i].find_all();
            itemData = []  # 아이템의 데이터
            for j in range(len(item)) :
                if i == 0 :
                    nameList.append(item[j].name);
                text = item[j].text;
                itemData.append(text);
            result.append(itemData);

        data = pd.DataFrame(result, columns=nameList);
        data = data.astype({'clearCnt':int});
        data_li = data['clearCnt'].to_list();

        results = {
            'datas' : data_li,
            'dates' : OpenAPI().date_range()
        }

        print(results)
        return results

    def death(self):
        now = datetime.datetime.now()
        endDt = now.strftime('%Y%m%d')
        now7 = now - datetime.timedelta(days=7)
        startDt = now7.strftime('%Y%m%d')

        url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+startDt+'&endCreateDt='+endDt;
        result = requests.get(url);
        response = result.text.encode('utf-8');
        xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
        rows = xml_obj.find_all('item');

        result = []         # 최종 리스트
        nameList = []       # 컬럼 명

        rowsLen = len(rows);    # item의 개수
        for i in range(rowsLen) :
            item = rows[i].find_all();
            itemData = []  # 아이템의 데이터
            for j in range(len(item)) :
                if i == 0 :
                    nameList.append(item[j].name);
                text = item[j].text;
                itemData.append(text);
            result.append(itemData);

        data = pd.DataFrame(result, columns=nameList);
        data = data.astype({'deathCnt':int});
        data_li = data['deathCnt'].to_list();

        results = {
            'datas' : data_li,
            'dates' : OpenAPI().date_range()
        }

        print(results)
        return results


    def high(self):
        now = datetime.datetime.now()
        now1 = now.strftime('%Y%m%d')

        now2 = now - datetime.timedelta(days=1)
        now2 = now2.strftime('%Y%m%d')

        for n in [now1, now2] :
            url='http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&pageNo=1&numOfRows=10&startCreateDt='+n+'&endCreateDt='+n;
            result = requests.get(url);
            response = result.text.encode('utf-8');
            xml_obj = bs4.BeautifulSoup(response, 'lxml-xml');
            rows = xml_obj.find_all('item');

            if len(rows) != 0 :
                continue;

        item = rows[0].find_all();
        itemData = []  # 아이템의 데이터
        for j in range(len(item)) :
            text = item[j].text;
            itemData.append(text);


        # nameIndx = ['accDefRate', 'accExamCnt', 'accExamCompCnt', 'careCnt', 'clearCnt',
        #            'createDt', 'deathCnt', 'decideCnt', 'examCnt', 'resutlNegCnt', 'seq',
        #            'stateDt', 'stateTime', 'updateDt'];
        nameIndx = ['누적 확진률','누적 검사 수','누적 검사 완료 수','치료중 환자 수','격리해제 수',
                    '등록일시분초','사망자 수','확진자 수','검사진행 수','결과 음성 수','게시글번호',
                    '기준일','기준시간','수정일시분초']
        colIndx = ['','#BE3075','','#EB001F','#64A12D','','#FFED00','#000000','#008AC5','#009EE0']

        data = [];

        for i in [1,3,4,6,7,8,9] :
            data.append([nameIndx[i], int(itemData[i]), colIndx[i], nameIndx[i]])

        results = {'d1':data[0], 'd2':data[1], 'd3':data[2], 'd4':data[3], 'd5':data[4], 'd6':data[5], 'd7':data[6]}

        # results = data
        print(results)
        return results

    def vaccine(self):
        ndate = datetime.datetime.now()
        nowDate = ndate.strftime('%Y-%m-%d')
        url='https://api.odcloud.kr/api/15077756/v1/vaccine-stat?page=1&perPage=20&serviceKey=23S7ZYj%2BtnwtbEN09iKFg%2B4O9%2Fw2AtdiXKey2plFT%2BcbFUhh065aLcPqpnkgeoPfK58B11wEi25a4%2Fg1c7M98A%3D%3D&cond%5BbaseDate%3A%3AGT%5D='+nowDate;
        result = requests.get(url);
        response = result.text.encode('utf-8');

        obj = json.loads(response)

        rows = obj.get("data")
        df = pd.DataFrame(rows);

        # Index(['accumulatedFirstCnt', 'accumulatedSecondCnt', 'baseDate', 'firstCnt',
        #        'secondCnt', 'sido', 'totalFirstCnt', 'totalSecondCnt'],
        #       dtype='object')

        # print(int(df[df['sido'] == '서울특별시']['firstCnt']))
        city = ['서울특별시','부산광역시','대구광역시','인천광역시','광주광역시','울산광역시','대전광역시']
        col = ['#BE3075','#EB001F','#64A12D','#FFED00','#000000','#008AC5','#009EE0']

        first = []
        for i in range(len(city)) :
            ndf = df[df['sido'] == city[i]]
            data = [city[i], round(int(ndf['firstCnt'])/1000), col[i], city[i]]
            first.append(data)

        return first



if __name__ == '__main__' :
    OpenAPI().vaccin();