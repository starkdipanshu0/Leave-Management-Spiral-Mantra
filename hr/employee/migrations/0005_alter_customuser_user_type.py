# Generated by Django 5.1 on 2024-08-12 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'employee'), (3, 'manager'), (1, 'admin')], default=1, max_length=50),
        ),
    ]
