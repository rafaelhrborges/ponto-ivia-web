from flask import Flask
from flask import render_template
from flask.json import dumps

import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/ponto')
def login():
    r = requests.post('http://intranet.ivia.com.br', data = {'txtUser': 'rafael.borges', 'txtPass': 'BObo220310', 'imageField': 'Login', 'imageField.x': '14', 'imageField.y': '32'})
    print(dir(r.cookies.__dict__.get("_cookies")))
    #r2 = requests.get('http://intranet.ivia.com.br/transfer.asp?targ=ponto')
    #r2 = requests.get('http://intranet.ivia.com.br/intranet.asp')
    #import cgi
    #return cgi.escape(r2.text)
    #return dumps(r.cookies.__dict__)
    #return dumps(r.cookies.__dict__.get("_cookies").__dict__)
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



