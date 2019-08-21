import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model._category import ICategory


def save_new_category(data):
    category = ICategory.query.filter_by(category_name=data['category_name']).first()
    if not category:
        new_category = ICategory(
            category_name=data['category_name'],
            category_status=data['category_status']
        )
        save_changes(new_category)
        return generate_new_category(new_category)
    else:
        response_object = {
            'status': 'fail',
            'message': 'Category already exists.'
        }
        return response_object, 409


def get_all_categories():
    return ICategory.query.order_by(ICategory.id.desc()).all()


def get_a_category(category_id):
    return ICategory.query.get_or_404(category_id)


def generate_new_category(category):
    try:
        response_object = {
            'status': 'success',
            'message': 'Category Successfully registered.',
            'data': {
                'category_name': category.category_name,
                'category_status': category.category_status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_category(category_id, data):
    category = ICategory.query.filter_by(id=category_id).first()
    if not category:
        response_object = {
            'status': 'fail',
            'message': 'Category does not exist.'
        }
        return response_object, 409
    else:
        category.category_name = data['category_name'],
        category.category_status = data['category_status'],
        db.session.commit()
        return update_category(category)


def update_category(category):
    try:
        response_object = {
            'status': 'success',
            'message': 'Category Details Successfully updated.',
            'data': {
                'category_name': category.category_name,
                'category_status': category.category_status
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_category(category_id):
    category = get_a_category(category_id)
    db.session.delete(category)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'Category Successfully deleted.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()


