from flask import request
from flask_restplus import Resource
from app.main.util.officer_decorator import *
from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import *
from ..service.mf_reimbursement_service import *
api = MfReimbursementDto.api
_mf_reimbursement = MfReimbursementDto.mf_reimbursement


@api.route('/all')
class MfReimbursementList(Resource):
    @api.doc('list_of_registered_mf_reimbursements')
    @api.marshal_list_with(_mf_reimbursement, envelope='data')
    def get(self):
        """List all registered mf reimbursements"""
        return get_all_mf_reimbursements()


@api.route('/<mf_id>/all')
class MfReimbursementList(Resource):
    @api.doc('list_of_registered_mf_reimbursements')
    @api.marshal_list_with(_mf_reimbursement, envelope='data')
    def get(self, mf_id):
        """List all registered mf reimbursements"""
        return get_all_mf_reimbursements_by_mf(mf_id)


@api.route('/new')
class MfReimbursementList(Resource):
    @api.expect(_mf_reimbursement, validate=True)
    @api.response(201, 'reimbursement successfully created.')
    @api.doc('create a new reimbursement')
    @admin_token_required
    def post(self):
        """Creates a new mf reimbursement """
        data = request.json
        return save_new_mf_reimbursement(data=data)


@api.route('/<mf_reimbursement_id>')
@api.param('mf_reimbursement_id', 'The reimbursement identifier')
@api.response(404, 'mf_reimbursement not found.')
class MfReimbursement(Resource):
    @api.doc('get a mf_reimbursement')
    @api.marshal_with(_mf_reimbursement)
    def get(self, mf_reimbursement_id):
        """get a mf reimbursement given its identifier"""
        le_mf_reimbursement = get_an_mf_reimbursement(mf_reimbursement_id)
        if not le_mf_reimbursement:
            return {'success': False, 'message': 'mf_reimbursement not found'}
        else:
            return le_mf_reimbursement


@api.route('/<mf_reimbursement_id>/edit')
@api.param('mf_reimbursement_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfReimbursement(Resource):
    @api.expect(_mf_reimbursement, validate=False)
    @api.response(201, 'mf successfully edited.')
    @api.doc('edit a new mf')
    @admin_token_required
    def put(self, mf_reimbursement_id):
        """Edits a mf reimbursement"""
        le_mf_reimbursement = get_an_mf_reimbursement(mf_reimbursement_id)
        if not le_mf_reimbursement:
            return {'success': False, 'message': 'mf not found'}
        data = request.json
        return edit_mf_reimbursement(mf_reimbursement_id, data=data)


@api.route('/<mf_reimbursement_id>/delete')
@api.param('mf_reimbursement_id', 'The mf identifier')
@api.response(404, 'mf not found.')
class MfReimbursement(Resource):
    @api.doc('delete an mf')
    @admin_token_required
    def delete(self, mf_reimbursement_id):
        """ Delete mf reimbursement by id """
        le_mf_reimbursement = get_an_mf_reimbursement(mf_reimbursement_id)
        if not le_mf_reimbursement:
            return {'success': False, 'msg': 'mf does not exist'}
        else:
            return delete_an_mf_reimbursement(mf_reimbursement_id)
