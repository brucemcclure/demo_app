from models.League import League                                       # Importing the League Model
from models.User import User                                           # Importing the User Model
from models.Member import Member
from schemas.MemberSchema import member_schema, members_schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from services.auth_service import verify_user 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

members = Blueprint("members", __name__, url_prefix="/league")         # Creating the league blueprint 



@members.route("/<int:id>/members", methods=["POST"])   
@jwt_required 
@verify_user    
def league_add_members(user, id):   
    league = League.query.filter_by(id=id, owner=user.id).first() 
    data = request.json
    for user_id in data["members"]:
        print(user_id)
        new_member = Member() 
        new_member.user_id = user_id
        new_member.league_id = id
        db.session.add(new_member) 
    db.session.commit() 

    return(f"The members were successfully added to the league")


@members.route("/<int:id>/members", methods=["delete"])   
@jwt_required 
@verify_user    
def league_remove_members(user, id):   
    league = League.query.filter_by(id=id, owner=user.id).first() 
    data = request.json
    for user_id in data["members"]:
        print(user_id)
        remove_member = Member.query.get(user_id)
        # print(remove_member)
        # db.session.delete(remove_member)
        # db.session.commit() 

    return(f"The members were successfully removed to the league")