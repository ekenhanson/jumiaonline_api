from rest_framework import serializers
from .models import CustomUser, InvitationCode
from .models import CustomUser


class InvitationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCode
        fields = '__all__'


from rest_framework import serializers
from .models import CustomUser, InvitationCode

class InvitationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvitationCode
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    invitationCode = serializers.CharField(write_only=True, required=True)
    invitationCode_display = InvitationCodeSerializer(source='invitationCode', read_only=True)
    user_type = serializers.CharField(default='client')
    level = serializers.CharField(default='VIP1')

    class Meta:
        model = CustomUser
        fields = "__all__"

        fields = ["id", "firstName", "lastName", "phone", "password", "level", "balance", "invitationCode","commission1","commission2",
                   "unsettle","withdrawalPassword", "date_joined", "grabbed_orders_count", "invitationCode_display", "user_type"]  # Adjust the fields based on what's needed
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        invitation_code = validated_data.pop('invitationCode')
        try:
            code_instance = InvitationCode.objects.get(code=invitation_code, is_used=False)
        except InvitationCode.DoesNotExist:
            raise serializers.ValidationError({'invitationCode': 'Invalid or already used invitation code'})

        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.invitationCode = code_instance
        user.save()

        # Mark the invitation code as used
        code_instance.is_used = True
        code_instance.save()

        return user



class PasswordResetSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, required=True, min_length=8)

    def validate_new_password(self, value):
        # You can add custom validation here
        return value
