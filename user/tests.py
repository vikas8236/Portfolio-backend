# from django.test import TestCase

# from django.test import TestCase
# from .models import Project, Skill, Experience, AboutMe, SocialMedia, Contact, Education
# from django.contrib.auth.models import User

# class ProjectModelTestCase(TestCase):
#     def setUp(self):
#         self.project = Project.objects.create(
#             project_name="Test Project",
#             project_link="http://example.com",
#             project_description="This is a test project.",
#             project_stack="Python, Django",
#             duration="3 months",
#             role="Developer"
#         )

#     def test_project_string_representation(self):
#         self.assertEqual(str(self.project), "Test Project")

# class SkillModelTestCase(TestCase):
#     def setUp(self):
#         self.skill = Skill.objects.create(
#             skill_name="Python",
#             proficiency_level="Expert",
#             years_of_experience=5.0,
#             icon="http://example.com/icon.png",
#             last_used="2024-09-25",
#             description="Python programming skills.",
#             project="Test Project"
#         )

#     def test_skill_string_representation(self):
#         self.assertEqual(str(self.skill), "Python")

# class ExperienceModelTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='123456')
#         self.experience = Experience.objects.create(
#             job_title="Software Engineer",
#             company="Tech Company",
#             location="New York",
#             start_date="2022-01-01",
#             end_date="2023-01-01",
#             is_current=False,
#             responsibilities="Developing applications.",
#             technologies="Python, Django",
#             achievements="Successfully launched a product.",
#             experience_level="Mid-Level",
#             reference_links="http://example.com",
#             owner=self.user
#         )

#     def test_experience_string_representation(self):
#         self.assertEqual(str(self.experience), "Software Engineer at Tech Company")

# class AboutMeModelTestCase(TestCase):
#     def setUp(self):
#         self.about_me = AboutMe.objects.create(
#             name="John Doe",
#             bio="A passionate developer.",
#             location="Remote",
#             linkdin="http://linkedin.com/in/johndoe"
#         )

#     def test_about_me_string_representation(self):
#         self.assertEqual(str(self.about_me), "John Doe")

# class SocialMediaModelTestCase(TestCase):
#     def setUp(self):
#         self.social_media = SocialMedia.objects.create(
#             platform_name="LinkedIn",
#             platform_url="http://linkedin.com/in/johndoe"
#         )

#     def test_social_media_string_representation(self):
#         self.assertEqual(str(self.social_media), "LinkedIn")

# class ContactModelTestCase(TestCase):
#     def setUp(self):
#         self.contact = Contact.objects.create(
#             name="John Doe",
#             email="john.doe@example.com",
#             subject="Inquiry",
#             message="This is a test message."
#         )

#     def test_contact_string_representation(self):
#         self.assertEqual(str(self.contact), "John Doe")

# class EducationModelTestCase(TestCase):
#     def setUp(self):
#         self.education = Education.objects.create(
#             title="Bachelor of Science",
#             description="A degree in computer science."
#         )

#     def test_education_string_representation(self):
#         self.assertEqual(str(self.education), "Bachelor of Science")
