from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Această clasă de configurare definește setările aplicației 'api'.
    """
    default_auto_field = 'django.db.models.BigAutoField' # Utilizează BigAutoField ca tip implicit pentru câmpurile auto-generate
    name = 'api' # Numele aplicației
