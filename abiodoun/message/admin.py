from django.contrib import admin
from abiodoun.message.models import Message
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class MessageResource(resources.ModelResource):
    class Meta:
        model = Message

class MessageAdmin(ImportExportModelAdmin):
    resource_class = MessageResource

admin.site.register(Message, MessageAdmin)
