from django.contrib import admin
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User admin."""

    list_display = ('id', 'identification', 'username', 'email',)
    list_display_links = ('id',  'identification', 'username', 'email',)

    search_fields = (
        'email',
        'username',
        'first_name',
        'last_name',
    )

    list_filter = (
        'is_active',
        'is_staff',
    )

    filter_horizontal = ('user_permissions', 'groups',)
