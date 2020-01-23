from django.contrib import admin
from rbac import models
# Register your models here.
admin.site.register(models.UserProfile)
admin.site.register(models.Permission)
admin.site.register(models.Organization)
admin.site.register(models.Role)
admin.site.register(models.Menu)

