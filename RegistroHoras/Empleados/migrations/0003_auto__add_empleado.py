# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Empleado'
        db.create_table('Empleados_empleado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('ApellidoPaterno', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('ApellidoMaterno', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
        ))
        db.send_create_signal('Empleados', ['Empleado'])


    def backwards(self, orm):
        # Deleting model 'Empleado'
        db.delete_table('Empleados_empleado')


    models = {
        'Empleados.empleado': {
            'ApellidoMaterno': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'ApellidoPaterno': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'Meta': {'ordering': "['ApellidoPaterno']", 'object_name': 'Empleado'},
            'Nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Empleados']