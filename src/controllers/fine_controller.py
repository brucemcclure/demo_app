from models.Category import Category
from models.Fine import Fine                                           # Importing the League Model
from models.User import User                                           # Importing the User Model
from schemas.FineSchema import fine_schema, fines_schema               # Importing the Profile Schema
from schemas.CategorySchema import category_schema, categories_schema
from main import db                                                    # This is the db instance created by SQLAlchemy
from main import bcrypt                                                # Import the hasing package from main
from services.auth_service import verify_user 
from sqlalchemy.orm import joinedload                                  # 
from flask_jwt_extended import jwt_required, get_jwt_identity          # Packages for authorization via JWTs
from flask import Blueprint, request, jsonify, abort                   # Import flask and various sub packages

fines = Blueprint("categories_fines", __name__, url_prefix="/categories")         

# Full crud unneseasry 

# Fines controller

@fines.route("/<int:id>/fines", methods=["GET"])                         
def category_fines_idex(id):                     
    category = Category.query.filter_by(id=id, private=False )
    if not category:
        return "Nah that shit doesnt work"
    # print(category.fine," <=====8")
    return jsonify(categories_schema.dump(category[0].fine))


@fines.route("/<int:id>/fines", methods=["POST"])       
@jwt_required 
@verify_user                      
def category_fines_create(user, id):                 
    fine_fields = fine_schema.load(request.json)      
    category = Category.query.filter_by(id=id, owner=user.id ).first()                  # Pull out a category that you own
    new_fine = Fine()
    new_fine.title = fine_fields["title"]
    new_fine.description = fine_fields["description"]
    new_fine.amount = fine_fields["amount"]
    new_fine.style = fine_fields["style"]
    new_fine.category_id = id
    category.fine.append(new_fine)
    db.session.commit()                                                
    return jsonify(fine_schema.dump(new_fine))


@fines.route("/<int:cat_id>/fines/<int:fine_id>", methods=["PATCH", "PUT"])       
@jwt_required 
@verify_user                      
def category_fines_update(user, cat_id, fine_id):
    owned_cats = []
    for i in user.category:
        owned_cats.append(i.id)
    
    if cat_id not in owned_cats:
        abort(401, description="Unauthorized to update fines in this category")    

    fine_fields = fine_schema.load(request.json)      

    fine = Fine.query.filter_by(id=fine_id,  category_id=cat_id  )
    if not fine:                                                    
        return abort(404, description="This fone does not exist")

    fine.update(fine_fields)

    db.session.commit()                                                
    return jsonify(fines_schema.dump(fine))

@fines.route("/<int:cat_id>/fines/<int:fine_id>", methods=["DELETE"])       
@jwt_required 
@verify_user                      
def category_fines_delete(user, cat_id, fine_id):
    category = Category.query.filter_by(id=cat_id, owner=user.id).first() 
    fines_in_cat = category.fine 
    for fine in fines_in_cat:
        if fine.id == fine_id:
            db.session.delete(fine)

    db.session.commit()                                                
    return jsonify(fine_schema.dump(fine))
