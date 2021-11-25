# Generated by Django 3.2.9 on 2021-11-25 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('mood', models.CharField(choices=[('G', '😊'), ('N', '😐'), ('B', '😢'), ('A', '😡')], default='G', max_length=1)),
                ('day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.day')),
            ],
        ),
    ]