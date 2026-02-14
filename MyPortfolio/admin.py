from django.contrib import admin
from .models import portfolios, Project


@admin.register(portfolios)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'phone')
    search_fields = ('user__username', 'full_name', 'email')
    list_filter = ('user',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    search_fields = ('title', 'user__username')
    list_filter = ('user',)
