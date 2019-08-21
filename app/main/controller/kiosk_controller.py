from flask import request
from flask_restplus import Resource

from app.main.util.decorator import admin_token_required, token_required, admin_or_officer_token_required
from app.main.util.officer_decorator import officer_token_required

from ..util.dto import *
from ..service.kiosk_service import *
from flask_restplus import Resource, reqparse
from werkzeug.datastructures import FileStorage
parser = reqparse.RequestParser()
parser.add_argument('file', type=FileStorage, location='files')
api = KioskDto.api
_kiosk = KioskDto.kiosk


@api.route('/all')
class KioskList(Resource):
    @api.doc('list_of_registered_officers')
    @token_required
    @api.marshal_list_with(_kiosk, envelope='data')
    def get(self):
        """List all kiosks"""
        return get_all_kiosks()


@api.route('/new')
class KioskList(Resource):
    @api.expect(_kiosk, validate=True)
    @api.response(201, 'kiosk successfully created.')
    @api.doc('create a new kiosk')
    @token_required
    def post(self):
        """Creates a new kiosk """
        data = request.json
        return save_new_kiosk(data=data)


@api.route('/<int:kiosk_id>')
@api.param('kiosk_id', 'The kiosk identifier')
@api.response(404, 'kiosk not found.')
class Kiosk(Resource):
    @api.doc('get a kiosk')
    @token_required
    @api.marshal_with(_kiosk)
    def get(self, kiosk_id):
        """get a kiosk given its identifier"""
        kiosk = get_a_kiosk(kiosk_id)
        if not kiosk:
            api.abort(404)
        else:
            return kiosk


@api.route('/get_qr/<int:kiosk_id>')
@api.param('kiosk_id', 'The kiosk identifier')
@api.response(404, 'kiosk not found.')
class Kiosk(Resource):
    @api.doc('generate a kiosk qr code')
    def get(self, kiosk_id):
        """generate a kiosk qr code given its identifier"""
        le_kiosk = get_a_kiosk(kiosk_id)
        if not le_kiosk:
            return {'success': False, 'msg': 'kiosk does not exist'}
        else:
            return generate_kiosk_qr(kiosk_id)


@api.route('/qr/<kiosk_id>')
class KioskQr(Resource):
    @api.doc('download a kiosk qr code')
    def get(self, kiosk_id):
        """download a kiosk qr code given its identifier"""
        return get_kiosk_qr(kiosk_id)


@api.route('/read_qr')
class KioskQr(Resource):
    @api.doc('download a kiosk qr code')
    def post(self):
        """read a kiosk qr code given its identifier"""
        data = parser.parse_args()
        image = data['file']
        return read_kiosk_qr(image)


@api.route('/assign_kiosk/<int:kiosk_id>')
@api.param('kiosk_id', 'The kiosk identifier')
@api.response(404, 'kiosk not found.')
class Kiosk(Resource):
    @api.doc('assign a kiosk')
    @token_required
    def post(self, kiosk_id):
        """assign a kiosk"""
        le_kiosk = get_a_kiosk(kiosk_id)
        if not le_kiosk:
            api.abort(404)
        else:
            data = request.json
            return assign_kiosk(kiosk_id, data)


@api.route('/deassign_kiosk/<int:kiosk_id>')
@api.param('kiosk_id', 'The kiosk identifier')
@api.response(404, 'kiosk not found.')
class Kiosk(Resource):
    @api.doc('deassign a kiosk')
    @token_required
    def post(self, kiosk_id):
        """deassign a kiosk"""
        le_kiosk = get_a_kiosk(kiosk_id)
        if not le_kiosk:
            api.abort(404)
        else:
            data = request.json
            return deassign_kiosk(kiosk_id, data)


@api.route('/<int:kiosk_id>/delete')
@api.param('kiosk_id', 'The kiosk identifier')
@api.response(404, 'kiosk not found.')
class Kiosk(Resource):
    @api.doc('delete a kiosk')
    @token_required
    def delete(self, kiosk_id):
        """ Delete kiosk by id """
        le_kiosk = get_a_kiosk(kiosk_id)
        if not le_kiosk:
            return {'success': False, 'msg': 'kiosk does not exist'}
        else:
            delete_a_kiosk(kiosk_id)
            return {'success': True, 'message': 'kiosk deleted successfully'}

