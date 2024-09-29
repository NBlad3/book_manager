from app.models import User
from flask import request, jsonify
from app import app, db

@app.route("/register", methods = ["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = data["password"]

    username_exists = User.query.filter_by(username = username).first()
    if username_exists:
        return jsonify({"message": "Username already exists"}), 400

    new_user = User(username = username, password = password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registered successfully"}), 200
