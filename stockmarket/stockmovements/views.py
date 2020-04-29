from django.shortcuts import render
from django.http import response
from .sharenews import today_price


def share_market_view(requests,*args,**kwargs):
    object=today_price("today")
    stockhead=object.stock_headlines()
    stockdetails=object.stock_movements()
    data={
        'stock_header': stockhead,
        'stock_details': stockdetails
    }
    return render(requests,'index.html',data)

def main_view(requests,*args,**kwargs):
    content={}
    return render(requests,'base.html', content)




