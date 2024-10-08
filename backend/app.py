from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from flask_migrate import Migrate
import os

from apis import api
from core.database import db

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://' + DB_USER + ':' + DB_PASSWORD +  '@' + DB_HOST + ':5432/' + DB_NAME
app.config['ERROR_404_HELP'] = False
api.init_app(app)
db.init_app(app)

# Migracion con Flask-Migrate (Alembic)
migrate = Migrate(app, db)
# flask db init
# flask db migrate -m "Initial migration"
# flask db upgrade
# flask db downgrade
# flask db --help

if __name__ == '__main__':
    app.run(debug=True)