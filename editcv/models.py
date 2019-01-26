from django.db import models
import datetime

from django.db import models
from django.utils import timezone
# Create your models here.


class User_Data(models.Model):
    def __str__(self):
        return self.name

    #need this?
    name = models.CharField(max_length=200)




class Header(models.Model):
    def __str__(self):
        return self.text

    #need this?
    text = models.CharField(max_length=200)

    user_data = models.ForeignKey(User_Data, on_delete=models.CASCADE)



class Header_Field(models.Model):
    def __str__(self):
        return self.text

    header = models.ManyToManyField(Header)


    text = models.CharField(max_length=200)

    #def was_published_recently(self):
    #    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Section(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length = 200)
#    votes = models.IntegerField(default=0)
#
#    def __str__(self):
#        return self.choice_text

class Section(models.Model):
    def __str__(self):
        return self.section_name

    section_name = models.CharField(max_length=200)

    user_data = models.ForeignKey(User_Data, on_delete=models.CASCADE)
    cvs = models.ManyToManyField(CV) #a section can be in many cvs, and a cv has many sections


class Entry(models.Model):
    def __str__(self):
        return self.entry_name

    section = models.ForeignKey(Section, on_delete=models.CASCADE) # section has many entries

    entry_name = models.CharField(max_length=200)
    entry_subtitle = models.CharField(max_length=200)
    entry_location = models.CharField(max_length=200)
    entry_date = models.CharField(max_length=200)

class Bullet(models.Model):
    def __str__(self):
        return self.bullet_text

    entry = models.ForeignKey(Entry, on_delete=models.CASCADE) # entry has many bullets

    bullet_text = models.CharField(max_length=200)


class CV(models.Model):
    def __str__(self):
        return self.cv_name

    cv_name = models.CharField(max_length=200)
    header = models.ForeignKey(Header, on_delete=models.SET_NULL)
