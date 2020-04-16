from django.contrib import admin
from app1.models import Grades, Students

# Register your models here.
'''
 配置数据查询页相关功能
'''


# 在web页面添加班级时，会附带 添加学生 的输入框
class StudentsInfo(admin.TabularInline):  # 另一种显示方式 StackedInline
    model = Students
    extra = 2  # 学生输入框默认个数


class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]  # 和上面配套使用

    # 列表页属性列出数据的页面）列表页右上角会有一个增加数据按钮，点击进入修改页面

    # 列表页显示的字段名称；
    list_display = ('id', 'gname', 'gdate', 'ggirlnum', 'gboynum', 'IsDelete')
    # 列表页进行数据筛选的条件字段；
    list_filter = ['gname']
    # 列表页搜索栏进行搜索的字段
    search_fields = ['gname']
    # 列表页每页显示数据个数
    list_per_page = 5

    # 添加、修改页属性（增加修改数据的页面） 下面两个属性不能同时出现 。

    # 增加修改可以修改的字段
    # fields = ['ggirlnum','gboynum','gname','gdate','isDelete'] # 决定了修改页的字段顺序
    # 对增加页的字段进行分组 分为num 和person两个组。
    fieldsets = [("num", {"fields": ["ggirlnum", 'gboynum']}), ("person", {"fields": ['gname', 'gdate']})]


# 注册
admin.site.register(Grades, GradesAdmin)


@admin.register(Students)  # 使用装饰器注册admin
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
    list_display = ('id', 'sname', gender, 'sage', 'scontent', 'isDelete', 'sgrade')
    list_filter = ['sname']
    search_fields = ['sname']
    list_per_page = 5
    # 添加、修改页属性 下面两个属性不能同时出现
    fields = ['sname', 'sgender', 'sage', 'scontent', 'isDelete', 'sgrade']  # 决定了修改页的字段顺序
    # 页面中动作功能显示位置设置
    actions_on_bottom = True
    actions_on_top = False


# admin.site.register(Student, StudentAdmin) 注释一般使用装饰器 而不是调用此函数


# 注册富文本模型类
from app1.models import Text

admin.site.register(Text)
