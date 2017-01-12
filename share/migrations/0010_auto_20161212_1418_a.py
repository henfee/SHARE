# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-12 14:18
from __future__ import unicode_literals

import db.deletion
from django.conf import settings
from django.db import migrations, models
import share.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0009_auto_20161209_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractagent',
            name='change',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='affected_abstractagent', to='share.Change'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='extra',
            field=models.OneToOneField(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), to='share.ExtraData'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='same_as',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='sources',
            field=share.models.fields.TypedManyToManyField(editable=False, related_name='source_abstractagent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='abstractagent',
            name='version',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='share_abstractagent_version', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='change',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='affected_abstractagentrelation', to='share.Change'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='extra',
            field=models.OneToOneField(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), to='share.ExtraData'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='related',
            field=models.ForeignKey(on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='incoming_agent_relations', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='same_as',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentRelation'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='sources',
            field=share.models.fields.TypedManyToManyField(editable=False, related_name='source_abstractagentrelation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='subject',
            field=models.ForeignKey(on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='outgoing_agent_relations', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelation',
            name='version',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='share_abstractagentrelation_version', to='share.AbstractAgentRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='change',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='affected_abstractagentrelationversion', to='share.Change'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='extra',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), to='share.ExtraData'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='related',
            field=models.ForeignKey(db_index=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='related_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='same_as',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentRelation'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='subject',
            field=models.ForeignKey(db_index=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentrelationversion',
            name='subject_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='change',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='affected_abstractagentversion', to='share.Change'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='extra',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), to='share.ExtraData'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='extra_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='same_as',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentversion',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='agent',
            field=models.ForeignKey(on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='work_relations', to='share.AbstractAgent'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='agent_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='change',
            field=models.OneToOneField(editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='affected_abstractagentworkrelation', to='share.Change'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='creative_work',
            field=models.ForeignKey(on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='agent_relations', to='share.AbstractCreativeWork'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='creative_work_version',
            field=models.ForeignKey(db_index=False, editable=False, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractCreativeWorkVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='extra',
            field=models.OneToOneField(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), to='share.ExtraData'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='extra_version',
            field=models.OneToOneField(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.ExtraDataVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='same_as',
            field=models.ForeignKey(null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentWorkRelation'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='same_as_version',
            field=models.ForeignKey(db_index=False, editable=False, null=True, on_delete=db.deletion.DatabaseOnDelete(clause='CASCADE'), related_name='+', to='share.AbstractAgentWorkRelationVersion'),
        ),
        migrations.AlterField(
            model_name='abstractagentworkrelation',
            name='sources',
            field=share.models.fields.TypedManyToManyField(editable=False, related_name='source_abstractagentworkrelation', to=settings.AUTH_USER_MODEL),
        ),
    ]