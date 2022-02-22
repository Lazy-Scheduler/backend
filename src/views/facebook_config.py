import os
import json
import requests
from flask import Blueprint
from app import app

facebook_graph_api_version=os.environ.get('FACEBOOK_GRAPH_API_VERSION')
facebook_posta_app_id=os.environ.get('FACEBOOK_POSTA_APP_ID')
facebook_posta_app_secret=os.environ.get('FACEBOOK_POSTA_APP_SECRET')

def generate_user_access_token():
    '''
    Generate access token that lasts for 60 seconds

    You will need the following:

    A valid User Access Token
    Your App ID
    Your App Secret

    Query the

    curl -X GET "https://graph.facebook.com/oauth/access_token
    ?client_id={your-app-id}
    &client_secret={your-app-secret}
    &grant_type=client_credentials"
    '''
    url = 'https://graph.facebook.com/oauth/access_token'
    res = requests.get(url, params={
        'client_id': os.environ.get('FACEBOOK_POSTA_APP_ID'),
        'client_secret': os.environ.get('FACEBOOK_POSTA_APP_SECRET'),
        'grant_type': 'client_credentials'
    })
    app.config['FACEBOOK_POSTA_ACCESS_TOKEN'] = generate_user_access_token()
    return res.json()['access_token']

def generate_long_term_access_token():
    '''
    Generate access token that lasts for 60 days

    If you need a long-lived User access token you can generate one from a short-lived User access token. 
    A long-lived token generally lasts about 60 days.

    You will need the following:

    A valid User Access Token
    Your App ID
    Your App Secret


    Query the GET oauth/access_token endpoint.

    curl -i -X GET "https://graph.facebook.com/{graph-api-version}/oauth/access_token?  
    grant_type=fb_exchange_token&          
    client_id={app-id}&
    client_secret={app-secret}&
    fb_exchange_token={your-access-token}" 

    Sample Response

    {
    "access_token":"{long-lived-user-access-token}",
    "token_type": "bearer",
    "expires_in": 5183944            //The number of seconds until the token expires
    }
    '''
    facebook_posta_access_token = os.environ.get('FACEBOOK_POSTA_ACCESS_TOKEN')

    url = 'https://graph.facebook.com/{graph-api-version}/oauth/access_token?'.format(graph_api_version=facebook_graph_api_version)
    
    res = requests.get(url, params={
        'grant_type': 'fb_exchange_token',
        'client_id': facebook_posta_app_id,
        'client_secret': facebook_posta_app_secret,
        'fb_exchange_token': facebook_posta_access_token
    })
    app.config['FACEBOOK_POSTA_LONG_TERM_ACCESS_TOKEN'] = generate_long_term_access_token()
    return res.json()['access_token']

def get_group_id():
    '''
    Get the group id of the group you want to post to.
    
    Send a GET request to the /{user-id}/groups endpoint to get a list of Groups for which a User who has granted your app permission to do so.
    curl -i -X GET \ 
    "https://graph.facebook.com/{user-id}/groups"

    Sample response

            {
        "data": [
            {
            "name": "Heather's Tupperware",
            "id": "871704662996313"
            },
            {
            "name": "Team Loomer",
            "id": "244471929349963"
            },
            {
            "name": "Wild Horses",
            "id": "146797922030397"
            },
        ],
        "id": "268045640633085"
        }
    '''
    url = 'https://graph.facebook.com/{user-id}/groups'.format(user_id=os.environ.get('FACEBOOK_USER_ID'))
    res = requests.get(url, params={
        'access_token': os.environ['FACEBOOK_POSTA_LONG_TERM_ACCESS_TOKEN']
    })
    print(res.json())
    # app.config['FACEBOOK_GROUP_ID'] = res.json()['data'][0]['id']
    return res.json()



def regenerate_tokens():
    '''
    Background task to check if tokens are up to date

    
    
    '''
    pass