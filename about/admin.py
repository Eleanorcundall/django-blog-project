from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the About model.

    This configuration enhances the Django admin interface for managing About instances,
    particularly focusing on the 'content' field, which is rendered using a rich-text editor.

    Attributes:
        summernote_fields (tuple): A tuple specifying the fields to be rendered using
                                   the Summernote rich-text editor. In this case, it includes 'content'.

    Note:
        The About model represents information about the site or its creator, and this admin
        configuration allows the use of a rich-text editor for editing the 'content' field.
    """
    summernote_fields = ('content',)

    
@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin configuration for CollaborateRequest model.

    This configuration defines the display options for CollaborateRequest instances
    in the Django admin interface.

    Attributes:
        list_display (tuple): A tuple specifying the fields to be displayed in the list view
                             of CollaborateRequest instances. In this case, it includes 'message'
                             and 'read' fields.

    Note:
        The CollaborateRequest model represents requests for collaboration and is
        managed through the Django admin interface with this configuration.
    """

    list_display = ('message', 'read',)