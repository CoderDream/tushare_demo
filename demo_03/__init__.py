# CrawBaiduStocksA.py
import requests
from bs4 import BeautifulSoup
import traceback
import re
 
# 获取页面的公共方法
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "get fail"

# 获取股票代码列表
def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser') 
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])           
        except:
            continue
 
# 获取个股信息并输出到文件中
def getStockInfo(lst, stockURL, fpath):
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class':'stock-bets'})
            if stockInfo:
                name = stockInfo.find_all(attrs={'class':'bets-name'})[0]
                infoDict.update({'股票名称': name.text.split()[0]})
            else:
                print('stockInfo is null')
                break
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val
             
            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
        except:
            traceback.print_exc()
            continue
 
def main():
    print('Hello world!')
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'  # 东放财富股票列表
    stock_info_url = 'https://gupiao.baidu.com/stock/'  # 百度股票信息
    output_file = 'D:/BaiduStockInfo.txt'  # 结果存储的文件
    slist = []
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)
 
if __name__ == '__main__':
    main()
