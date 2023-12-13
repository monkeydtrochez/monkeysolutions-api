import os
from flask import Flask, jsonify, request
from persistence.database import SQLALCHEMY_DATABASE_URL, initialize_db

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db, ma = initialize_db(app)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    linked_in = db.Column(db.String, nullable=False)
    github = db.Column(db.String, nullable=False)

    def __init__(self, first_name, last_name, role, phone_number, email, linked_in, github):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.phone_number = phone_number
        self.email = email
        self.linked_in = linked_in
        self.github = github


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


user_schema = UserSchema()
users_schema = UserSchema(many=True)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world from Monkey Solutions!'


# Get user by id
@app.route('/api/v1/user', methods=['GET'])
def get_users():
    user_id = request.args.get('id', int)
    user = User.query.filter(User.id == user_id)
    result = users_schema.dump(user)
    return jsonify(result)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)

