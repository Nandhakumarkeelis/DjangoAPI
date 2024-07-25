from django.db import models

# Create your models here.
class Color(models.Model):
    Color_Name= models.CharField(max_length= 100)

    def __str__(self):
        return self.Color_Name

class Person(models.Model):
    Color= models.ForeignKey(Color, null= True, blank= True, on_delete= models.CASCADE, related_name= 'Color')
    Name= models.CharField(max_length= 100)
    Age= models.IntegerField()
    Country= models.CharField(max_length=100)

    def __str__(self):
        return self.Name
    

class Books(models.Model):
    AuthorName= models.CharField(max_length= 100, null= True)
    BookName= models.CharField(max_length= 300, null= True)
    PublishedDate= models.DateField(null= True, blank= True)

    def __str__(self):
        return self.BookName