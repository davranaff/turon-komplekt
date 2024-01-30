from django.contrib import admin
from app.models import Info, Project, FeedBack, Objects, Branch, Certificate, Trust


# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ['title_ru']
    search_fields = ['title_ru']
    list_filter = ['title_ru']

    class Meta:
        model = Info


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name_ru']
    search_fields = ['name_ru']
    list_filter = ['name_ru']

    class Meta:
        model = Project


admin.site.register(Info, InfoAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Branch)
admin.site.register(Certificate)
admin.site.register(FeedBack)
admin.site.register(Objects)
admin.site.register(Trust)
