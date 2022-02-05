from flask import Flask, request, render_template
import requests
import csv
#Pobieranie API i wyciąganie z niego tabeli Rates
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
data1=data[0]
rates=data1["rates"]
#Utworzenie i zapisanie kursów walut w pliku CSV
with open('waluty.csv', 'w', encoding='utf-8') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    csvwriter = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    csvwriter.writeheader()
    for n in rates:
        csvwriter.writerow(n)
#Wyciąganie danych z listy słowników
dolar=rates[0]
dolar_austalijski=rates[1]
dolar_kanadyjski=rates[2]
euro=rates[3]
forint=rates[4]
frank=rates[5]
funt=rates[6]
jen=rates[7]
korona_czeska=rates[8]
korona_dunska=rates[9]
korona_norweska=rates[10]
korona_szwedzka=rates[11]
sdr=rates[12]

app=Flask(__name__)
@app.route('/waluty', methods=['GET',"POST"])
def waluty():
    if request.method=='GET':
        return render_template("waluty.html")
    elif request.method=='POST':
        #Pobieranie danych z formularza
        waluta=request.form['waluty']
        ilosc=float(request.form['ilosc'])
        #Tworzenie warunków dla każdej z walut
        if waluta=='USD':
            wartosc=ilosc/dolar.get('ask')
            return f'Wartość w USD: {wartosc}'

        elif waluta=='AUD':
            wartosc=ilosc/dolar_austalijski.get('ask')
            return f'Wartość w AUD: {wartosc}'

        elif waluta=="CAD":
            wartosc=ilosc/dolar_kanadyjski.get('ask')
            return f'Wartość w CAD: {wartosc}'

        elif waluta=='EUR':
            wartosc=ilosc/euro.get('ask')
            return f'Wartość w EUR: {wartosc}'

        elif waluta=='HUF':
            wartosc=ilosc/forint.get("ask")
            return f'Wartość w HUF: {wartosc}'

        elif waluta=='CHF':
            wartosc=ilosc/frank.get('ask')
            return f'Wartość w CHF: {wartosc}'

        elif waluta=='GBP':
            wartosc=ilosc/funt.get("ask")
            return f'Wartość w GBP: {wartosc}'
        
        elif waluta=="JPY":
            wartosc=ilosc/jen.get('ask')
            return f"Wartość w JPY: {wartosc}"
        
        elif waluta=="CZK":
            wartosc=ilosc/korona_czeska.get('ask')
            return f'Wartość w CZK: {wartosc}'
        
        elif waluta=="DKK":
            wartosc=ilosc/korona_dunska.get('ask')
            return f'Wartość w DKK: {wartosc}'

        elif waluta=='NOK':
            wartosc=ilosc/korona_norweska.get('ask')
            return f"Wartość w NOK: {wartosc}"

        elif waluta=="SEK":
            wartosc=ilosc/korona_szwedzka.get('ask')
            return f'Wartość w SEK: {wartosc}'

        elif waluta=='SDR':
            wartosc=ilosc/sdr.get('ask')
            return f'Wartość w XDR: {wartosc}'

    return render_template("waluty.html")