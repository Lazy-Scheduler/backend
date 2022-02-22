from flask import Blueprint,render_template

policy = Blueprint('policy', __name__)

@policy.route('/data_deletion', methods=['GET'])
def data_deletion():
    return 'data_deletion'
    
@policy.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return 'funtimes'

@policy.route('/terms_of_use', methods=['GET'])
def terms_of_use():
    return 'funtimes'