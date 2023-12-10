from flask import Flask, request
from injector import inject
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from persistence.database import get_db
from persistence.models import User

app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@inject
@app.route('/api/v1/user', methods=['GET'])
def get_by_id():
    db: Session = next(get_db())
    user_id = request.args.get('id', None)
    # user = db.get(User).filter(User.id == user_id).first()
    user = db.execute(text(f'select * from users where id = {user_id}'))
    return user

