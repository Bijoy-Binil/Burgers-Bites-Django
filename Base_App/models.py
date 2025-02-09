from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name=models.CharField(max_length=15)

    def __str__(self):
        return self.Category_name
    

class Items(models.Model):
    Item_name=models.CharField(max_length=32)
    description=models.TextField(blank=False)
    price=models.IntegerField()
    Category=models.ForeignKey(ItemList,related_name='Name',on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Item_name
    

class AboutUs(models.Model):
    Description=models.TextField(blank=False)

  

class Feedback(models.Model):
    User_name=models.CharField(max_length=15)
    Description=models.TextField(blank=False)
    Rating=models.IntegerField()
    Image=models.ImageField(upload_to='Items/',blank=True)

    def __str__(self):
        return self.User_name
    

class BookTable(models.Model):
    Name=models.CharField(max_length=15)
    Phone_number=models.IntegerField()
    Email=models.EmailField()
    Total_person=models.IntegerField(blank=True,null=True)
    Booking_date=models.DateField(blank=True,null=True)

    def __str__(self):
        return self.Name
