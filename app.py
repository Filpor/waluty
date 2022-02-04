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
dolar=rates[0]
dolar_austalijski=rates[1]
dolar_kanadyjski=rates[2]


app=Flask(__name__)
@app.route('/waluty', methods=['GET',"POST"])
def waluty():
    if request.method=='GET':
        return render_template("waluty.html")
    elif request.method=='POST':
        waluta=request.form['waluty']
        ilosc=float(request.form['ilosc'])
        if waluta=='USD':
            wartosc=ilosc/dolar.get('ask')
            wartosc=str(wartosc)
            print(wartosc)
            return f'Wartość w USD: {wartosc}'
        elif waluta=='AUD':
            wartosc=ilosc/dolar_austalijski.get('ask')
            return f'Wartość w AUD: {wartosc}'
        elif waluta=='CAD':

    return render_template("waluty.html")