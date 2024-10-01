
import pytest
from django.contrib.auth import get_user_model

@pytest.mark.django_db
def test_user_creation():
    User = get_user_model()
    user = User.objects.create_user(email='testuser@example.com', password='password123')
    assert user.email == 'testuser@example.com'
    assert user.check_password('password123') is True

@pytest.mark.django_db
def test_project_creation():
    from user.models import Project
    project = Project.objects.create(
        project_name="Test Project",
        project_link="http://example.com",
        project_description="This is a test project",
        project_stack="Django, React",
        duration="6 months",
        role="Backend Developer"
    )
    assert project.project_name == "Test Project"
    assert project.project_link == "http://example.com"

@pytest.mark.django_db
def test_skill_creation():
    from user.models import Skill
    skill = Skill.objects.create(
        skill_name="Python",
        proficiency_level="Expert",
        category=Skill.TECHNICAL,
        years_of_experience=5.0,
        icon="http://example.com/icon.png",
        project="Test Project",
        last_used="2024",
        description="Python development skills",
        skill_type=Skill.BACKEND
    )
    assert skill.skill_name == "Python"
    assert skill.years_of_experience == 5.0

@pytest.mark.django_db
def test_experience_creation(user):
    from user.models import Experience
    experience = Experience.objects.create(
        job_title="Software Developer",
        company="Tech Corp",
        location="Remote",
        start_date="2020-01-01",
        end_date="2021-12-31",
        is_current=False,
        responsibilities="Developing backend services",
        technologies="Python, Django",
        owner=user
    )
    assert experience.job_title == "Software Developer"
    assert experience.company == "Tech Corp"
@pytest.mark.django_db
def test_aboutme_creation():
    from user.models import AboutMe
    about_me = AboutMe.objects.create(
        name="John Doe",
        bio="A passionate software developer.",
        location="New York, USA",
        linkdin="http://linkedin.com/in/johndoe"
    )
    assert about_me.name == "John Doe"
    assert about_me.bio == "A passionate software developer."
@pytest.mark.django_db
def test_socialmedia_creation():
    from user.models import SocialMedia
    social_media = SocialMedia.objects.create(
        platform_name="LinkedIn",
        platform_url="http://linkedin.com/in/johndoe"
    )
    assert social_media.platform_name == "LinkedIn"
    assert social_media.platform_url == "http://linkedin.com/in/johndoe"
@pytest.mark.django_db
def test_contact_creation():
    from user.models import Contact
    contact = Contact.objects.create(
        name="John Doe",
        email="johndoe@example.com",
        subject="Inquiry about your service",
        message="I am interested in your services. Please contact me."
    )
    assert contact.name == "John Doe"
    assert contact.email == "johndoe@example.com"
@pytest.mark.django_db
def test_education_creation():
    from user.models import Education
    education = Education.objects.create(
        title="Bachelor of Science in Computer Science",
        description="Completed my degree in Computer Science."
    )
    assert education.title == "Bachelor of Science in Computer Science"
    assert education.description == "Completed my degree in Computer Science."
