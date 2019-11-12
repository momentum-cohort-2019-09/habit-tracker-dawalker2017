from django.contrib import admin
from core.models import User, Log, Habit

class HabitInLine(admin.TabularInline):
    model = Habit
    extra = 0

class LogInLine(admin.TabularInline):
    model = Log
    extra = 0

class LogAdmin(admin.ModelAdmin):
    list_display = (
        'subject',
        'number_of_habits',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'subject',
        'is_active',
    )

class HabitAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'title',
    )

class UserAdmin(admin.ModelAdmin):
    inlines = [
        LogInLine,
    ]
    
admin.site.register(Log, LogAdmin)
admin.site.register(Habit, HabitAdmin)
admin.site.register(User, UserAdmin)