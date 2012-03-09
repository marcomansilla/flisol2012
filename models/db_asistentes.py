# -*- coding: utf-8 -*-

db.define_table('asistente',
    Field('nombre','string',length=30),
    Field('apellido','string',length=30),
    Field('dni','integer',length=10),
    Field('email','string',length=40),
    Field('ocupacion','string',default='Estudiante'),
    Field('institucion','string'),
    Field('provincia','string',default='Salta'),
    Field('certificado','boolean',label='Solicita certificado?'),
    Field('instalacion','boolean',label='Lleva un dispositivo para participar del install fest?'),
    Field('dispositivo','string',default='PC'),
    Field('distribucion','string',default='Debian'),
    Field('comentario','text'),
    Field('fecha','datetime',default=request.now,writable=False),
    )

################################
#Validacion de datos personales#
################################
db.asistente.nombre.comment=('(requerido)')
db.asistente.nombre.requires=IS_NOT_EMPTY()

db.asistente.apellido.comment=('(requerido)')
db.asistente.apellido.requires=IS_NOT_EMPTY()

db.asistente.dni.comment=('(requerido)')
db.asistente.dni.requires=[IS_NOT_EMPTY(), IS_NOT_IN_DB(db,'asistente.dni')]

db.asistente.provincia.comment=XML(str(T('(see %s)',A('[2]',_href='#footnote2'))))

db.asistente.email.comment=('(requerido)')
db.asistente.email.requires=[IS_EMAIL(), IS_NOT_IN_DB(db,'asistente.email')]

db.asistente.ocupacion.requires=IS_IN_SET(['Estudiante','Tecnico','Sysadmin','Programador','Empresario','Independiente','Entusiasta','Amigo de Matt'])

db.asistente.provincia.requires=IS_IN_SET(['Buenos Aires','Catamarca','Chaco','Chubut','Córdoba','Corrientes','Entre Ríos','Formosa','Jujuy','La Pampa,','La Rioja','Mendoza','Misiones','Neuquén','Río Negro','Salta','San Juan','San Luis','Santa Cruz','Santa Fe','Santiago del Estero','Tierra del Fuego, Antártida e Islas del Atlántico Sur','Tucumán'])

############################################
#Informacion requerida para el install fest#
############################################
db.asistente.instalacion.comment=()

db.asistente.distribucion.comment=XML(str(T('Seleccionar la distribución que desea instalar (ver %s)',A('[1]',_href='#footnote1'))))

db.asistente.dispositivo.requires=IS_IN_SET(['PC','Notebook','Netbook','Smartphone','Tablet','Otro...'])
db.asistente.distribucion.requires=IS_IN_SET(['Debian','Ubuntu','Linux Mint','Fedora','Tuquito','Dream Linux','Puppy'])
