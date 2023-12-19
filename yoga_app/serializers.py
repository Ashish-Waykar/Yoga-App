from rest_framework import serializers

from authentication.models import Account,UserProfile

from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import *
from contracts.models import *

from chat.models import *
# class TestSerializers(serializers.ModelSerializer):
#     class Meta:
#         model=quiz_test
#         fields=(
#             "test_id",
#             "title",
#             "subtitle",
#             "description",
#             "test_thumbnail",
#             "created_on",
#             "expiring_on",
#             "is_active",
#             "is_shuffled",
#             "total_marks",
#             "test_from_timefield",
#             "test_time",
#             "is_marks_disclosed"
#         )

class userMessageModelSerializer(serializers.ModelSerializer):
    # products = ContractImages(many=True)

    class Meta:
        model = MessageModel
        fields = '__all__'
        depth=2

    def to_representation(self, obj):
        rep = super(userMessageModelSerializer, self).to_representation(obj)

        rep.get('recipient').pop('password',None)
        rep.get('sender').pop('password',None)
        # rep.get('follow_s_user_profile').pop('user__password',None)
        
        return rep
    
class userFollowlistSerializer(serializers.ModelSerializer):
    # products = ContractImages(many=True)

    class Meta:
        model = userFollowlist
        fields = '__all__'
        depth=2

    def to_representation(self, obj):
        rep = super(userFollowlistSerializer, self).to_representation(obj)

        rep.get('user_self').pop('password',None)
        rep.get('follow_s').pop('password',None)
        # rep.get('follow_s_user_profile').pop('user__password',None)
        
        return rep
    


class ContractImagesSerializer(serializers.ModelSerializer):
    # products = ContractImages(many=True)

    class Meta:
        model = ContractImages
        fields = '__all__'

class PatchSerializer(serializers.Serializer):
    # Define your PatchSerializer fields
    id = serializers.IntegerField()
    # Add more fields as needed

class BillWithPatchesSerializer(serializers.Serializer):
    bill = serializers.JSONField()
    bill_patches = PatchSerializer(many=True)

class ContractImagesSerializer(serializers.Serializer):
    # Define your ContractImagesSerializer fields
    id = serializers.IntegerField()
    # Add more fields as needed

class UserDashboardSerializer(serializers.Serializer):
    patches = PatchSerializer(many=True)
    Contract = serializers.JSONField()
    ContractImages = ContractImagesSerializer(many=True)
    client_details = serializers.JSONField()
    billing = BillWithPatchesSerializer(many=True)

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "email", "dob", "password")

        # extra_kwargs={'password':{"write_only":True,'required':True}}


class UserDetailsSerialiser(serializers.ModelSerializer):
    password = serializers.HiddenField(default='')
    class Meta:
        # model=Account
        model=UserProfile
        # fields=('user','address_line_1','address_line_2','profile_picture','city','state','country', 'LocationLink')
        fields="__all__"
        # exclude = ['user__password'] 
        depth=1
    def to_representation(self, obj):
        rep = super(UserDetailsSerialiser, self).to_representation(obj)
        # rep.pop('id', None)
        rep.pop('datetime', None)
        rep.get('user').pop('password',None)
        # rep.get('user').pop('id',None)
        rep.get('user').pop('datetime',None)
        rep.get('user').pop('date_time',None)
        rep.get('user').pop('date_joined',None)
        rep.get('user').pop('last_login',None)
        return rep

