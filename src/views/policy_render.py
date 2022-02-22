from flask import Blueprint,render_template

policy = Blueprint('policy', __name__)

@policy.route('/data_deletion', methods=['GET'])
def data_deletion():
    return render_template('/src/templates/data_deletion.html')

@policy.route('/privacy_policy', methods=['GET'])
def privacy_policy():
    return render_template('/src/templates/privacy_policy.html')

@policy.route('/terms_of_use', methods=['GET'])
def terms_of_use():
    return render_template('/src/templates/terms_service.html')