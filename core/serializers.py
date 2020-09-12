from rest_framework import serializers
from .models import Airplane
import math

"""
Class: AirplaneSerializer
arguments: serializers.ModelSerializer
note: Serializer Class for model Airplane 
"""

class AirplaneSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Airplane
        fields = '__all__'
        
    ## Move validation to presentaion to hanle type list
    def to_interval_value(self, data):
        # if "passenger" in data:
        #     return data
        
        # data["passenger"] = 0 
        # return data
        pass
    
    """
    Function: handle_many
    Description: This functions handle list and checks passenger field from request data,
           Add passenger field if not found, assigns passenger value from request data
    arguments: request_data, serrialized_data
    return: serialized_data: list=[] 
    """
        
    def handle_many(self, data: list=[], serialized_data: list=[]):
        
        item = [x for x in data
                if x["airplane"] == serialized_data['airplane'] ]
        
        if "passenger" in item[0]:
            serialized_data["passenger"] = item[0]["passenger"]
        else:
            serialized_data["passenger"] = 0
        
        return serialized_data
    
    """
    Function: handle_one
    Description: This functions handle a dict and checks passenger field from request data,
          Add passenger field if not found, assigns passenger value from request data
    arguments: request_data, serialized_data
    return: serialized_data: list=[] 
    """
    
    def handle_one(self, data: dict={}, serialized_data: list=[]):
                
        if "passenger" in data:
            serialized_data["passenger"] = data["passenger"]
        else:
            serialized_data["passenger"] = 0
        
        return serialized_data
    
    """
    Function: get_capacity
    Description: Computes tank capacity as 200 liters * id of the airplane  
    arguments: custom id of airplane
    return: float 
    """    
    
    def get_capacity(self, id_num: int):
        
        return 200 * id_num
        
    """
    Function: get_capacity
    Description: Computes tank consumption as logarithm of the airplane id multiplied by 0.80 liters
                 Each passenger will increase fuel consumption for additional 0.002 liters per minute
    arguments: custom id of airplane(int), number of passenger(int)
    return: float 
    """
    
    def get_consumption(self, id_num: int, passenger: int):
        
        return (math.log(id_num) * 0.08) + (passenger * 0.002)
    
    """
    Function: get_max_mins_fly
    Description: Computes max no of minutes the airplane can fly
    arguments: custom id of airplane(int), number of passenger(int)
    return: float 
    """
    
    def get_max_mins_fly(self, capacity: float, consumption: float):
        
        return capacity / consumption
    
    
    ## override to_presentation for additional details required
    def to_representation(self, data):
            
        # Serialize the airplane object
        serialized_data = super(AirplaneSerializer, self).to_representation(data)
        
        # Include your non-model data
        # I hope I understood clearly the passenger side,
        # Initial solution was passenger field will be added in the model,
        # but as I read through instructions mentioned "passenger assumptions"
        serialized_data["passenger"] = 0
        
        if "request" in self.context:
            if self.context['request'].method != 'GET':            
                request_data = self.context['request'].data
                if isinstance(request_data, list):
                    serialized_data = self.handle_many(request_data, serialized_data)
                else:
                    serialized_data = self.handle_one(request_data, serialized_data)
                   
            
        tank_capacity: float = self.get_capacity(serialized_data["id"])
        tank_consumption: float = self.get_consumption(serialized_data["id"], serialized_data["passenger"])
        max_mins_fly: float = self.get_max_mins_fly(tank_capacity, tank_consumption)
        
        serialized_data["computed_details"] = {
            "tank_capacity" : tank_capacity,            
            "tank_consumption" : tank_consumption,
            "max_mins_fly" : max_mins_fly,
        }
        
        return serialized_data    
