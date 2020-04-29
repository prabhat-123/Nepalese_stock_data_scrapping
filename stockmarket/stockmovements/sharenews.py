from bs4 import BeautifulSoup
import requests


class today_price():
    def __init__(self,day):
        self.day=day

    def parser_url(self):
        self.url="https://www.sharebazarnepal.com.np/share-watch/"+self.day+"-s-market-price.html"
        self.response=requests.get(self.url)
        self.soup=BeautifulSoup(self.response.content,'html.parser')
        self.table_data=self.soup.find_all(class_="table table-hover table-striped")
        
        
       

    def stock_headlines(self):
        self.parser_url()
        for items in self.table_data:
            self.tab_data=items.find_all('tr')
        self.header_location =self.tab_data[0]
        self.table_head=self.header_location.find_all('th')
        self.header_list=[]
        for items in self.table_head:
            self.req_header=items.text
            self.header_list.append(self.req_header)
        return self.header_list
        

    def stock_movements(self):
        self.parser_url()
        self.stock_headlines()
        self.data_list=[]
        for value in self.tab_data[1:167]:
            self.table_data=value.find_all('td')
            for data in self.table_data:
                self.req_data=data.text
                self.data_list.append(self.req_data)
            self.length=len(self.data_list)
            self.data_listoflist=[]
            for var in range(0,self.length-9,10):
                self.data_listoflist.append(self.data_list[var:var+10])
        return self.data_listoflist


        


'''
for items in table_data:
        tab_data=items.find_all('tr')
header_list=[]
data_list=[]
header_location=tab_data[0]
table_head=header_location.find_all('th')
for items in table_head:
        req_header=items.text
        header_list.append(req_header)
print(header_list)
for items in tab_data[1:167]:
        table_data=items.find_all('td')
        for value in table_data:
                req_data=value.text
                data_list.append(req_data)
print(data_list)
'''