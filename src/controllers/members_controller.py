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
    data = request.json
    for user_id in data["members"]:
        print(user_id)
        new_member = Member() 
        new_member.user_id = user_id
        new_member.league_id = id
        new_member.active = True
        db.session.add(new_member) 
    db.session.commit() 

    return(f"The members were successfully added to the league")


@members.route("/<int:id>/members", methods=["delete"])   
@jwt_required 
@verify_user    
def league_remove_members(user, id):   
    # check if 
    # league = League.query.filter_by(id=id, owner=user.id).first() 
    # data = request.json
    # for user_id in data["members"]:
    #     print(user_id)
#         remove_member = Member.query.get(user_id)
#         # print(remove_member)
#         # db.session.delete(remove_member)
#         # db.session.commit() 
    return "pickles"
#     return(f"The members were successfully removed to the league")