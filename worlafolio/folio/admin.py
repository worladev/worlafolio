from django.contrib import admin
from folio.models import User, Projects, Education, Experience


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'headline']

admin.site.register(Projects)

admin.site.register(Education)

admin.site.register(Experience)
