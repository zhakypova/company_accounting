# Generated by Django 3.2 on 2023-02-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20230216_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.CharField(default='specialist', max_length=30),
            preserve_default=False,
        ),
    ]
