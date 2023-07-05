from rest_framework.viewsets import ModelViewSet
from baba.work.models import Work
from baba.work.serializers import WorkSerializers


class WorkViewset(ModelViewSet):
    serializer_class = WorkSerializers
    http_method_names = ['get',  'post']
    lookup_filed = 'slug'

    def get_queryset(self):
        queryset = Work.objects.all().order_by('-created_at')

        slug = self.request.query_params.get('slug')

        if slug is not None:
            queryset = Work.objects.filter(slug=slug)
        
        return queryset
