from django.db import models
from django.utils.functional import cached_property

class Project(models.Model):

    project= models.CharField(max_length=50, default="",blank= False)

    def __str__(self):
        return self.project


class LogEntry(models.Model):

    project = models.ForeignKey(Project ,on_delete= models.CASCADE, default=None)
    body = models.TextField(blank = True, max_length=100)
    startt = models.DateTimeField()
    endt = models.DateTimeField()

    def __str__(self):
        return 'Dates: {} {}'.format(self.startt, self.endt)
        
    @property    
    def timercount(self):
        timer = self.endt - self.startt
        return timer

        


