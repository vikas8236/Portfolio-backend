import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager
class BaseModel(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)

    class Meta:
        abstract = True
# API for User Authentication
class User(AbstractUser, BaseModel):
    username = None
    email = models.EmailField(unique = True, max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    profileImg = models.URLField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email
# API for Projects Section
class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_link = models.URLField()
    project_description = models.TextField(max_length=500)
    project_stack = models.TextField(max_length=500)
    duration = models.CharField(max_length=30)
    role = models.CharField(max_length=50)
    
    def __str__(self):
        return self.project_name
# API for Skills Section    
class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    Proficiency_level = models.CharField(max_length=40)
    category = models.CharField(max_length=50)
    years_of_experience = models.DecimalField(max_digits=2, decimal_places=1)
    icon = models.URLField()
    project_name = models.ManyToManyField(Project)
    last_used = models.CharField(max_length=10)
    description = models.TextField(max_length=1000)
    skill_type = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.skill_name

# API for Experience Section
class Experience(models.Model):
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_current = models.BooleanField(default=False)
    responsibilities = models.TextField()
    technologies = models.CharField(max_length=500, blank=True)
    achievements = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=100, blank=True, null=True)
    reference_links = models.URLField(blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.job_title} at {self.company}"
# API for About Me Section    
class AboutMe(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='images', null=True, blank= True)
    bio = models.TextField(max_length=500)
    location = models.CharField(max_length=100)
    linkdin = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.name