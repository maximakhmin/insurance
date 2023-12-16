from .models import UserPolicy
from rest_framework import serializers

class UserPolicySerializer(serializers.ModelSerializer):
    policy_type = serializers.CharField(source='policy_id.type')
    policy_description = serializers.CharField(source='policy_id.description')

    class Meta:
        model = UserPolicy
        fields = ['policy_type', 'policy_description','cost', 'payment']