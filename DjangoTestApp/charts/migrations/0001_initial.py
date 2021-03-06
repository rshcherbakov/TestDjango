# Generated by Django 2.0.3 on 2018-03-12 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='RatesToStore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='exchangerates',
            name='currencyCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.RatesToStore'),
        ),
    ]
