from django.db import models

class Nauczyciel(models.Model):
    id_nauczyciela = models.IntegerField()
    nazwiskoN = models.CharField(max_length=30)
    imieN = models.CharField(max_length=30)

class Kurs(models.Model):
    id_kursu = models.IntegerField()
    nazwa = models.CharField(max_length=30)
    id_nauczyciela = models.ForeignKey(Nauczyciel, on_delete=models.CASCADE)
    dzien_godzina = models.CharField(max_length=30)
    semestr = models.CharField(max_length=30)
    cena = models.IntegerField()

class Uczen(models.Model):
    id_ucznia = models.IntegerField()
    id_kursu = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    nazwiskoU = models.CharField(max_length=30)
    imieU = models.CharField(max_length=30)
    nazwiskoR = models.CharField(max_length=30)
    imieR = models.CharField(max_length=30)

class Dzien(models.Model):
    dzien_godzina = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    nr_sali = models.IntegerField()

class Rodzaj(models.Model):
    nazwa = models.CharField(max_length=30)
    jezyk = models.CharField(max_length=30)
    poziom = models.CharField(max_length=30)

class Nauczyciel_Rodzaj(models.Model):
    id_nauczyciela = models.ForeignKey(Nauczyciel, on_delete=models.CASCADE)
    rodzaj_kursu = models.ForeignKey(Rodzaj, on_delete=models.CASCADE)
