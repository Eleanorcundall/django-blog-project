from django.apps import AppConfig


class AboutConfig(AppConfig):
    """
    Django application configuration for the 'about' app.

    This configuration specifies various settings for the 'about' app, including the default
    auto-generated field type and the app's name.

    Attributes:
        default_auto_field (str): The default auto-generated field type for models in the app.
                                 In this case, it is set to 'django.db.models.BigAutoField'.
        name (str): The name of the app, which is 'about' in this configuration.

    Note:
        The 'about' app likely contains models and functionalities related to site information,
        such as an 'About Me' page, and this configuration provides specific settings for the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'about'