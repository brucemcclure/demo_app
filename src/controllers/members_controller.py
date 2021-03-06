from models.League import League                                       
from models.User import User                                          
from models.Member import Member
from schemas.MemberSchema import member_schema, members_schema
from main import db                                                    
from services.auth_service import verify_user 
from flask_jwt_extended import jwt_required, get_jwt_identity         
from flask import Blueprint, request, jsonify, abort                   

members = Blueprint("members", __name__, url_prefix="/league")         



@members.route("/<int:id>/members", methods=["POST"])   
@jwt_required 
@verify_user    
def league_add_members(user, id):   
    league = League.query.filter_by(id=id, owner=user.id).first() 
    if not league:                                                    
        return abort(401, description="Unauthorized to add members to this league")
    data = request.json
    for user_id in data["members"]:
        new_member = Member() 
        new_member.user_id = user_id
        new_member.league_id = id
        new_member.active = True
        member_already_exists = Member.query.filter_by(user_id = new_member.user_id, league_id = new_member.league_id ).first()
        if not member_already_exists:
            db.session.add(new_member) 
        else:
            continue
    db.session.commit() 

    return(f"The members were successfully added to the league")


@members.route("/<int:id>/members", methods=["DELETE"])   
@jwt_required 
@verify_user    
def league_remove_members(user, id):   
    league = League.query.filter_by(id=id, owner=user.id).first() 
    if not league:                                                    
        return abort(401, description="Unauthorized to remove members from this league")

    # if league.owner == user.id:
    #     return abort(401, description="The owner of the league cannot be deactivated")

    data = request.json
    for user_id in data["members"]:
        member = Member.query.filter_by(user_id=user_id, league_id=league.id).first() 
        if not member:
            continue
        member.active = False
        db.session.commit() 
    return "pickles"

@members.route("/<int:league_id>/members", methods=["PATCH", "PUT"])   
@jwt_required 
@verify_user    
def reactivate_member(user, league_id):   
    member = Member.query.filter_by(user_id=user.id, league_id=league_id).first()
    if member.active == True:
        member.active = False
    else:
        member.active = True
    db.session.commit() 
    return jsonify(member_schema.dump(member))
