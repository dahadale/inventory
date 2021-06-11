from django.db import models

# Create your modelse here.

class Owner(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.code + ' | ' + self.name

class Movement(models.Model):   
    MOVEMENT_TYPE_CHOICES = [
        ('entry', 'Entrada'),
        ('exit', 'Salida'),
       ]
    movement_type = models.CharField(
        max_length=10,
        choices=MOVEMENT_TYPE_CHOICES,
        default= 'exit',
    )
    date = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100,blank=True,null=True)
    consumable = models.ForeignKey('Consumable', on_delete=models.CASCADE)
    purchase_order = models.CharField(max_length=10)
    lot = models.CharField(max_length=20,blank=True,null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,blank=True)
    date_shelflife = models.DateField(blank=True,null=True)
    quantity = models.IntegerField()
    user_requesting = models.CharField(max_length=20)
    user_deliver = models.CharField(max_length=20)
    login_user = models.CharField(max_length=20)
    count = models.IntegerField(blank=True,null=True)



    def __str__(self):
        return self.movement_type + '-' + self.consumable.part_number

class Consumable(models.Model):
    part_number = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    fsc = models.CharField(max_length=10)
    niin = models.CharField(max_length=20)  
    unit_price = models.FloatField()
    unit_issue = models.CharField(max_length=10)
    shelf_life = models.BooleanField(default = False)  
    def __str__(self):
        return self.part_number + '  |  ' + self.item_name

class Location(models.Model):
    code = models.CharField(max_length=15)
    description = models.TextField(max_length=200)
    def __str__(self):
        return self.code + ' | ' + self.description

class LocationConsumable(models.Model):
    consumable  = models.ForeignKey(Consumable, on_delete=models.CASCADE)
    location  = models.ForeignKey(Location, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('consumable', 'location',)

class Course(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)














