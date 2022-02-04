from flask import Flask,request, redirect, render_template
import requests
response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
app=Flask(__name__)