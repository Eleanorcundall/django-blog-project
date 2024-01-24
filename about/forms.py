from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Django ModelForm for creating or updating CollaborateRequest instances.

    This form is designed to work with the CollaborateRequest model and includes fields for
    'name', 'email', and 'message'.

    Attributes:
        model (CollaborateRequest): The model associated with the form, which is CollaborateRequest.
        fields (tuple): A tuple specifying the fields to include in the form, including 'name', 'email',
                        and 'message'.

    Note:
        This form is typically used in Django views to handle the creation or updating of
        CollaborateRequest instances through user input.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
