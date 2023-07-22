from rest_framework.serializers import ModelSerializer
from abiodoun.work.models import Work


class WorkSerializers(ModelSerializer):

    class Meta:
        model = Work
        fields = '__all__'
