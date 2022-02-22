import os
import json
import requests
from flask import Blueprint, Response

pages = Blueprint('pages', __name__)

admin_user_id = os.environ.get('FACEBOOK_PAGES_ADMIN_USER_ID')
admin_user_token = os.environ.get('FACEBOOK_PAGES_ADMIN_USER_TOKEN')

def load_data():
    with open('data/data.json') as data_file:
        return json.load(data_file)

@pages.route('/page_info', methods=['GET'])
def get_page_id():
    url = 'https://graph.facebook.com/{}/accounts?access_token={}'.format(admin_user_id, admin_user_token)
    res = requests.get(url)
    return res.json()['data'][0]['access_token'], res.json()['data'][0]['id']

@pages.route('/pages', methods=['GET'])
def post_to_page():
    '''
    Post to Facebook

    https://graph.facebook.com/{page-id}/feed
    ?message=Hello Fans!
    &access_token={page-access-token}"
    
    '''
    responses = []
    page_access_token, page_id = get_page_id()
    data = load_data()
    for item in data:
        url = 'https://graph.facebook.com/{}/feed'.format(page_id)
        res = requests.post(url, params={
            'message': item['message'],
            'access_token': page_access_token
        })
        responses.append(res.json())
    return Response(json.dumps(responses))




