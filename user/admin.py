from django.contrib import admin
from user.models import Skill, Project, User, Experience, AboutMe
admin.site.register(User)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_name', 'role']
    search_fields = ['project_name']
admin.site.register(Project, ProjectsAdmin)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(AboutMe)


