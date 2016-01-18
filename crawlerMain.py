'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=

from CrawlerforJDPhone import urlManager, htmlDownloader, \
    crawlerOutputer
from CrawlerforJDPhone import htmlParser


class crawlerMain(object):
    def __init__(self):
        self.urls = urlManager.urlManager()
        self.downloader = htmlDownloader.htmlDownloader()
        self.parser = htmlParser.htmlParser()
        self.outputer = crawlerOutputer.crawlerOutput()
    
    def craw(self, rootUrl):
        count = 1
        self.urls.addNewUrl(rootUrl)
        while self.urls.hasNewUrl():
            try:
                newUrl = self.urls.getNewUrl()
                print("craw %d : %s" % (count,newUrl))
                htmlCont = self.downloader.download(newUrl)
                newUrls, newData = self.parser.parse(newUrl, htmlCont)
                self.urls.addNewUrls(newUrls)
                self.outputer.collectData(newData)
                
                if count == 1000:
                    break
                
                count = count + 1
            except:
                print("Craw fialed!")
        self.outputer.outPutHtml()
    
    



if __name__ =="__main__":
    rootUrl = "http://list.jd.com/list.html?cat=9987,653,655"
    
    objCrawler = crawlerMain()
    
    objCrawler.craw(rootUrl)
else:
    print("2")