# Generated by Django 4.2.5 on 2023-09-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('y360', '0007_departments_description_groups_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups_hierarchy',
            name='parentId',
            field=models.ForeignKey(help_text='id of a parent group', null=True, on_delete=django.db.models.deletion.CASCADE, to='y360.groups'),
        ),
        migrations.AlterField(
            model_name='groups_members',
            name='groupId',
            field=models.ForeignKey(help_text='group ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='y360.groups'),
        ),
        migrations.AlterField(
            model_name='groups_staff',
            name='groupId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='y360.groups'),
        ),
        migrations.AlterField(
            model_name='groups_staff',
            name='staffId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='y360.staff'),
        ),
    ]