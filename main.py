from flask import Flask, json, request, jsonify
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "SuperSecretPwd"
}

@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password

app = Flask(__name__)

@app.route('/api/cashback', methods = ['POST'])
@auth.login_required
def hello_world():
    print (request.is_json)
    content = request.get_json()
    soldat = content['sold_at']
    customer_doc = content['customer']['document']
    customer_name = content['customer']['name']
    total_price = content['total']
    print(f'Sold at: {soldat} ;\nCustomer Name: {customer_name} ;\nCustomer Doc: {customer_doc} ;\nTotal Price: {total_price} ')
    return 'JSON posted'

if __name__ == '__main__':
    print('Starting app')
    app.run(host='0.0.0.0', debug=True, port=8080)
    