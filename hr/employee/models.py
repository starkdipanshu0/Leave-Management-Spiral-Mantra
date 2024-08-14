import datetime
from employee.utility import code_format
from django.db import models
from employee.managers import EmployeeManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    USER=[
        (1,'admin'),
        (2,'employee'),
        (3,'manager')
    ]
    user_type = models.PositiveSmallIntegerField(choices=USER,default=1)


class Role(models.Model):

    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')
        ordering = ['name','created']


    def __str__(self):
        return self.name


class Department(models.Model):


    name = models.CharField(max_length=125)
    description = models.CharField(max_length=125,null=True,blank=True)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True)


    class Meta:
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')
        ordering = ['name','created']

    def __str__(self):
        return self.name



# Education
class Education(models.Model):
    high_school_name = models.CharField(max_length=255, blank=True, null=True)
    high_school_obtained_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    high_school_year_of_passing = models.IntegerField(blank=True, null=True)
    high_school_result_file = models.FileField(upload_to='results/highschool/', blank=True, null=True)

    intermediate_college_name = models.CharField(max_length=255, blank=True, null=True)
    intermediate_obtained_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    intermediate_year_of_passing = models.IntegerField(blank=True, null=True)
    intermediate_result_file = models.FileField(upload_to='results/intermediate/', blank=True, null=True)

    graduation_university_name = models.CharField(max_length=255, blank=True, null=True)
    graduation_obtained_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    graduation_year_of_passing = models.IntegerField(blank=True, null=True)
    graduation_result_file = models.FileField(upload_to='results/graduation/', blank=True, null=True)

    post_graduation_university_name = models.CharField(max_length=255, blank=True, null=True)
    post_graduation_obtained_marks = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    post_graduation_year_of_passing = models.IntegerField(blank=True, null=True)
    post_graduation_result_file = models.FileField(upload_to='results/postgraduation/', blank=True, null=True)

    def __str__(self):
        return f"Education for {self.employee.user.first_name}"



class Employee(models.Model):

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    NOT_KNOWN = 'Not Known'

    GENDER = (
    (MALE,'Male'),
    (FEMALE,'Female'),
    (OTHER,'Other'),
    (NOT_KNOWN,'Not Known'),
    )


    FULL_TIME = 'Full-Time'
    PART_TIME = 'Part-Time'
    CONTRACT = 'Contract'
    INTERN = 'Intern'

    EMPLOYEETYPE = (
    (FULL_TIME,'Full-Time'),
    (PART_TIME,'Part-Time'),
    (CONTRACT,'Contract'),
    (INTERN,'Intern'),
    )

    # PERSONAL DATA

    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)
    birth_date = models.DateField(_('Birthday'),blank=False,null=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True, default='000-000-0000')
    personal_email = models.EmailField(max_length=255, null=True, blank=False)

    #Work Detail
    department =  models.ForeignKey(Department,verbose_name =_('Department'),on_delete=models.SET_NULL,null=True,default=None)
    role =  models.ForeignKey(Role,verbose_name =_('Role'),on_delete=models.SET_NULL,null=True,default=None)
    startdate = models.DateField(_('Employement Date'),help_text='date of employement',blank=False,null=True)
    employeetype = models.CharField(_('Employee Type'),max_length=15,default=FULL_TIME,choices=EMPLOYEETYPE,blank=False,null=True)
    employeeid = models.CharField(_('Employee ID Number'),max_length=10,null=True,blank=True)
    dateissued = models.DateField(_('Date Issued'),help_text='date staff id was issued',blank=False,null=True)

    #Leave Balance
    casual_leave_balance = models.PositiveIntegerField(default=0)
    paid_leave_balance = models.PositiveIntegerField(default=0)
    #Education
    education = models.OneToOneField(Education, on_delete=models.CASCADE, null= True, blank=True, related_name='education')
    # app related
    is_blocked = models.BooleanField(_('Is Blocked'),help_text='button to toggle employee block and unblock',default=False)
    is_deleted = models.BooleanField(_('Is Deleted'),help_text='button to toggle employee deleted and undelete',default=False)

    created = models.DateTimeField(verbose_name=_('Created'),auto_now_add=True,null=True)
    updated = models.DateTimeField(verbose_name=_('Updated'),auto_now=True,null=True)


    #PLUG MANAGERS
    objects = EmployeeManager()



    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ['-created']



    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


    @property
    def update_leave_balance(self, leave_type, days):
        if leave_type == 'casual':
            if self.casual_leave_balance >= days:
                self.casual_leave_balance -= days
            else:
                raise ValueError("Insufficient casual leave balance.")
        elif leave_type == 'paid':
            if self.paid_leave_balance >= days:
                self.paid_leave_balance -= days
            else:
                raise ValueError("Insufficient paid leave balance.")
        else:
            raise ValueError("Invalid leave type.")
        self.save()

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.birthday.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return



    @property
    def can_apply_leave(self):
        pass



    def save(self,*args,**kwargs):
        '''
        overriding the save method - for every instance that calls the save method
        perform this action on its employee_id
        added : March, 03 2019 - 11:08 PM

        '''
        get_id = self.employeeid #grab employee_id number from submitted form field
        data = code_format(get_id)
        self.employeeid = data #pass the new code to the employee_id as its orifinal or actual code
        super().save(*args,**kwargs) # call the parent save method
        # print(self.employeeid)




class FamilyContact(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='family_contact')
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    home_contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"Family contact details for {self.user.username}"

    class Meta:
        verbose_name = 'Family Contact'
        verbose_name_plural = 'Family Contacts'
