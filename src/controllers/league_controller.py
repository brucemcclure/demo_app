from models.League import League                                       # Importing the League Model
from models.User import User                                           # Importing the User Model
from models.Member import Member
from models.Category import Category
from schemas.CategorySchema import category_schema
from schemas.LeagueSchema import league_schema, leagues_schema         # Importing the Profile Schema
from schemas.MemberSchema import member_schema, members_schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_user 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

leagues = Blueprint("leagues", __name__, url_prefix="/league")         # Creating the league blueprint 

@leagues.route("/", methods=["GET"])                                   # Route for the profile index
def league_index():                                                    # This function will run when the route is matched
    leagues = League.query.all()                                       # Retrieving all profiles from the db
    return jsonify(leagues_schema.dump(leagues))                       # Returning all the profiles in json 

@leagues.route("/<int:id>", methods=["GET"])                         
@jwt_required 
@verify_user    
def league_show(user, id):                                                  
    leagues = League.query.get(id)                                    
    return jsonify(league_schema.dump(leagues))                     


@leagues.route("/", methods=["POST"])                        
@jwt_required 
@verify_user    
def league_create(user):                                           
    league_fields = league_schema.load(request.json)                

    new_league = League()
    new_league.title = league_fields["title"]
    new_league.description = league_fields["description"]
    new_league.owner = user.id
    user.league.append(new_league)
    

    db.session.add(new_league)
    created_league = League.query.filter_by(owner=user.id)
    member = Member()
    member.user_id = user.id
    member.league_id = created_league[-1].id
    member.active = True
    db.session.add(member)
    db.session.commit() 

    return jsonify(league_schema.dump(new_league))     


@leagues.route("/<int:id>", methods=["PUT", "PATCH"])                    
@jwt_required 
@verify_user    
def league_update(user, id):                                                  
    league_fields = league_schema.load(request.json)                
    league = League.query.filter_by(id=id, owner=user.id) 
    if not league:                                                    # If there is no profile found
        return abort(401, description="Unauthorized to update this league")

    league.update(league_fields)

    db.session.commit()
    return jsonify(league_schema.dump(league[0]))     


@leagues.route("/<int:id>", methods=["DELETE"])   
@jwt_required 
@verify_user    
def league_delete(user, id):                                  
    league = League.query.filter_by(id=id, owner=user.id).first() 

    if not league:                                                    
        return abort(400, description="Unauthorized to update this league")
        
    db.session.delete(league)
    db.session.commit()                                                # Commit the session to the db
    return jsonify(league_schema.dump(league)) 

@leagues.route("/<int:league_id>/categories", methods=["POST"])   
@jwt_required 
@verify_user    
def add_category_to_league(user, league_id):    
    league = League.query.filter_by(id=league_id, owner=user.id).first() 
    if not league:                                                 
        return abort(400, description="Unauthorized to add categories to this league")
    
    data = request.json
    categories_already_in_league = []
    for cat in league.leagues_categories:
        categories_already_in_league.append(cat.id)


    for cat_id in data["categories"]:
        category = Category.query.filter_by(id=cat_id, private=False ).first()
        if category.private == True or (cat_id in categories_already_in_league) or (not category):
            continue
        league.leagues_categories.append(category)
        db.session.commit()                                               

    return jsonify(leagues_schema.dump(league.leagues_categories)) 


@leagues.route("/<int:league_id>/categories", methods=["DELETE"])   
@jwt_required 
@verify_user    
def remove_categories_from_league(user, league_id):    
    league = League.query.filter_by(id=league_id, owner=user.id).first() 
    if not league:                                                 
        return abort(400, description="Unauthorized to remove categories to this league")
    
    data = request.json
    categories_already_in_league = []
    for cat in league.leagues_categories:
        categories_already_in_league.append(cat.id)

    for cat_id in data["categories"]:
        category = Category.query.filter_by(id=cat_id, private=False ).first()
        if category.private == True or (not category):
            continue
        elif cat_id in categories_already_in_league:
            league.leagues_categories.remove(category)
    db.session.commit()                                               

    return jsonify(leagues_schema.dump(league.leagues_categories)) 
