# -*- coding: utf-8 -*-

db.define_table('asistente',
    Field('nombre','string',length=30),
    Field('apellido','string',length=30),
    Field('dni','integer',length=10),
    Field('email','string',length=40),
    Field('ocupacion','string'),
    Field('provincia','string'),
    Field('certificado','boolean',label='Solicita certificado?'),
    Field('instalacion','boolean',label='Lleva un dispositivo para participar del install fest?'),
    Field('dispositivo','string'),
    Field('distribucion','string',default='Seleccione una distribucion...'),
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
db.asistente.dni.requires=IS_NOT_EMPTY()

db.asistente.email.comment=('(requerido)')
db.asistente.email.requires=IS_EMAIL()

db.asistente.ocupacion.requires=IS_IN_SET(['Estudiante','Tecnico','Sysadmin','Programador','Empresario','Independiente','Entusiasta','Amigo de Matt'])

############################################
#Informacion requerida para el install fest#
############################################
db.asistente.dispositivo.requires=IS_IN_SET(['PC','Notebook','Netbook','Smartphone','Tablet','Otro...'])
db.asistente.distribucion.requires=IS_IN_SET(['Debian','Ubuntu','Linux Mint','Fedora','Tuquito','Dream Linux','Puppy'])
