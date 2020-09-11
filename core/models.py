from django.db import models

# Create your models here.

"""
Class: Airplane
arguments: Model
note: 
"""
class Airplane(models.Model):
    
    airplane = models.CharField(max_length=100, primary_key=True)
    id = models.IntegerField()
    # passenger = models.IntegerField()
    
    def __str__(self):
        return self.airplane
    
    ## moving to serializers
    # def _get_capacity_(self):
    #     "Returns tank capacity"
        
    #     return 200 * self.id

    # tank_capacity = property(_get_capacity_)
        
    # def _get_consumption_per_min_(self):
    #     "Returns tank consumption"
         
    #     return (math.log(self.id) * 0.08) + (self.passenger * 0.002)
    
    # tank_consumption = property(_get_consumption_per_min_)
    
    # def _get_max_min_(self):
    #     "Returns max minutes able to fly"
         
    #     return self.tank_capacity / self.tank_consumption 

    # max_mins_fly = property(_get_max_min_)
