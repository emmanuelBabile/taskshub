from django.apps import AppConfig
from django.core.management import call_command

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'

    def ready(self):
        # Automatically load initial data when the app is ready
        call_command('load_initial_data')