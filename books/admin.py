from django.contrib import admin

# Register your models here.

from import_export import resources
from .models import Book,Category,Author

from import_export.admin import ImportExportModelAdmin

class BookResource(resources.ModelResource):

    class Meta:
        model = Book


class BookAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Author)	
admin.site.register(Category)	
admin.site.register(Book,BookAdmin)	
