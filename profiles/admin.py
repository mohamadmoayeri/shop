from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin

from .models import User,ads


class  CustomUserAdmin(UserAdmin):
    fieldsets=(
        *UserAdmin.fieldsets,
        ('added_fields',{'fields':('avatar','phone','gender','birthday')})
    )


admin.site.register(User,CustomUserAdmin,list_display=['username','image_tag'],)

admin.site.register(ads)
