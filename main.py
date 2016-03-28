from flask import Flask
from flask import render_template
from flask.json import dumps

from bs4 import BeautifulSoup

import requests

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/ponto')
def login():
    s = requests.Session()
    r = s.post('http://intranet.ivia.com.br', data = {'txtUser': 'rafael.borges', 'txtPass': 'BObo220310', 'imageField': 'Login', 'imageField.x': '14', 'imageField.y': '32'})
    # print(dir(r.cookies.__dict__.get("_cookies")))
    print(s.cookies.get_dict())
    r2 = s.get('http://intranet.ivia.com.br/transfer.asp?targ=ponto', cookies=s.cookies.get_dict())
    #r2 = requests.get('http://intranet.ivia.com.br/intranet.asp')
    # import cgi
    # return cgi.escape(r2.text)
    # return r2.text

    soup = BeautifulSoup(r2.text)

    fields = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE':'',
        '__EVENTVALIDATION': '',
        'CodeNumberTextBox': '',
        'btnPonto': '',
        'hdfLastTime': '',
        'hdfTotalTime': '',
        'hdfActivitiesCount': 0,
        'txtHour': '',
        'txtDescription': '',
        'hdfDataEscolhida': '',
    }

    attrs = {'name': '__EVENTTARGET'}

    for item in fields.items():
        input = soup.find('input', {'name': item[0]})
        if input:
            fields.update({item[0]: input.get('value')})

    r3 = s.post('http://intranet.ivia.com.br/intranetApp/Ponto/Index.aspx', data=fields, cookies=s.cookies.get_dict())
    # import pdb; pdb.set_trace()
    # return dumps(s.cookies.get_dict())
    #return dumps(r.cookies.__dict__.get("_cookies").__dict__)
    # return 'ok'
    return r3.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



