from django.db import models


class EmployeePostion(models.Model):

    position = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class EmployeeRegister(models.Model):

    fullname = models.CharField(max_length=100)
    mobile = models.IntegerField()
    emp_no = models.CharField(max_length=100)
    emp_pos = models.ForeignKey(EmployeePostion, on_delete = models.CASCADE)

