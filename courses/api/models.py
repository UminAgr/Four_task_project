from django.db import models


class Category(models.Model):
    name=models.CharField(max_length=45)
    imgpath=models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    latitude=models.CharField(max_length=45)
    longitude=models.CharField(max_length=45)
    address=models.CharField(max_length=60)

    def __str__(self):
        return self.address

class Contact(models.Model):

    class Choice(models.IntegerChoices):
        PHONE=1
        FACEBOOK=2
        EMAIL=3


    choice= models.IntegerField(choices=Choice.choices)
    value=models.CharField(max_length=56)
    course=models.ForeignKey("Course", on_delete=models.CASCADE, null=True, related_name='Contact' )

    def __str__(self):
        return self.value

class Course(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True,related_name='course')
    logo=models.CharField(max_length=45,blank=True)

    def __str__(self):
        return self.name




