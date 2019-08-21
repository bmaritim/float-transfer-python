import uuid
import datetime
from flask import json, jsonify, request
from sqlalchemy import extract
from datetime import datetime
from app.main import db
from app.main.model.user_answer import UserAnswer
from app.main.model.mf import Mf
from app.main.model.officer import Officer


def save_new_user_answer(data):
    new_user_answer = UserAnswer(
        answer=data['answer'],
        question_id=data['question_id'],
        mf_id=data['mf_id']
    )
    save_changes(new_user_answer)
    return generate_new_user_answer(new_user_answer)


def save_once(data):
    new_user_answer = UserAnswer(
        answer=data['answer'],
        question_id=data['question_id'],
        mf_id=data['mf_id']
    )
    save_changes(new_user_answer)
    return update_user_answer(new_user_answer)


def get_all_user_answers():
    return UserAnswer.query.all()


def get_user_answer_count(town_id):
    return UserAnswer.query.join(Mf, (UserAnswer.mf_id == Mf.id)).join(
        Officer, (Mf.town_id == Officer.town_id)
    ).filter(Officer.town_id == town_id).group_by(UserAnswer.mf_id, UserAnswer.id).count()


def get_monthly_count(town_id):
    this_month = datetime.today().month
    return UserAnswer.query.join(Mf, (UserAnswer.mf_id == Mf.id)).join(Officer, (Mf.town_id == Officer.town_id))\
        .filter(Officer.town_id == town_id).filter(extract('month', UserAnswer.create_at) == this_month)\
        .group_by(UserAnswer.mf_id, UserAnswer.id).count()


def get_a_user_answer(user_answer_id):
    return UserAnswer.query.get_or_404(user_answer_id)


def generate_new_user_answer(user_answer):
    try:
        response_object = {
            'status': 'success',
            'message': 'user_answer Successfully registered.',
            'data': {
                'user_answer_id': user_answer.id,
                'user_answer': user_answer.answer,
                'question': user_answer.question_id,
                'mf_id': user_answer.mf_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def edit_user_answer(user_answer_id, data):
    user_answer = UserAnswer.query.filter_by(id=user_answer_id).first()
    if not user_answer:
        response_object = {
            'status': 'fail',
            'message': 'user_answer does not exist.'
        }
        return response_object, 409
    else:
        user_answer.name = data['user_answer']
        db.session.commit()
        return update_user_answer(user_answer)


def update_user_answer(user_answer):
    try:
        response_object = {
            'status': 'success',
            'message': 'user_answer Details Successfully updated.',
            'data': {
                'user_answer_id': user_answer.id,
                'user_answer': user_answer.answer,
                'question_id': user_answer.question_id
            }
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again.'
        }
        return response_object, 401


def delete_a_user_answer(user_answer_id):
    user_answer = get_a_user_answer(user_answer_id)
    db.session.delete(user_answer)
    db.session.commit()
    try:
        response_object = {
            'status': 'success',
            'message': 'user_answer Successfully deleted.'
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


