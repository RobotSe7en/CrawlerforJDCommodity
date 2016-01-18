'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=

from bs4 import BeautifulSoup
import re,urllib
from builtins import str
import json


class htmlParser(object):
    
    
    def getNewUrl(self, pageUrl, soup):
        newUrls = set()
        
        # /list.html?cat=9987%2C653%2C655&page=2&JL=6_0_0
        links = soup.find_all('a', class_='pn-next',href=re.compile(r"/list.html\?cat=9987%2C653%2C655&page=\d+\&JL=6_0_0"))
        # print(links)
        for link in links:
            newUrl = link['href']
            newFullUrl = urllib.parse.urljoin(pageUrl,newUrl)
            newUrls.add(newFullUrl)
        return newUrls
        
    
    
    def getNewData(self, pageUrl, soup):
        resData = {}
        
        count = 1
        while True:
            try:
                # print(soup.find('div',index=str(count)).find('div',class_='p-name').find('a',target='_blank').find('em'))
                # <a target="_blank" href="http://item.jd.com/1413073.html" title="真的好一点！5.5英寸FHD大屏幕，双卡双待千元机！2GB+16GB大容量！K3 note超多好评选择不犹豫！【更多暖心定制礼包】">
                # <em>联想 乐檬 K3 Note（K50-t3s） 16G 珍珠白 移动4G手机 双卡双待</em>
                # <i class="promo-words">真的好一点！5.5英寸FHD大屏幕，双卡双待千元机！2GB+16GB大容量！K3 note超多好评选择不犹豫！【更多暖心定制礼包】</i>
                # </a>
                commodityName = soup.find('div',index=str(count)).find('div',class_='p-name').find('a',target='_blank').find('em')
                resData['Name'+str(count)] = commodityName.get_text()
                
                # <strong class="J_price"><em>¥</em><i>499.00</i></strong>
                commoditySku = soup.find('div',index=str(count)).get('data-sku')
                temp = urllib.request.urlopen('http://p.3.cn/prices/get?skuid=J_'+commoditySku)
                soup1 = BeautifulSoup(temp.read(),'lxml',from_encoding='utf-8')
                soup1.find('p')
                commodityPrice = json.loads(soup1.find('p').get_text())
                resData['Price'+str(count)] = commodityPrice[0]['p']
                count = count + 1
            except:
                return resData
            
        return resData
    
    
    def parse(self,pageUrl,pageCont):
        if pageUrl is None or pageCont is None:
            return
        soup = BeautifulSoup(pageCont,'lxml',from_encoding='utf-8')
        newUrl = self.getNewUrl(pageUrl,soup)
        newData = self.getNewData(pageUrl,soup)
        return newUrl,newData
        
    
    



