from django.test import TestCase
import json
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient
from .serializers import AirplaneSerializer
from .models import Airplane
import math


# Create your tests here.
class AirplaneTest(TestCase):
    """ Test module for Airplane model """

    def setUp(self):
        Airplane.objects.create(
            airplane='ap1', id=3)
        Airplane.objects.create(
            airplane='ap2', id=2)

    def test_airplane_id(self):
        ap1 = Airplane.objects.get(airplane='ap1')
        ap2 = Airplane.objects.get(airplane='ap2')
        self.assertEqual(ap1.id, 3)
        self.assertEqual(ap2.id, 2)


class AirplaneDRFTest(APITestCase):
    """ Test module for GET all Airplane API """

    client = RequestsClient()

    def setUp(self):
        # Airplane.objects.create(
        #     airplane='airplane1', id=1)
        Airplane.objects.create(
            airplane='airplane2', id=2)
        Airplane.objects.create(
            airplane='airplane3', id=3)
        Airplane.objects.create(
            airplane='airplane4', id=4)
        Airplane.objects.create(
            airplane='airplane5', id=5)

    def test_get_all_airplanes(self):
        # get API response
        url = 'http://127.0.0.1:8000/api/airplane/'
        response = self.client.get(url)
        # get data from db
        planes = Airplane.objects.all()
        serializer = AirplaneSerializer(planes, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_create_airplanes(self):
        # get API response
        data = [
            {
                "airplane": "sample1",
                "id": 2
            },
            {
                "airplane": "sample2",
                "id": 2
            },
            {
                "airplane": "sample3",
                "id": 2
            },
            {
                "airplane": "sample4",
                "id": 2
            },
            {
                "airplane": "sample5",
                "id": 2,
                "passenger": 1
            },
            {
                "airplane": "sample6",
                "id": 4,
                "passenger": 2
            }
        ]
        url = 'http://127.0.0.1:8000/api/airplane/'
        response = self.client.post(url, data=data, format='json')  
        # get data from db
        planes = Airplane.objects.filter(airplane__in=['sample1', 'sample2', 
                                                       'sample3', 'sample4', 
                                                       'sample5', 'sample6'])
        serializer = AirplaneSerializer(planes, many=True)
        self.assertEqual(len(response.data), len(serializer.data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
        for airplane in response.data:
            computed_details = airplane.get('computed_details')
            
            capacity = 200 * airplane.get('id')
            consumption = (math.log(airplane.get('id')) * 0.08) + (airplane.get('passenger') * 0.002)
            max_mins_fly = capacity / consumption
            
            self.assertEqual(computed_details['tank_capacity'], capacity)
            self.assertEqual(computed_details['tank_consumption'], consumption)
            self.assertEqual(computed_details['max_mins_fly'], max_mins_fly)
            
