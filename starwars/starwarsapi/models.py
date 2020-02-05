from django.db import models

# Create your models here.

class Planet(models.Model):
    name=models.CharField(max_length=200)
    climate=models.CharField(max_length=200, null=True)
    terrain=models.CharField(max_length=200, null=True)
    image=models.CharField(max_length=200, null=True, blank=True)

class Species(models.Model):
    name=models.CharField(max_length=200)
    classification=models.CharField(max_length=200, null=True)
    language=models.CharField(max_length=200, null=True)

class Vehicle(models.Model):
    name=models.CharField(max_length=200)
    manufacturer=models.CharField(max_length=200, null=True)
    max_speed=models.IntegerField(null=True)
    passengers=models.IntegerField(null=True)    
    vehicle_class=models.CharField(max_length=200, null=True)

class Starship(models.Model):
    name=models.CharField(max_length=200)
    manufacturer=models.CharField(max_length=200, null=True)
    max_speed=models.IntegerField(null=True)
    passengers=models.IntegerField(null=True)    
    starship_class=models.CharField(max_length=200, null=True)

class Movie(models.Model):
    title=models.CharField(max_length=200)
    episode=models.IntegerField()
    roman_numeral=models.CharField(max_length=5, blank=True)
    opening_crawl=models.CharField(max_length=1000, blank=True)
    poster=models.CharField(max_length=1000, blank=True)
    # characters=models.ManyToManyField(Character, through="CharacterMovie")

class Character(models.Model):
    name=models.CharField(max_length=200)  
    gender=models.CharField(max_length=200, null=True)
    planet=models.CharField(max_length=200, null=True)
    species=models.CharField(max_length=200, null=True)    
    image=models.CharField(max_length=200, null=True)
    force_sensitive=models.BooleanField(null=True, blank=True)
    side=models.CharField(max_length=200, null=True, blank=True)
    role=models.CharField(max_length=200, null=True, blank=True)
    quote=models.CharField(max_length=200, null=True, blank=True)
    lightsaber=models.CharField(max_length=200, null=True, blank=True)
    sith_name=models.CharField(max_length=200, null=True, blank=True)
    movies=models.ManyToManyField(Movie, through="CharacterMovie")

class CharacterMovie(models.Model):
    character=models.ForeignKey(Character, on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)



