# Generated by Django 2.2.27 on 2022-03-30 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izenburua', models.CharField(max_length=100)),
                ('zuzendaria', models.CharField(max_length=60)),
                ('urtea', models.IntegerField()),
                ('generoa', models.CharField(max_length=2)),
                ('sinopsia', models.CharField(max_length=700)),
                ('bozkak', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Bozkatzailea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erabiltzailea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('gogokofilmak', models.ManyToManyField(to='FilmenGunea.Filma')),
            ],
        ),
    ]
