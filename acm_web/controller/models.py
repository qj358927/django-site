from django.db import models

# Create your models here.
class Visits(models.Model):
    numVisits = models.IntegerField()
    pageName = models.CharField(max_length=200)
    
    def getVisits(self):
        return self.numVisits;
    
    def incVisits(self):
        self.numVisits = self.numVisits + 1

    @staticmethod
    def incrementVisitCount(pName):
        view = Visits.objects.filter(pageName = pName)
        if view.count() == 0:
            v = Visits(pageName=pName, numVisits=1)
            v.save()
        else:
            v = view[0]
            v.incVisits()
            v.save()
        return v.numVisits;

