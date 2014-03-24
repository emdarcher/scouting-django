# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TeamData'
        db.create_table(u'scouting_teamdata', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('scouter_name', self.gf('django.db.models.fields.CharField')(default='unidentified scouter', max_length=32)),
            ('match_number', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('team_number', self.gf('django.db.models.fields.PositiveIntegerField')(default=10000001)),
            ('catches', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('truss', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('assists', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('auto_points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('teleop_points', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('comments', self.gf('django.db.models.fields.TextField')(default='No Comments in Entry')),
        ))
        db.send_create_signal(u'scouting', ['TeamData'])


    def backwards(self, orm):
        # Deleting model 'TeamData'
        db.delete_table(u'scouting_teamdata')


    models = {
        u'scouting.teamdata': {
            'Meta': {'object_name': 'TeamData'},
            'assists': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'auto_points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'catches': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'comments': ('django.db.models.fields.TextField', [], {'default': "'No Comments in Entry'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'match_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'scouter_name': ('django.db.models.fields.CharField', [], {'default': "'unidentified scouter'", 'max_length': '32'}),
            'team_number': ('django.db.models.fields.PositiveIntegerField', [], {'default': '10000001'}),
            'teleop_points': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'truss': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['scouting']