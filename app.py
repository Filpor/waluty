from flask import Flask,request, redirect, render_template
import requests
import csv
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data1=data[0]
rates=data1["rates"]
with open('waluty.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    csvwriter = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    csvwriter.writeheader()
    for n in rates:
        csvwriter.writerow(n)
app=Flask(__name__)