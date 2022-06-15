from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#
# SE INSTANCIA APP
#

# Se crea instancia (objecto) de Flask
app = Flask(__name__)

#
# CONFIG APP
#

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5002/tienda"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#
# SE INSTANCIAN OBJECTOS
#

# Se crea instancia (objecto) de SQLAlchemy
db = SQLAlchemy(app)

# Se crea instancia (objecto) de Migrate
migrate = Migrate(app, db)

#
# IMPORT MODULES
#

from app import models
from app import routes
