from django.db import models
from datetime import date

class Lunch(models.Model):
    date = models.DateField()
    time = models.TimeField()
    cook = models.CharField(max_length=30)
    meal = models.CharField(max_length=200)
    where = models.CharField(max_length=30)
    
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
        
    def is_today(self):
        return date.today()==self.date
        
    def is_weekend(self):
        return self.date.isoweekday()>5
    
    class Meta:
        ordering = ["date","time"]
        app_label = 'lunch-organizer'
    
    class Admin:
        pass
        