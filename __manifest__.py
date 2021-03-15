{
    'name': 'Presupesto desde el portal del cliente',
    'version': '1.0',
    'category': 'sales',
    'sequence': 60,
    'summary': 'Genera una orden de presupuesto desde la web del portal del usario',
    'description': "Generacion de orden de presupuesto emitida por el cliente desde el portal del usuario",
    'author':'Ariel Cerrato',
    'depends': ['base'],
    'data': [
             'views/vista_web_presupuesto.xml',
      ],
    'installable': True,
    'auto_install': False,
    'application': False,
}