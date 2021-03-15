import werkzeug
import requests
import logging
import datetime
_logger = logging.getLogger(__name__)

import odoo.http as http
from odoo.http import request

class Presupuesto_Controller(http.Controller):
    

    #Funcion de gracias luego que se agrega la informacion al modulo
    @http.route('/nuevo/presupuesto/creacion', type="http", auth="public", website=True)
    def support_presupuesto_nuevo2(self, **kw):
        email = http.request.env.user.email
        name = http.request.env.user.name
        dirrecion_fact = http.request.env.user.partner_id.street
        empresa = http.request.env.user.partner_id.id
        lista_productos = http.request.env['product.template'].sudo().search([('active', '=', True),('default_code', '=', 'ABE12')])
        return http.request.render('presupuesto_web_alpha.portal_create_presupuesto', {'email': email, 'name': name, 'empresa': empresa, 
                                                                                       'dirrecion_fact': dirrecion_fact, 
                                                                                       'lista_productos': lista_productos})

        #return http.request.render('presupuesto_web_alpha.portal_create_presupuesto', {})

    
    #Funcion de gracias luego que se agrega la informacion al modulo
    @http.route('/new/presupuesto/thanks', type="http", auth="public", website=True)
    def support_presupuesto_thanks(self, **kw):
        return http.request.render('presupuesto_web_alpha.presupuesto_thank_you', {})


    #Funcion para agregar un campo desde el formulario
    @http.route('/envio/presupuesto', type='http', auth="public", website=True)
    def submit_presupuesto(self, **kw):
        print('kw')
        #Busco el producto 
        produc = request.env['product.template'].sudo().search([('id', '=', int(kw.get('productos')) )])

        vals = {'partner_id': kw.get('empresa'),
                'partner_invoice_id': kw.get('empresa'), 
                'partner_shipping_id':kw.get('empresa'),
                'date_order': datetime.datetime.now(),
                'state': 'draft',
                'pricelist_id': '1',
                } 
        venta_presupuesto =  request.env['sale.order'].sudo().create(vals)
       
        #Creo la orde de la linea de venta 
        linea_orden = {
                        'order_id': venta_presupuesto.id,
                        'product_id': produc.id,
                        'name': produc.description_sale,
                        'price_unit': produc.list_price,
                        'product_uom': 1,
                        'product_uom_qty': 1,
                        }
        request.env['sale.order.line'].sudo().create(linea_orden)
       
        
        return werkzeug.utils.redirect("/new/presupuesto/thanks")
        
