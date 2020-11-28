from models.Category import Category
from models.Fine import Fine
from schemas.CategorySchema import category_schema, categories_schema
from schemas.FineSchema import fine_schema, fines_schema
from main import db
from services.auth_service import verify_user
from sqlalchemy.orm import joinedload 
from flask_jwt_extended import jwt_required, get_jwt_identity  
from flask import Blueprint, request, jsonify, abort  

categories = Blueprint("categories", __name__, url_prefix="/categories") 

@categories.route("/", methods=["GET"])                                         
def category_index():                                                           
    categories = Category.query.filter_by(private=False)                      
    return jsonify(categories_schema.dump(categories))        



@categories.route("/<int:id>", methods=["GET"])                         
def category_show(id):                                          
    category = Category.query.filter_by(id=id, private=False )  
    return jsonify(categories_schema.dump(category))    


@categories.route("/", methods=["POST"])                        
@jwt_required 
@verify_user    
def category_create(user):                                                  
    category_fields = category_schema.load(request.json)                
    new_category = Category()
    new_category.title = category_fields["title"]
    new_category.description = category_fields["description"]
    new_category.private = category_fields["private"]
    new_category.owner = user.id    
     
    user.category.append(new_category)

    db.session.commit()
    return jsonify(category_schema.dump(new_category))    


@categories.route("/<int:id>", methods=["PUT", "PATCH"])                    
@jwt_required 
@verify_user    
def category_update(user, id):                                                  
    category_fields = category_schema.load(request.json)                
    category = Category.query.filter_by(id=id, owner=user.id) 
    if not category:                                                    # If there is no profile found
        return abort(401, description="Unauthorized to update this category")
    category.update(category_fields)

    db.session.commit()
    return jsonify(category_schema.dump(category[0]))     


@categories.route("/<int:id>", methods=["DELETE"])   
@jwt_required 
@verify_user    
def category_delete(user, id):                                  
    category = Category.query.filter_by(id=id, owner=user.id).first() 

    if not category:                                                    
        return abort(400, description="Unauthorized to update this category")
        
    db.session.delete(category)
    db.session.commit()                                                # Commit the session to the db
    return jsonify(category_schema.dump(category)) 


