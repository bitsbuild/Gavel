from rest_framework.serializers import CharField,ModelSerializer,ValidationError
from django.contrib.auth.models import User
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        feilds = [
            'email',
            'username',
            'password',
            'confirm_password'
        ]
        extra_kwargs = {
            'password':{
                'write_only':True
            }
        }
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError('Account With This Email Exists!')
        elif User.objects.filter(username=attrs['username']).exists():
            raise ValidationError('Account With This Username Exists!')
        elif attrs['password'] != attrs['confirm_password']:
            raise ValidationError('Passwords Do Not Match!')
        else:
            return attrs
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user_instance = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user_instance.set_password(validated_data['password'])
        user_instance.save()
        return user_instance
        