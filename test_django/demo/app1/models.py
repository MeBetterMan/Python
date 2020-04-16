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

    class Meta:
        db_table = 'grades'  # 定义数据表名，如果不写，数据表名默认为 应用名小写_类名小写
        ordering = []


# 自定义管理器类Manger。下面重写的方法会自动筛选掉isDelete=True的数据
class StudentManager(models.Manager):
    def get_queryset(self):
        return super(StudentManager, self).get_queryset().filter(isDelete=False)

    # 管理器中定义方法 用来创建对象 然后返回的stu调用save方法进行保存
    def createStudent(self, name, age, gender, grade, content, isD=False):
        stu = self.mode()  # 用来创建空对象
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.sgrade = grade
        stu.isDelete = isD
        return stu


class Students(models.Model):
    # 自定义模型管理器属性名字 ，自定义后objects属性就不存在了
    stuObj = models.Manager()
    # 使用自定义的Manager类的管理器
    stuObj2 = StudentManager()
    sname = models.CharField(max_length=20)
    sgender = models.BooleanField(default=True)
    sage = models.IntegerField()
    scontent = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    # 关联外键
    sgrade = models.ForeignKey("Grades", on_delete=models.CASCADE, )

    def __str__(self):
        return self.sname

    # 元数据主要设置字段之外的一些配置
    class Meta:
        db_table = 'students'  # 定义数据表名，如果不写，数据表名默认为 应用名小写_类名小写
        ordering = ['id']  # 对象默认排序字段，获取对象的列表时可以使用，此时为升序   ordering=['-id']加一个减号为降序。

    # 定义一个类方法创建对象
    @classmethod
    def createStudent(cls, name, age, gender, grade, content, isD=False):
        # cls 代表的就是类名，可以直接使用cls创建对象或者访问类变量
        student = cls(sname=name, sage=age, sgrade=grade, sgender=gender, scontent=content, isDelete=isD)
        return student


from tinymce.models import HTMLField


class Text(models.Model):
    str = HTMLField()
