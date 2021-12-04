from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from henri.work.models import Work
from henri.work.serializers import WorkSerializers


class WorkViewset(ModelViewSet):
    serializer_class = WorkSerializers
    http_methods = ['get',  'post']
    lookup_filed = 'slug'

    def get_queryset(self):
        queryset = Work.objects.all().order_by('-created_at')

        slug = self.request.query_params.get('slug')

        if slug is not None:
            queryset = Work.object.filter(slug=slug)
        
        return queryset
    
