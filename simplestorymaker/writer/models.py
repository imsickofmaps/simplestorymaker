from django.db import models

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    reason = models.CharField(max_length=200)
    role = models.ForeignKey(Role)
    goal = models.CharField(max_length=200)

    def __unicode__(self):
        return u"So that " + self.reason + u" as a " + self.role.name + u" I want " + self.goal
