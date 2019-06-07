#!/usr/bin/env python3

import json

import requests

from schema import Schema

class API:

    def __init__(self):
        self.link = "http://dev.markitondemand.com/MODApis/Api/v2/"

    def lookup(self, company_name):
        self.link += "lookup/json?input=" + company_name
        response = requests.get(self.link).text
        return json.loads(response)[0]["Symbol"]
        
    def quote(self, symbol):
        self.link += "Quote/json?symbol=" + symbol
        response = requests.get(self.link).text
        return json.loads(response)["LastPrice"]

            
if __name__ == "__main__":
    #company_name = input("company name: ")
    #print(API().lookup(company_name))    
    symbol = input("symbol: ")
    print(API().quote(symbol))
