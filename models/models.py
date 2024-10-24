from odoo import models, fields, api

class datos(models.Model):
  _name = 'api.datos'
  _description = 'Datos de la API'
  
  marca = fields.Char(string="Marca", required=True)
  sucursal = fields.Char(string="Sucursal", required=True)
  aspirante = fields.Char(string="Aspirante", required=True)
