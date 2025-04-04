from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
["from rest_framework.authtoken.models import Token", "Token.objects.create", "get_user_model().objects.create_user"]

class RegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only = True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
    
    def validate(self, attrs):
        # attrs (attributes) contain the cleaned data, it returns the data after field-level validation.
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({'Error': 'password do not match'})
        return super().validate(attrs)
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        return data

class CustomUserSerializer(serializers.ModelSerializer):
    following = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'bio', 'followers', 'following']

    # def validate(self, attrs):
    #     current_user_id = self.context['request'].user.id
    #     print("in here")
    #     user_id = attrs.get('id')
    #     print(current_user_id, user_id)
    #     if current_user_id != user_id:
    #         raise ValidationError(message={'id': 'You\'re not permitted to modify this details, only the owner can!'})
    #     print(super().validate(attrs))
    #     return super().validate(attrs)  
  