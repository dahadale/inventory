from django.db import models

# Create your modelse here.


class Owner(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.code + ' | ' + self.name


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
    def __str__(self):
        return self.code

class Entry(models.Model):   
   
    count_entry = models.AutoField(primary_key=True)
    part_number = models.ForeignKey('Consumable',on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    purchase_order = models.CharField(max_length=10)
    lot = models.CharField(max_length=20,blank=True,null=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,blank=True)
    date_shelflife = models.DateField(blank=True,null=True)
    quantity = models.IntegerField()
    login_user = models.CharField(max_length=20)
    picture = models.CharField(max_length=300)
    def __str__(self):
        return self.part_number.part_number

class Exit(models.Model):

    count_exit = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    count_requisition = models.ForeignKey('Requisition', on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE,blank=True)
    purchase_order = models.CharField(max_length=10)
    lot = models.CharField(max_length=20,blank=True,null=True)
    user_deliver = models.CharField(max_length=20)
    observations = models.TextField(max_length=250)
    def __str__(self):
        return self.part_number.part_number
   

class Requisition(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pendiente'),
        ('declined', 'Cancelado'),
        ('delivered', 'Entregado'),
    )
    count_requisition = models.AutoField(primary_key=True)
    part_number = models.ForeignKey('Consumable', on_delete=models.CASCADE)
    date_requisition = models.DateField(auto_now_add=True)
    course_code = models.ForeignKey('Course', on_delete=models.CASCADE)
    course_number = models.CharField(max_length=20,blank=True,null=True)
    quantity = models.IntegerField()
    user_requesting = models.CharField(max_length=20)
    status = models.CharField(max_length=30,choices = STATUS_CHOICES,default='pending')
    def __str__(self):
        return self.part_number.part_number + ' | ' + self.course_code.code + ' | ' + self.user_requesting









