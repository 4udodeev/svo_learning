from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    BasePosition, CurrentStates, Employee, Mvz, Organization,
    Position, PositionCategory, PositionTypeOfWork, Subdivision
)


UserAdmin.fieldsets += (
    (
        'Персональные данные',
        {'fields': (
            'middle_name',
            'sex',
            'birth_date',
            'photo',
            'passport',
            'driver_license',
            'education',
            'comment',
        )}
    ),
    (
        'Данные о работнике',
        {'fields': (
            'code',
            'hire_date',
            'is_candidate',
            'is_dismiss',
            'dismiss_date',
            'is_banned',
        )}
    )
)


admin.site.register(BasePosition)
admin.site.register(CurrentStates)
admin.site.register(Employee, UserAdmin)
admin.site.register(Mvz)
admin.site.register(Organization)
admin.site.register(Position)
admin.site.register(PositionCategory)
admin.site.register(PositionTypeOfWork)
admin.site.register(Subdivision)
