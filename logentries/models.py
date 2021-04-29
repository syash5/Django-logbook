from django.db import models
from django.utils.functional import cached_property
from user.models import UserProfile

class Project(models.Model):

    # username = models.ForeignKey(UserProfile ,on_delete= models.CASCADE, default=None)
    project= models.CharField(max_length=50, default="",blank= False)

    def __str__(self):
        return self.project


class LogEntry(models.Model):

    user = models.ForeignKey(UserProfile ,on_delete= models.CASCADE, default=None, related_name='getuser',blank=True, null=True)
    project = models.ForeignKey(Project ,on_delete= models.CASCADE, default=None,related_name='getproject')
    body = models.TextField(blank = True, max_length=100)
    startt = models.DateTimeField()
    endt = models.DateTimeField()

    def __str__(self):
        return 'Dates: {} {}'.format(self.startt, self.endt)
        
    @property    
    def timercount(self):
        timer = self.endt - self.startt
        return timer

        


