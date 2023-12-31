# Generated by Django 4.2.5 on 2023-09-19 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('y360', '0005_alter_groups_hierarchy_childid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domains',
            fields=[
                ('name', models.CharField(help_text='full domain name', max_length=200, primary_key=True, serialize=False)),
                ('isMaster', models.BooleanField(help_text='is main or alias')),
            ],
        ),
    ]
