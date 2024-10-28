from django.contrib import admin
from abiodoun.work.models import Work
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class WorkResource(resources.ModelResource):

    class Meta:
        model = Work

class WorkAdmin(ImportExportModelAdmin):
    resource_class = WorkResource

admin.site.register(Work, WorkAdmin)

