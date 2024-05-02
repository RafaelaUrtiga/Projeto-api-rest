# Generated by Django 5.0.4 on 2024-04-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('prazo', models.DateField(blank=True, null=True)),
                ('descricao', models.TextField(blank=True)),
                ('finalizada', models.BooleanField(default=False)),
            ],
        ),
    ]
