# Generated by Django 3.2.6 on 2021-11-28 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_bill_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Bill_picture',
            field=models.FileField(upload_to=''),
        ),
    ]
