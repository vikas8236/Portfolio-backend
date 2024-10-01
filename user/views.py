from user.models import User, Project, Skill, Experience, AboutMe, SocialMedia, Contact, Education
from rest_framework.views import APIView
from rest_framework.response import Response
from user.serializers import UserSerializer, LoginSerializer, PasswordResetRequestSerializer, PasswordResetConfirmSerializer, ProjectsSerializer,SkillsSerializer, ExperienceSerializer, AboutMeSerializer,SocialMediaSerializer, ContactSerializer, EducationSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.mail import send_mail
from rest_framework import generics, status
from rest_framework.response import Response
from .utils import generate_otp
from django.core.cache import cache
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

# Register api
class UserSignupView(APIView):

    def post(self, request, format=None):
        email = request.data.get('email')
        try:
            User.objects.get(email=email)
            return Response('Email already exists')
        except User.DoesNotExist:
            serializer = UserSerializer(data=request.data, context = {"request": request})
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(request.data.get('password'))
                user.save()
                serializer_data = {'message': 'Register Successfully', 'data': serializer.data}
                return Response(serializer_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


import logging

logger = logging.getLogger(__name__)


#  Login api 
class LoginView(APIView):
 
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')
                user = authenticate(email=email, password=password)
                if user:
                    # Generate or fetch existing token for the user
                    token, created = Token.objects.get_or_create(user=user)  # Use Token.objects to create or retrieve tokens
                    return Response({
                        'email': user.email,
                        'message': 'Login Successful',
                        'token': token.key,  # Send the token key to the client
                    }, status=status.HTTP_200_OK)
                else:
                    return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Exception occurred in LoginView: {e}")
            return Response("Internal server error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# logout api
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response({'message': 'Logged out successfully'}, status=200)
    
# reset-password api
class PasswordResetRequestView(generics.GenericAPIView):
    serializer_class = PasswordResetRequestSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "No user is associated with this email address."}, status=status.HTTP_404_NOT_FOUND)
        
        otp = generate_otp()
        print(otp)
        # import pdb; pdb.set_trace()
        cache.set(f'password_reset_otp_{email}', otp, timeout=60)
      

        subject = "Password Reset OTP"
        message = f"Your OTP for password reset is {otp}."
        send_mail(subject, message, 'admin@example.com', [email])

        return Response({"detail": "OTP has been sent to your email."}, status=status.HTTP_200_OK)

class PasswordResetConfirmView(generics.GenericAPIView):
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        new_password = serializer.validated_data['new_password']
        cached_otp = cache.get(f'password_reset_otp_{email}')

        if cached_otp is None or cached_otp != otp:
            return Response({"detail": "Invalid or expired OTP."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "No user is associated with this email address."}, status=status.HTTP_404_NOT_FOUND)
        
        user.set_password(new_password)
        user.save()

        cache.delete(f'password_reset_otp_{email}')

        return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)

class ProjectListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # Fetch the specific project by id
            project = get_object_or_404(Project, id=id)
            serializer = ProjectsSerializer(project)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all projects
            projects = Project.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
class skillsListView(APIView):
    def get(self, request, id=None):
        # Check if a specific skill ID is provided
        if id is not None:
            skill = get_object_or_404(Skill, id=id)
            serializer = SkillsSerializer(skill)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        # Check for category in query parameters (technical/other)
        category = request.query_params.get('category', None)
        
        if category in [Skill.TECHNICAL, Skill.OTHER]:
            skill_list = Skill.objects.filter(category=category)
        else:
            skill_list = Skill.objects.all()
        
        serializer = SkillsSerializer(skill_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class experienceListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # If an id is provided, retrieve the specific experience
            exp = Experience.objects.get(id=id)
            serializer = ExperienceSerializer(exp)
            return Response(serializer.data)
        else:
            # If no id is provided, retrieve all experience
            exp_list = Experience.objects.all()
            serializer = ExperienceSerializer(exp_list, many=True)
            return Response(serializer.data)

class AboutMeListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # Fetch the specific project by id
            about_me = get_object_or_404(AboutMe, id=id)
            serializer = AboutMeSerializer(about_me)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all projects
            about_me_all = AboutMe.objects.all()
            serializer = AboutMeSerializer(about_me_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)        



class SocialMediaListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # Fetch the specific project by id
            social_media = get_object_or_404(SocialMedia, id=id)
            serializer = SocialMediaSerializer(social_media)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all projects
            social_media_all = SocialMedia.objects.all()
            serializer = SocialMediaSerializer(social_media_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)         

class ContactListView(APIView):
    def get(self, request, id=None):
        if id is not None:
            # Fetch the specific contact by id
            contact_one = get_object_or_404(Contact, id=id)
            serializer = ContactSerializer(contact_one)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all contacts
            contact_all = Contact.objects.all()
            serializer = ContactSerializer(contact_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new contact
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new contact to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        
class EducationListView(APIView):   
    def get(self, request, id=None):
        if id is not None:
            # Fetch the specific project by id
            educaton = get_object_or_404(Education, id=id)
            serializer = EducationSerializer(educaton)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Fetch all projects
            education_all = Education.objects.all()
            serializer = EducationSerializer(education_all, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)           