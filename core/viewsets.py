from rest_framework import viewsets
from .serializers import AirplaneSerializer
from .models import Airplane

"""
Class: CreateListModelMixin
arguments: object
note: Mixin that allows to create multiple objects from lists
"""

class CreateListModelMixin(object):

    def get_serializer(self, *args, **kwargs):
        """ if an array is passed, set serializer to many """
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)

"""
Class: AirplaneViewSet
arguments: CreateListModelMixin, viewsets.ModelViewSet
note: Added CreateListModelMixin for accepting List for API request
"""

class AirplaneViewSet(CreateListModelMixin, viewsets.ModelViewSet):
    queryset = Airplane.objects.all().order_by('id')
    serializer_class = AirplaneSerializer
