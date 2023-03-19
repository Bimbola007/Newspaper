from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','is_staff','username','age']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('age',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields':('age', 'email',)}),)


admin.site.register(CustomUser,CustomUserAdmin)
