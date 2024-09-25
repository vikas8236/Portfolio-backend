from django.contrib import admin
from user.models import Skill, Project, User, Experience, AboutMe, SocialMedia, Contact, Education
admin.site.register(User)

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'role']
    search_fields = ['project_name']
admin.site.register(Project, ProjectsAdmin)

class SkillsAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'category', 'years_of_experience']
    search_fields = ['skill_name', 'category', 'years_of_experience']
admin.site.register(Skill, SkillsAdmin )

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['job_title', 'company']
    search_fields = ['job_title', 'company']
admin.site.register(Experience, ExperienceAdmin)

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'linkdin']
    search_fields = ['name']
admin.site.register(AboutMe, AboutMeAdmin)

class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform_name', 'platform_url']
    search_fields = ['platform_name']
admin.site.register(SocialMedia, SocialMediaAdmin)

class ContatAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    search_fields = ['name','email']
admin.site.register(Contact, ContatAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
admin.site.register(Education, EducationAdmin)


