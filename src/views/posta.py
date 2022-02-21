from flask import Blueprint,request

posta = Blueprint('posta', __name__)

f = open('data/data.json')

data = json.load(f)

for i in data['emp_details']:
    print(i)
 
# Closing file
f.close()