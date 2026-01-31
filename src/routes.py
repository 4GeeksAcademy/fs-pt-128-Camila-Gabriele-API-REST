from flask import Blueprint, jsonify, request
from models import User, db, Character, Location

api = Blueprint("api" , __name__)

@api.route("/users",methods=["GET"])
def get_users():
    users = User.query.all()
    response = [user.serialize()for user in users]
    print(users)
    return jsonify(response), 200

@api.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 400
    return jsonify(user.serialize()), 200


@api.route("/character", methods=["GET"])
def get_characters():
    characters = Character.query.all()
    response = [character.serialize()for character in characters]
    print(characters)
    return jsonify(response), 200


@api.route("/character/<int:character_id>", methods=["GET"])
def get_character(character_id):
    character = Character.query.all(character_id)
    if not character:
        return jsonify({"error": "Character not found"}), 400
    return jsonify(character.serialize()), 200


@api.route("/location", methods=["GET"])
def get_locations():
    locations = Location.query.all()
    response = [location.serialize()for location in locations]
    print(locations)
    return jsonify(response), 200


@api.route("/location/<int:location_id>", methods=["GET"])
def get_location(location_id):
    location = Character.query.all(location_id)
    if not location:
        return jsonify({"error": "Location not found"}), 400
    return jsonify(location.serialize()), 200
    
@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data.get("name") or not data.get("last_name"):
        return jsonify({"error": "Name and Last Name are required"}), 400
    new_user = User (
        name=data["name"],
        last_name=data["last_name"]
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()), 201



