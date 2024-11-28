# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_enri(models.Model):
    _name = 'test_enri.test_enri'
    _description = 'esta es una descripcion'

    # Campos de la tabla
    name = fields.Char(string="Nombre", required=True)
    value = fields.Integer(string="ValorX")
    value2 = fields.Float(string="ValueY")
    description = fields.Text(string="Descripcion")

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
