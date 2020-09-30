# Generated by Django 3.1.1 on 2020-09-30 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start', models.IntegerField()),
                ('end', models.IntegerField()),
                ('iri', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]