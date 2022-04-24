from rest_framework import generics , status
from rest_framework.response import Response

from .utils import get_location
from .serializers import CreateLocationSerializer, LocationsSeraizlier , LocationDetailSerializer
from .models import Incidences


class LocationAPIView(generics.ListAPIView):
    serializer_class = LocationsSeraizlier

    def get_queryset(self):
        qs = Incidences.objects.all()
        return qs
    
    def get(self, request, *args, **kwargs):
        try :
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        except :
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')
        

class LocationDetailsAPIView(generics.RetrieveAPIView):
    serializer_class = LocationDetailSerializer
    
    def get_object(self):
        return self.kwargs.get('pk')
    
    def get_queryset(self):
        id = self.get_object()
        qs = Incidences.objects.filter(id=id)
        return qs

    def get(self, request, *args, **kwargs):
        try :
            
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='nothing found')


class CreateLocationAPIView(generics.CreateAPIView):
    serializer_class = CreateLocationSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if not serializer.is_valid():
                return Response(status=status.HTTP_400_BAD_REQUEST, data='All Fields Must Be Full')
            name = request.data['name']
            x = request.data['location_x']
            y = request.data['location_y']
            location = get_location(x=x,y=y)
            Incidences.objects.create(name=name, location=location)
            return Response(status=status.HTTP_200_OK, data='Done')
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data='Failed')
            