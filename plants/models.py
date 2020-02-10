from django.db import models

# Kategoria rośliny

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False, default="",
        unique=True,
        verbose_name="Name",
        help_text="",
    )

    def __str__(self):
        return self.name

# Pomieszczenie

class Room(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False, default="",
        unique=True,
        verbose_name="Name",
        help_text="",
    )

    EXPOSURE_CHOICES = [
        ('dark', 'Dark'),
        ('shade', 'Shade'),
        ('partsun', 'Part sun'),
        ('sunny', 'Sunny'),
    ]

    exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        blank=False, null=False, default="",
        verbose_name="Sun exposure",
        help_text="",
    )

    TEMPERATURE_CHOICES = [
        ('cold', 'Cold'),
        ('medium', 'Medium'),
        ('warm', 'Warm'),
    ]

    temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        blank=False, null=False, default="",
        verbose_name="Temperature",
        help_text="",
    )

    HUMIDITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        blank=False, null=False, default="",
        verbose_name="Humidity",
        help_text="",
    )

    draft = models.BooleanField(
        blank=True, null=False, default=False,
        verbose_name="Draft",
        help_text="",
    )

    def __str__(self):
        return self.name

# Roślina

class Plant(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False, null=False, 
        unique=True,
        verbose_name="Name",
        help_text="",
    )

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, 
        blank=False, null=False, 
        verbose_name="Plant's category",
        help_text="",
    )
    
    room = models.ForeignKey(
        Room, on_delete=models.SET_NULL, 
        default=None, blank=True, null=True, 
        verbose_name="Room",
        help_text="",
    )

    watering_interval = models.PositiveIntegerField(
        blank=False, null=False,
        verbose_name="Watering interval",
        help_text="In seconds",
    )

    fertilizing_interval = models.PositiveIntegerField(
        blank=False, null=False,
        verbose_name="Fertilizing interval",
        help_text="In seconds",
    )
    
    EXPOSURE_CHOICES = Room.EXPOSURE_CHOICES
    required_exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        blank=False, null=False,
        verbose_name="Sun exposure",
        help_text="",
    )


    TEMPERATURE_CHOICES = Room.TEMPERATURE_CHOICES
    required_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        blank=False, null=False,
        verbose_name="Sun exposure",
        help_text="",
    )

    HUMIDITY_CHOICES = Room.HUMIDITY_CHOICES
    required_humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        blank=False, null=False,
        verbose_name="Sun exposure",
        help_text="",
    )
    
    blooming = models.BooleanField(
        default=False, blank=True, null=False,
        verbose_name="Blooming",
        help_text="",
    )

    DIFFICULTY = [
        (1, 'Low'),
        (2, 'Medium-low'),
        (3, 'Medium'),
        (4, 'Medium-high'),
        (5, 'High'),
    ]

    difficulty = models.PositiveIntegerField(
        blank=False, null=False, default=1,
        verbose_name="Cultivation difficulty level",
        help_text="",
    )

    last_watered = models.DateTimeField(
        default=None, blank=True, null=True,
        verbose_name="Last watering timestamp",
        help_text="",
    )

    last_fertilized = models.DateTimeField(
        default=None, blank=True, null=True,
        verbose_name="Last fertilizing timestamp",
        help_text="",
    )

    def __str__(self):
        return self.name

