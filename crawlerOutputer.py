'''
Created on 2016年1月17日

@author: wangpeng
'''
#coding=utf8=
import xlrd

class crawlerOutput(object):
    
    def __init__(self):
        self.datas = []
        
    def collectData(self,data):
        if data is None:
            return
        self.datas.append(data)

    
    def outPutHtml(self):
        fout = open('outPutofJDPhone.txt','w',encoding='UTF-8')
        # print(self.datas)
        for data in self.datas:
            for i in range(1,int(len(data)/2+1)):
                # print(data['Name'+str(i)],data['Price'+str(i)])
                fout.writelines(data['Name'+str(i)]+'---->')
                fout.writelines(data['Price'+str(i)]+'\n')
        fout.close()
    
    
    
    



