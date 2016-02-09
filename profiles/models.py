from django.contrib.auth.models import User, Group
from django.db import models
from django.db.models.signals import post_save
from django.core.validators import URLValidator
from django.core import urlresolvers
from jsonfield import JSONField
from datetime import datetime
# Create your models here.


class StudentDetail(models.Model):
    '''
    It stores information about the Students of college.
    '''
    # List of courses
    BTech = 'BTECH'
    MCA = 'MCA'
    MBA = 'MBA'
    MTECH = 'MTECH'
    OTHERS = 'OTHER'
    COURSE = (
        (BTech, 'B.Tech'),
        (MCA, 'MCA'),
        (MBA, 'MBA'),
        (MTECH, 'Masters of Technology'),
        (OTHERS, 'Others'),
    )
    # List of branches
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    MT = 'MT'
    BRANCH = (
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (EE, 'Electrical Engineering'),
        (ECE, 'Electronics and Communication Engineering'),
        (EEE, 'Electrical and Electronics Engineering'),
        (CE, 'Civil Engineering'),
        (IC, 'Instrumentation and Control Engineering'),
        (ME, 'Mechanical Engineering'),
        (MT, 'Manufacturing Technology'),
    )
    user = models.OneToOneField(User)
    course = models.CharField(max_length=5, choices=COURSE, default=None, null=True)
    branch = models.CharField(max_length=5, choices=BRANCH, default=None, null=True)
    semester = models.PositiveIntegerField(default=None, null=True)
    univ_roll_no = models.PositiveIntegerField(blank=True, null=True, editable=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True, editable=True)
    father_name = models.CharField(max_length=200, blank=True, null=True, editable=True)
    mother_name = models.CharField(max_length=200, blank=True, null=True, editable=True)
    address = models.CharField(max_length=500, blank=True, null=True, editable=True)
    display_to_others = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)
    # relevent_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # academics_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # administration_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # misc_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # tnp_last_seen = models.DateTimeField(auto_now_add=True,editable = True)
    # events_last_seen = models.DateTimeField(auto_now_add=True,editable = True)

    def __unicode__(self):
        return self.user.username


class FacultyDetail(models.Model):
    '''
    It stores the information about the faculties/administration of college
    '''
    user = models.OneToOneField(User)
    designation = models.CharField(max_length=100, blank=True, null=True, editable=True)
    department = models.CharField(max_length=100, blank=True, null=True, editable=True)
    contact_no = models.PositiveIntegerField(blank=True, null=True, editable=True)
    address = models.CharField(max_length=500, blank=True, null=True, editable=True)
    alternate_email = models.EmailField(max_length=254, blank=True, null=True, editable=True)
    display_to_others = models.BooleanField(default=False)

    created = models.DateTimeField("Created", auto_now_add=True, null=True)
    modified = models.DateTimeField("Last Modified", auto_now=True, null=True)

    def __unicode__(self):
        return self.user.username

    def get_full_name(self):
        return self.user.first_name + " " + self.user.last_name
