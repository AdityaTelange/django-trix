from trix.models import Attachment
from trix.widgets import TrixEditor
from django.contrib import admin


class TrixAdmin(object):

    def formfield_for_dbfield(self, db_field, **kwargs):

        if not hasattr(self, 'trix_fields'):
            raise ValueError('trix_fields is required on model')

        if db_field.name in self.trix_fields:
            return db_field.formfield(widget=TrixEditor())
        return super(TrixAdmin, self).formfield_for_dbfield(db_field, **kwargs)


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'file', 'uploaded_at')
    list_filter = ("uploaded_at",)
    search_fields = ['title', ]


admin.site.register(Attachment, AttachmentAdmin)
