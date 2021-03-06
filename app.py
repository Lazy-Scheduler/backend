from flask import Flask
from celery import Celery

# blueprints
from src.views.policy_render import policy
from src.views.posta import posta
from src.views.pages import pages

app = Flask(__name__)

#register blueprints
app.register_blueprint(policy)
app.register_blueprint(posta)
app.register_blueprint(pages)

@app.route('/')
def hello():
    return "Hello World!"

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)
@celery.task()
def add_together(a, b):
    return a + b

if __name__ == '__main__':
    app.run(debug=True)