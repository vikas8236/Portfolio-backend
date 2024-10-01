import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from user.models import User, Project, Skill, Experience, AboutMe, SocialMedia, Contact, Education
from rest_framework.authtoken.models import Token

# Fixture to create a test user
@pytest.fixture
def create_user():
    return User.objects.create_user(email="testuser@example.com", password="password123")

@pytest.fixture
def api_client():
    return APIClient()

# Test Registration View
@pytest.mark.django_db
def test_user_signup(api_client):
    url = reverse('register')  
    data = {
        "email": "newuser@example.com",
        "password": "password123",
        "first_name": "Test",
        "last_name": "User"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'Register Successfully' in response.data['message']

# Test Login View
@pytest.mark.django_db
def test_login(api_client, create_user):
    url = reverse('login')  
    data = {
        "email": create_user.email,
        "password": "password123"
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'token' in response.data

# Test Logout View
@pytest.mark.django_db
def test_logout(api_client, create_user):
    token, _ = Token.objects.get_or_create(user=create_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    url = reverse('logout')  
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['message'] == 'Logged out successfully'

# Test Password Reset Request View
@pytest.mark.django_db
def test_password_reset_request(api_client, create_user, mocker):
    mocker.patch('django.core.mail.send_mail', return_value=1)  # Mock email sending
    mocker.patch('user.views.generate_otp', return_value='123456')  # Mock OTP generation

    url = reverse('password-reset-request') 
    data = {"email": create_user.email}
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert 'OTP has been sent to your email.' in response.data['detail']

# Test Project List View
@pytest.mark.django_db
def test_project_list(api_client):
    url = reverse('project-list') 
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test Skills List View
@pytest.mark.django_db
def test_skills_list(api_client):
    url = reverse('skills-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test Experience List View
@pytest.mark.django_db
def test_experience_list(api_client):
    url = reverse('experience-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test About Me List View
@pytest.mark.django_db
def test_aboutme_list(api_client):
    url = reverse('aboutme-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test Social Media List View
@pytest.mark.django_db
def test_socialmedia_list(api_client):
    url = reverse('socialmedia-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test Contact List View
@pytest.mark.django_db
def test_contact_list(api_client):
    url = reverse('contact-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK

# Test Education List View
@pytest.mark.django_db
def test_education_list(api_client):
    url = reverse('education-list')  
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
