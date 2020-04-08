from django.db import models


# Create your models here.
class Person(models.Model):
    p_name = models.CharField(max_length=16)

    class Meta:
        abstract = True     # 不创建Person模型


class Student(Person):
    s_sex = models.BooleanField(default=True)


class Card(models.Model):
    id_num = models.CharField(max_length=18, unique=True)
    id_stu = models.OneToOneField(Student, on_delete=models.CASCADE)


class Class(models.Model):
    c_name = models.CharField(max_length=16)
    c_student = models.ManyToManyField(Student)


class Fresh(Student):
    f_department = models.CharField(max_length=16)
