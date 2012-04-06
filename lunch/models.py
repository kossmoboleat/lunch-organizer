from django.db import models

class Lunch(models.Model):
    date = models.DateField()
    time = models.TimeField()
    cook = models.CharField(max_length=30)
    meal = models.CharField(max_length=200)
    
    def __str__(self):
        description  = self.cook + " cooks on "
        description += self.date.isoformat()
        description += " at "
        description += self.time.__str__()
        return  description
    
    def str_weekday(self):
        return self.date.strftime("%A") 
    
    def str_date(self):
        return self.date.strftime("%d.%m")
        
    def str_time(self):
        return self.time.strftime("%H:%M")
    
#    def save(self, *args, **kwargs):
#        if self.pk:
#            kwargs['force_update'] = True
#            kwargs['force_insert'] = False
#        else:
#            kwargs['force_insert'] = True
#            kwargs['force_update'] = False
#        return super(Lunch, self).save(*args, **kwargs)
    
    class Meta:
        ordering = ["date","time"]
        app_label = 'lunch-organizer'
    
    class Admin:
        pass
        