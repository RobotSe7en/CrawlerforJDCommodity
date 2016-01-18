'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=

import urllib.request


class htmlDownloader(object):
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
        
    
