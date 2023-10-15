from django.db import models

class FixedAmount(models.Model):
    date = models.DateField(default="")
    type = models.CharField(max_length=50,default="")
    shop_name = models.CharField(max_length=200,default="")
    invoice_no = models.CharField(max_length=20,default="") 
    item_name = models.CharField(max_length=200,default="")
    qty = models.IntegerField(default="")
    price = models.IntegerField(default="")
    upload_file = models.FileField(upload_to='uploads/',default='your_default_value')
  
    
    def __str__(self):
     return self.shop_name 

class NonFixedAmount(models.Model):
    date = models.DateField(default="")
    type = models.CharField(max_length=50,default="")
    shop_name = models.CharField(max_length=200,default="")
    invoice_no = models.CharField(max_length=40,default="")
    item_name = models.CharField(max_length=200,default="")
    qty = models.IntegerField(default="")
    price = models.IntegerField(default="")
    upload_file = models.FileField(upload_to='uploads/')

    def __str__(self):
     return self.shop_name 