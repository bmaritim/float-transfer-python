import uuid
import datetime
from flask import json, jsonify, request
from app.main import db
from app.main.model.answer import Answer
from app.main.service.question_service import *


def save_new_answer(data):
    new_answer = Answer(
        answer=data['answer'],
        question_id=data['question_id']
    )
    save_changes(new_answer)
    return generate_new_answer(new_answer)


def get_all_answers():
    return Answer.query.all()


def get_an_answer(answer_id):
    return Answer.query.get_or_404(answer_id)


def generate_new_answer(answer):
    try:
        response_object = {
            'status': 'success',
            'message': 'answer Successfully registered.',
            'data': {
                'answer_id': answer.id,
                'answer': answer.answer,
                'question_id': answer.question_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_answer(answer_id, data):
    answer = Answer.query.filter_by(id=answer_id).first()
    if not answer:
        response_object = {
            'status': 'fail',
            'message': 'answer does not exist.'
        }
        return response_object, 409
    else:
        answer.name = data['answer']
        db.session.commit()
        return update_answer(answer)


def update_answer(answer):
    try:
        response_object = {
            'status': 'success',
            'message': 'answer Details Successfully updated.',
            'data': {
                'answer_id': answer.id,
                'answer': answer.answer,
                'question_id': answer.question_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_answer(answer_id):
    answer = get_an_answer(answer_id)
    db.session.delete(answer)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'answer Successfully deleted.'
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


