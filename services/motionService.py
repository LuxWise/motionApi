from odoo import http
from odoo.http import Response, request
import json

class MotionService:
    
    @staticmethod
    def get_data():
        try:
            records = request.env['api.datos'].search([])
            data = [{"id": rec.id, "marca": rec.marca, "sucursal": rec.sucursal, "aspirante": rec.aspirante}  for rec in records]
            return MotionService._json_response({'status': 'success', 'data': data})
        except Exception as e:
            return MotionService._error_response(str(e))

    @staticmethod
    def create_data(data):
        try:
            request.env['api.datos'].create({
                'marca': data.get('marca'),
                'sucursal': data.get('sucursal'),
                'aspirante': data.get('aspirante')
            })
            return MotionService._json_response({'status': 'success'})
        except Exception as e:
            return MotionService._error_response(str(e))

    @staticmethod
    def _json_response(data, status_code=200):
        return Response(json.dumps(data), status=status_code, mimetype='application/json')

    @staticmethod
    def _error_response(error_message):
        return MotionService._json_response({'status': 'error', 'message': error_message}, status_code=500)

