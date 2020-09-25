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


class ShoeSize(models.Model):
    CHOICES = [
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9")
    ]
    size = models.CharField(max_length=5, choices=CHOICES, default="7")


class BrandName(models.Model):
    CHOICES = [
        ("nike", "nike"),
        ("addidas", "addidas"),
        ("rainbow", "rainbow"),
        ("vans", "vans"),
        ("other", "other")
    ]
    brand = models.CharField(max_length=200, choices=CHOICES, default="vans")


class ShoeMaterial(models.Model):
    CHOICES = [
        ("leather", "leather"),
        ("canvas", "canvas"),
        ("other", "other")
    ]
    material = models.CharField(max_length=200, choices=CHOICES, default="leather")


class FastenType(models.Model):
    CHOICES = [
        ("laces", "laces"),
        ("velcrow", "velcrow"),
        ("other", "other")
    ]
    fastener = models.CharField(max_length=200, choices=CHOICES, default="laces")


class Shoe(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, blank=False, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandName, blank=False, on_delete=models.CASCADE)
    shoe_type = models.ForeignKey(ShoeType, blank=False, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, blank=False, on_delete=models.CASCADE)
    size = models.ForeignKey(ShoeSize, blank=False, on_delete=models.CASCADE)
    material = models.ForeignKey(ShoeMaterial, blank=False, on_delete=models.CASCADE)
    fastener = models.ForeignKey(FastenType, blank=False, on_delete=models.CASCADE)
