import os
import json
import requests
from flask import Blueprint, Response


posta = Blueprint('posta', __name__)

def load_data():
    with open('data/data.json') as data_file:
        return json.load(data_file)


@posta.route('/posta', methods=['POST'])
def post_to_facebook():
    '''
    Post to Facebook

    Send a POST request to the /{group-id}/feed endpoint to post a message to a Group.
    curl -i -X POST \ 
    "https://graph.facebook.com/{group-id}/feed"

    Sample response

    {
    "id": "1015396500240109_1015396500240110",
    "from": {
        "name": "Heather",
        "id": "268045640633085"
        },
    "message": "Hello World!",
    "created_time": "2015-05-22T19:29:30+0000"
    }
    '''
    group_id = os.environ.get('FACEBOOK_POSTA_GROUP_ID')
    long_term_access_token = os.environ.get('FACEBOOK_POSTA_LONG_TERM_ACCESS_TOKEN')

    # return Response(long_term_access_token)
    long_term_access_token = os.environ.get('FACEBOOK_POSTA_LONG_TERM_ACCESS_TOKEN')
    data = load_data()
    for item in data:
        message = item['message']
        

        url = 'https://graph.facebook.com/{}/feed'.format(group_id)
        res = requests.post(url, params={
            'access_token': long_term_access_token
        }, data={
            'message': message
        })
        return res.json()