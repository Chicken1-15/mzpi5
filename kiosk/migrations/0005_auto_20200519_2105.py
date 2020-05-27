# Generated by Django 3.0.6 on 2020-05-19 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosk', '0004_auto_20200508_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='KioskUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('password_api', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='kioskmodel',
            name='x',
            field=models.DecimalField(decimal_places=40, max_digits=45),
        ),
        migrations.AlterField(
            model_name='kioskmodel',
            name='y',
            field=models.DecimalField(decimal_places=40, max_digits=45),
        ),
        migrations.AlterField(
            model_name='kioskmodel',
            name='z',
            field=models.DecimalField(decimal_places=40, max_digits=45),
        ),
    ]