import connexion
from flask_cors import CORS
# from prometheus_client import make_wsgi_app
# from werkzeug.middleware.dispatcher import DispatcherMiddleware
# from flask import Flask

if __name__ == '__main__':
    capp = connexion.FlaskApp(__name__, specification_dir='swagger/')
    capp.add_api('blog.yaml', arguments={'title': 'GDG Blog Assignment'})
    CORS(capp.app)
    capp.run(host='0.0.0.0', debug=True, port=666)