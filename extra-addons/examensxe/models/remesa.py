# -*- coding: utf-8 -*-

from odoo import fields, models

class TestModel(models.Model):
    _name = "remesa"
    _description = "muy buena"


    id= fields.Integer(string="542387RT")
    producto= fields.Text(string="tomates")
    viabilidad= fields.Float(string="15")