from flask import Flask
from flask_restx import Api
from apis import api
from core.database import db
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://' + DB_USER + ':' + DB_PASSWORD +  '@' + DB_HOST + ':5432/' + DB_NAME
api.init_app(app)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)