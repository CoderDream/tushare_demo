#!/usr/bin/python  
# coding: UTF-8  
  
"""This script parse stock info"""  
  
import tushare as ts  
  
def get_all_price(STOCK):  
    '''''process all stock'''  
    df = ts.get_realtime_quotes(STOCK)  
    df.tail(10)
    print(df)
    
def get_history_data(STOCK):  
    '''''process all stock'''  
    df = ts.get_hist_data(STOCK)  
    print(df)
    
def get_history_data_1():
    #df = ts.get_hist_data('600848')
    ts.get_hist_data('600848',ktype='W') #获取周k线数据
    ts.get_hist_data('600848',ktype='M') #获取月k线数据
    ts.get_hist_data('600848',ktype='5') #获取5分钟k线数据
    ts.get_hist_data('600848',ktype='15') #获取15分钟k线数据
    ts.get_hist_data('600848',ktype='30') #获取30分钟k线数据
    ts.get_hist_data('600848',ktype='60') #获取60分钟k线数据
    ts.get_hist_data('sh')#获取上证指数k线数据,其它参数与个股一致,下同
    ts.get_hist_data('sz')#获取深圳成指k线数据 ts.get_hist_data('hs300')#获取沪深300指数k线数据
    ts.get_hist_data('sz50')#获取上证50指数k线数据
    ts.get_hist_data('zxb')#获取中小板指数k线数据
    ts.get_hist_data('cyb')#获取创业板指数k线数据  
  
if __name__ == '__main__':  
    STOCK = ['600219',       ##南山铝业  
             '000002',       ##万  科Ａ  
             '000623',       ##吉林敖东  
             '000725',       ##京东方Ａ  
             '600036',       ##招商银行  
             '601166',       ##兴业银行  
             '600298',       ##安琪酵母  
             '600881',       ##亚泰集团  
             '002582',       ##好想你  
             '600750',       ##江中药业  
             '601088',       ##中国神华  
             '000338',       ##潍柴动力  
             '000895',       ##双汇发展  
             '000792']       ##盐湖股份  
  
    #get_all_price(STOCK)  
    #get_history_data()
    
    # ts.get_hist_data('600848',ktype='W') 
    #get_history_data(STOCK) #一次性获取全部数据
    
    #ts.get_stock_basics()
    #ts.get_industry_classified()
    ts.get_hist_data('600848')