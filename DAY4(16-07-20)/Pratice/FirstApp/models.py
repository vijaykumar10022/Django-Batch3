import datetime
from django import forms
from django.db import models
from django.utils import timezone


# Create your models here.

class adminfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Admin File'
        verbose_name_plural = 'Admin Files'

class aplsafile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'APLSA File'
        verbose_name_plural = 'APLSA Files'

class compliancefile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Compliance File'
        verbose_name_plural = 'Compliance Files'

class itfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'IT File'
        verbose_name_plural = 'IT Files'

class ruralfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Rural File'
        verbose_name_plural = 'Rural Files'

class srfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'SR File'
        verbose_name_plural = 'SR Files'

class securityfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Security File'
        verbose_name_plural = 'Security Files'

class technologyfile(models.Model):
    filename = models.CharField(max_length = 100)
    description = models.TextField(blank = False)
    date_added = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.filename
    def added(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    class Meta:
        verbose_name = 'Technology File'
        verbose_name_plural = 'Technology Files'

