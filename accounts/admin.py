from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    change_form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email"]
    
    search_fields = ['email']
    ordering = ('-date_joined',)


admin.site.register(CustomUser, CustomUserAdmin)

