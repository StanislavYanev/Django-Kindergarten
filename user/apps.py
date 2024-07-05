from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'


class TestConfig(AppConfig):
    name = 'Teacher'
    default_auto_field = 'django.db.models.BigAutoField'

class ChildConfig(AppConfig):
    name = 'Child'
    default_auto_field = 'django.db.models.BigAutoField'

class Childrens_groupConfig(AppConfig):
    name = 'Childrens_group'
    default_auto_field = 'django.db.models.BigAutoField'

