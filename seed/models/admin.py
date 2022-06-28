"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Process
from app.models import User
from app.models import File

class Admin:
    # pylint: disable=R0914,R0915
    @staticmethod
    def register():
        
        class ProcessResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Process
                fields = (
                    'id',
                    'created_at',
                    'n',
                    'k',
                    'result',
                    'user_id',
                )

        class ProcessAdmin(ImportExportModelAdmin):
            resource_class = ProcessResource
        
        class UserResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                )

        class UserAdmin(ImportExportModelAdmin):
            resource_class = UserResource
        
        class FileResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = File
        class FileAdmin(ImportExportModelAdmin):
            resource_class = FileResource
        admin.site.register(Process, ProcessAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)