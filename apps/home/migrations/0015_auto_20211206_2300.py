# Generated by Django 3.2.6 on 2021-12-06 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_bill_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='Bill_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Shop_address',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Shop_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Telephone_no',
            field=models.CharField(default='None', max_length=250),
        ),
        migrations.AlterField(
            model_name='bill',
            name='Total_items',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]