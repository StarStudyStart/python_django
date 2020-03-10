from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    """标签"""
    name = models.CharField(max_length=32)


class Customer(models.Model):
    """客户表"""
    name = models.CharField(max_length=20, verbose_name='客户名称')
    contact = models.CharField(max_length=64, verbose_name='联系方式')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='联系电话')
    referral_choices = (
        (0, '百度'),
        (1, '知乎'),
        (2, '介绍')
    )
    referral = models.SmallIntegerField(choices=referral_choices, verbose_name='来源')
    consult_course = models.ForeignKey("Course", verbose_name='咨询课程', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True, verbose_name='描述')
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'name:%s,contact: %s' % (self.name, self.contact)


class CustomerFollow(models.Model):
    """跟进记录"""
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='跟进记录')
    consultant = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    intentioned_choices = (
        (0, '一个月报名'),
        (1, '无报名意向'),
        (2, '已在其他机构报名'),
    )
    intentioned = models.SmallIntegerField(choices=intentioned_choices, verbose_name='意向')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer + self.content


class Enrollment(models.Model):
    """报名表"""
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    enrolled_class = models.ForeignKey("CourseList", on_delete=models.CASCADE)
    consultant = models.ForeignKey("UserProfile", on_delete=models.CASCADE)
    contract_agreed = models.BooleanField(default=True)
    contract_approved = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s,%s" % (self.customer, self.contract_approved)


class Course(models.Model):
    """课程表"""
    name = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    period = models.CharField(max_length=32, default='4个月')
    outline = models.TextField(verbose_name='课程大纲')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class CourseList(models.Model):
    """班级表"""
    semester = models.CharField(max_length=64, verbose_name='学期')
    course = models.ForeignKey("Course", on_delete=models.CASCADE)
    teachers = models.ManyToManyField("UserProfile")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.semester, self.teachers)


class CourseRecord(models.Model):
    """课程记录表"""
    from_class = models.ForeignKey("CourseList", on_delete=models.CASCADE)
    day_num = models.CharField(max_length=32, verbose_name="第几天")
    has_homework = models.BooleanField(default=True)
    homework_title = models.CharField(max_length=32, blank=True, null=True)
    homework_content = models.TextField(blank=True, null=True)
    outline = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.day_num, self.homework_title)


class StudyRecord(models.Model):
    """学习记录表"""
    pass


class Role(models.Model):
    """角色表：讲师、学生、老板"""
    name = models.CharField(max_length=64)

    def __str__(self):
        return "%s" % self.name


class UserProfile(models.Model):
    """账户表"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta():
        verbose_name = '账户管理'
