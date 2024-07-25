from django.db import models

# Create your models here.

class Books(models.Model):
    AuthorName= models.CharField(max_length= 100, null= True)
    BookName= models.CharField(max_length= 300, null= True)
    PublishedDate= models.DateField(null= True, blank= True)

    def __str__(self):
        return self.BookName