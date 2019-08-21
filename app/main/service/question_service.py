import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.question import Question


def save_new_question(data):
    new_question = Question(
        question=data['question']
    )
    save_changes(new_question)
    return generate_new_question(new_question)


def get_all_questions():
    return Question.query.all()


def get_a_question(question_id):
    return Question.query.get_or_404(question_id)


def generate_new_question(question):
    try:
        response_object = {
            'status': 'success',
            'message': 'Question Successfully registered.',
            'data': {
                'question_id': question.id,
                'question': question.question
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_question(question_id, data):
    question = Question.query.filter_by(id=question_id).first()
    if not question:
        response_object = {
            'status': 'fail',
            'message': 'question does not exist.'
        }
        return response_object, 409
    else:
        question.name = data['question']
        db.session.commit()
        return update_question(question)


def update_question(question):
    try:
        response_object = {
            'status': 'success',
            'message': 'question Details Successfully updated.',
            'data': {
                'question_id': question.id,
                'question': question.question
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_question(question_id):
    question = get_an_question(question_id)
    db.session.delete(question)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'question Successfully deleted.'
        }
        return response_object, 204
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def save_changes(data):
    db.session.add(data)
    db.session.commit()


