from rest_framework import serializers
from user.models import User, Project,Skill, Experience
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("id", "first_name", "last_name", "email", "mobile_no", "password", "profileImg")
        extra_kwargs = {
            "email": {"validators": []},
            "first_name": {"required": True},
            "last_name": {"required": True}
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model = User
        fields = ['email', 'password'] 
     
    def validate(self, attrs):
        email = attrs.get("email", "")
         
        if email == "":
            raise serializers.ValidationError("Email is required")
            
        return super().validate(attrs)

class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PasswordResetConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)
    new_password = serializers.CharField(write_only=True)
    re_new_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['re_new_password']:
            raise serializers.ValidationError("The two password fields didn't match.")
        return data
    
class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name', 'project_description','project_link','project_stack', 'duration', 'role', ]
        
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
            