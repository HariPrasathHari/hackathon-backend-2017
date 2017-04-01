"""

http://127.0.0.1:8000/users/register/
http://127.0.0.1:8000/users/login/
"""
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    CharField,
    EmailField,
    IntegerField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
            # 'first_name',
            # 'last_name',
        ]


class UserCreateSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    # email = EmailField(label='Email Address', write_only=True)
    # email2 = EmailField(label='Confirm Email', write_only=True)
    username = IntegerField(label='Aadhar id')
    pass2 = CharField(label='Confirm password',write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'token',
            # 'email',
            # 'email2',
            'pass2',
            'password',

        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }

    def validate(self, data):
        # email = data['email']
        # user_qs = User.objects.filter(email=email)
        # if user_qs.exists():
        #     raise ValidationError("This user has already registered.")
        return data

    def validate_username(self, value):
        data = self.get_initial()
        username = value
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        # if username.isdigit()!=True:
        #     raise ValidationError("Aadhar field should contain numbers")
        if len(str(username)) != 12:
            raise ValidationError("Aadhar number should be 12 digit")
        print(username, data)
        return value

    def validate_pass2(self, value):
        data = self.get_initial()
        compared = data.get("password")
        pass2 = value
        if compared != pass2:
            return ValidationError("Passwords must match")
        return value


    def create(self, validated_data):
        username = validated_data['username']
        # email = validated_data['email']
        password = validated_data['password']
        pass2 = validated_data['pass2']
        user_obj = User(
            username=username,
            # email=email
        )
        user_obj.set_password(password)
        # user_obj.active=False
        user_obj.save()
        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        validated_data['token'] = token
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    # email = EmailField(label='Email Address')
    class Meta:
        model = User
        fields = [
            'username',
            # 'email',
            'password',
            'token',

        ]
        extra_kwargs = {"password":
                            {"write_only": True},

                        }

    def validate(self, data):
        username = data['username']
        password = data['password']
        user_a = User.objects.filter(username__iexact=username)
        # user_b = User.objects.filter(email__iexact=username)
        # user_qs = (user_a | user_b).distinct()
        user_qs = (user_a).distinct()
        if user_qs.exists() and user_qs.count() == 1:
            user_obj = user_qs.first()  # User.objects.get(id=1)
            password_passes = user_obj.check_password(password)
            if not user_obj.is_active:
                raise ValidationError("This user is inactive")
            # HTTPS
            if password_passes:
                # token
                data['username'] = user_obj.username
                # data['email'] = user_obj.email
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                data['token'] = token
                return data
        raise ValidationError("Invalid credentials")

