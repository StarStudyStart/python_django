from django.db import models


# Create your models here.

class Customer(models.Model):
    """客户表"""
    pass


class CustomerFollow(models.Model):
    """跟进记录"""
    pass


class Enrollment(models.Model):
    """报名表"""
    pass


class Course(models.Model):
    """课程表"""
    pass


class CourseList(models.Model):
    """班级表"""
    pass


class CourseRecord(models.Model):
    """课程记录表"""
    pass


class StudyRecord(models.Model):
    """学习记录表"""
    pass


class Role(models.Model):
    """角色表：讲师、学生、老板"""
    pass


class UserProfile(models.Model):
    """账户表"""
    pass
