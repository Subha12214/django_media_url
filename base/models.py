from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    simages=models.ImageField(upload_to='uploads/',default='default.webp')


'''   
static
     css
     images
         uploads
         default.png

pip install pillow

'''