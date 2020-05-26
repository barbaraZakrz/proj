# Generated by Django 3.0.6 on 2020-05-26 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kurs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_kursu', models.IntegerField()),
                ('nazwa', models.CharField(max_length=30)),
                ('dzien_godzina', models.CharField(max_length=30)),
                ('semestr', models.CharField(max_length=30)),
                ('cena', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Nauczyciel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nauczyciela', models.IntegerField()),
                ('nazwiskoN', models.CharField(max_length=30)),
                ('imieN', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Rodzaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
                ('jezyk', models.CharField(max_length=30)),
                ('poziom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Uczen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ucznia', models.IntegerField()),
                ('nazwiskoU', models.CharField(max_length=30)),
                ('imieU', models.CharField(max_length=30)),
                ('nazwiskoR', models.CharField(max_length=30)),
                ('imieR', models.CharField(max_length=30)),
                ('id_kursu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkola.Kurs')),
            ],
        ),
        migrations.CreateModel(
            name='Nauczyciel_Rodzaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nauczyciela', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkola.Nauczyciel')),
                ('rodzaj_kursu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkola.Rodzaj')),
            ],
        ),
        migrations.AddField(
            model_name='kurs',
            name='id_nauczyciela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkola.Nauczyciel'),
        ),
        migrations.CreateModel(
            name='Dzien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nr_sali', models.IntegerField()),
                ('dzien_godzina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='szkola.Kurs')),
            ],
        ),
    ]
