from django.contrib import admin
from app1.models import Grades,Student
# Register your models here.
'''
 配置数据查询页相关功能
'''

# 在web页面新建班级时，会附带 添加学生 的输入框
class StudentsInfo(admin.TabularInline): # 另一种显示方式 StackedInline
    model = Student
    extra = 2 # 学生输入框默认个数

class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    # 列表页属性
    list_display = ('id','gname','gdate','ggirlnum','gboynum','IsDelete')
    list_filter = ['gname']
    search_fields = ['gname']
    list_per_page = 5
    #添加、修改页属性 下面两个属性不能同时出现
   # fields = ['ggirlnum','gboynum','gname','gdate','isDelete'] # 决定了修改页的字段顺序
    fieldsets = [("num",{"fields":["ggirlnum",'gboynum']}),("person",{"fields":['gname','gdate']})]
# 注册
admin.site.register(Grades,GradesAdmin)



class StudentAdmin(admin.ModelAdmin):
    # 数据库里的布尔值，在web页面显示文字。 调用时gender,没有括号
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    # 在web页面显示的字段名字
    gender.short_description = '性别'
    # 列表页属性
    list_display = ('id','sname',gender,'sage','scontent','isDelete','sgrade')
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5
    #添加、修改页属性 下面两个属性不能同时出现
    fields = ['sname','sgender','sage','scontent','isDelete','sgrade'] # 决定了修改页的字段顺序

admin.site.register(Student,StudentAdmin)