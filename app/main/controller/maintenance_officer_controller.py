from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.maintenance_officer_service import *
api = MaintenanceOfficerDto.api
_maintenance_officer = MaintenanceOfficerDto.maintenance_officer


@api.route('/all')
class MaintenanceOfficerList(Resource):
    @api.doc('list_of_registered_officers')
    @admin_token_required
    @api.marshal_list_with(_maintenance_officer, envelope='data')
    def get(self):
        """List all registered officer"""
        return get_all_maintenance_officers()


@api.route('/new')
class MaintenanceOfficerList(Resource):
    @api.expect(_maintenance_officer, validate=True)
    @api.response(201, 'maintenance officer successfully created.')
    @api.doc('create a new maintenance officer')
    @token_required
    def post(self):
        """Creates a new officer """
        data = request.json
        return save_new_maintenance_officer(data=data)


@api.route('/<int:maintenance_officer_id>')
@api.param('maintenance_officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class MaintenanceOfficer(Resource):
    @api.doc('get a officer')
    @token_required
    @api.marshal_with(_maintenance_officer)
    def get(self, maintenance_officer_id):
        """get a officer given its identifier"""
        m_officer = get_a_maintenance_officer(maintenance_officer_id)
        if not m_officer:
            return {'success': False, 'message': 'maintenance officer not found'}
        else:
            return m_officer


@api.route('/<int:maintenance_officer_id>/delete')
@api.param('maintenance_officer_id', 'The Officer identifier')
@api.response(404, 'Officer not found.')
class MaintenanceOfficer(Resource):
    @api.doc('delete an officer')
    @token_required
    def delete(self, maintenance_officer_id):
        """ Delete user by id """
        m_officer = get_a_maintenance_officer(maintenance_officer_id)
        if not m_officer:
            return {'success': False, 'msg': 'maintenance officer does not exist'}
        else:
            delete_a_maintenance_officer(maintenance_officer_id)
            return {'success': True, 'message': 'maintenance officer deleted successfully'}


@api.route('/<int:maintenance_officer_id>/deploy')
@api.param('maintenance_officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class OfficerDeploy(Resource):
    @api.doc('deploy an officer')
    @token_required
    def post(self, maintenance_officer_id):
        """deploy an officer given its identifier"""
        m_officer = get_a_maintenance_officer(maintenance_officer_id)
        if not m_officer:
            return {'success': False, 'msg': 'maintenance officer does not exist'}
        else:
            deployed_officer = deploy_a_maintenance_officer(maintenance_officer_id)
            return deployed_officer


@api.route('/<int:maintenance_officer_id>/suspend')
@api.param('maintenance_officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class Officer(Resource):
    @api.doc('suspend an officer')
    @token_required
    def post(self, maintenance_officer_id):
        """suspend an officer given its identifier"""
        m_officer = get_a_maintenance_officer(maintenance_officer_id)
        if not m_officer:
            return {'success': False, 'msg': 'maintenance officer does not exist'}
        else:
            suspended_officer = suspend_a_maintenance_officer(maintenance_officer_id)
            return suspended_officer


@api.route('/<int:maintenance_officer_id>/terminate')
@api.param('maintenance_officer_id', 'The officer identifier')
@api.response(404, 'officer not found.')
class Officer(Resource):
    @api.doc('terminate an officer')
    @token_required
    def post(self, maintenance_officer_id):
        """terminate an officer given its identifier"""
        m_officer = get_a_maintenance_officer(maintenance_officer_id)
        if not m_officer:
            return {'success': False, 'msg': 'maintenance officer does not exist'}
        else:
            terminated_officer = terminate_a_maintenance_officer(maintenance_officer_id)
            return terminated_officer



