from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer,CharField,ValidationError
class UserSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'password',
            'confirm_password'
        ]
        extra_kwargs = {
            'confirm_password':{
                'write_only':True
            }
        }
    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError("Account Already Exists For Given Mail Address")
        elif User.objects.filter(username=attrs['username']).exists():
            raise ValidationError("Username Already In Use")
        elif attrs['password'] != attrs['confirm_password']:
            raise ValidationError("Passwords Do Not Match")
        else:
            return attrs
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user