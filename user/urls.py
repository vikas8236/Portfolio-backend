from django.urls import path
from user.views import UserSignupView, LoginView, LogoutView,  PasswordResetRequestView, PasswordResetConfirmView,ProjectListView, skillsListView, experienceListView,AboutMeListView, SocialMediaListView, ContactListView, EducationListView


app_name = 'user'

urlpatterns = [
    path('register/',UserSignupView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name = 'logout' ),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('projects/', ProjectListView.as_view(), name='project-list'),  # List all projects
    path('projects/<int:id>/', ProjectListView.as_view(), name='project-detail'),  # Fetch specific project by id
    path('skills/', skillsListView.as_view(), name='skills-list'),
    path('skills/<int:id>/', skillsListView.as_view(), name = "skills-detail"),
    path('experience/', experienceListView.as_view(), name='experience-list'),
    path('experience/<int:id>/', experienceListView.as_view(), name = "experience-detail"),
    path('aboutme/', AboutMeListView.as_view(), name='experience-list'),
    path('aboutme/<int:id>/', AboutMeListView.as_view(), name = "experience-detail"),
    path('socialmedia/', SocialMediaListView.as_view(), name='experience-list'),
    path('socialmedia/<int:id>/', SocialMediaListView.as_view(), name = "experience-detail"),
    path('contact/', ContactListView.as_view(), name='experience-list'),
    path('contact/<int:id>/', ContactListView.as_view(), name = "experience-detail"),
    path('education/', EducationListView.as_view(), name='experience-list'),
    path('education/<int:id>/', EducationListView.as_view(), name = "experience-detail"),
    
]