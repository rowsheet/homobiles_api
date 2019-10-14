from flask import Flask, request, render_template, jsonify
import emailer
import json
import os
import requests
import base64
import wtforms as forms
from wtforms import validators
from flask_bootstrap import Bootstrap
app = Flask(__name__,template_folder="templates")
Bootstrap(app)

class ChargesForm(forms.Form):
    amount = forms.FloatField(
        "Amount", [
            validators.InputRequired(),
            validators.NumberRange(min=0.01,max=9999.99),
        ]
    )
    currency = forms.SelectField(
        "Currency",
        choices = [
            ("usd","USD"),
            ("aed","AED"),
            ("all","ALL"),
            ("amd","AMD"),
            ("ang","ANG"),
        ]
    )
    source = forms.StringField(
        "Source", [
        validators.AnyOf(["tok_amex","tok_mastercard","tok_visa"]),
        ]
    )
    description = forms.StringField(
        "Description", [
        validators.InputRequired(),
        validators.Length(max=100),
        ]
    )

class Charge:
    def __init__(self, amount, currency, source, description):
        self.amount = amount
        self.currency = currency
        self.source = source
        self.description = description

def authenticate(request):
    print(request.authorization.username)
    print(request.authorization.password)

@app.route("/v1/charges", methods=["GET", "POST"])
def v1_charges():
    print(request.method)
    form = ChargesForm(request.form)
    if request.method == "POST":
        if form.validate():
            charge = Charge(
                form.amount.data,
                form.currency.data,
                form.source.data,
                form.description.data)
            return json.dumps({"foo": "bar"})
        else:
            return json.dumps(form.errors), 400
    else:
        return render_template('register.html', form=form, url=request.url)

@app.route('/ping', methods=['POST', 'GET'])
def ping():
        print("got ping")
        return "pong"

if __name__ == '__main__':
        app.run(
                host= '0.0.0.0',
                port=5201,
                debug=True
        )
