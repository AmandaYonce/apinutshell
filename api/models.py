from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)


class ShoeType(models.Model):
    CHOICES = [
        ("sneaker", "sneaker"),
        ("boot", "boot"),
        ("sandal", "sandal"),
        ("dress", "dress"),
        ("other", "other")
    ]
    style = models.CharField(max_length=200, choices=CHOICES, default="sneaker")


class ShoeColor(models.Model):
    CHOICES = [
        ("red", "red"),
        ("orange", "orange"),
        ("yellow", "yellow"),
        ("green", "green"),
        ("blue", "blue"),
        ("indigo", "indigo"),
        ("violet", "violet"),
        ("black", "black"),
        ("white", "white")
    ]
    color_name = models.CharField(max_length=20, choices=CHOICES, default="white")
