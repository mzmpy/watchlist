# -*- coding: utf-8 -*-

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, patch_request_class, ALL
from pypinyin import lazy_pinyin

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)
login.login_view = 'login'

allowed_files = UploadSet(extensions=ALL)
configure_uploads(app, allowed_files)
patch_request_class(app, 512 * 1024 * 1024)

from app import routes, models
