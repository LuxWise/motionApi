from odoo import http
from odoo.http import request
from ..services.motionService import MotionService
import json

# Constantes
AUTH_TYPE = 'public'
CSRF_ENABLED = False
ROUTE_PREFIX = '/api'

class MotionApiController(http.Controller):
    
    @http.route(f'{ROUTE_PREFIX}/motion', auth=AUTH_TYPE, methods=['GET'], csrf=CSRF_ENABLED)
    def get_all_motion_data(self):
        return MotionService.get_data()

    @http.route('/api/motion', auth='public', methods=['POST'], csrf=False)
    def create_motion_data(self):
        data = json.loads(request.httprequest.data)
        if not data:
            return {"error": "No data provided"}
        
        return MotionService.create_data(data)

