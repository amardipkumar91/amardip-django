# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class American(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    departuredate = models.DateField(db_column='departureDate', blank=True, null=True)  # Field name made lowercase.
    origin = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    emptyseats = models.IntegerField(db_column='emptySeats', blank=True, null=True)  # Field name made lowercase.
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'american'


class NewYoutube(models.Model):
    product = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    last_sync_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'new_youtube'


class StockPrices(models.Model):
    stock = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    price1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_prices'
