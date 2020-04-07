from django.db import models


# Create your models here.

class Grades(models.Model):
    gname = models.CharField(max_length=22)
    gdate = models.DateField()
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    IsDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.gname


class Student(models.Model):
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades",on_delete=models.CASCADE,)
    def __str__(self):
        return self.sname