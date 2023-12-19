from django.shortcuts import render,redirect,get_object_or_404
from authentication.models import *
from contracts.models import * 
# Create your views here.
from django.core.serializers import serialize 
from django.db.models import F


# requirements as per the DRF
from rest_framework.mixins import Response
from rest_framework.permissions import *
from rest_framework.viewsets import *
from .serializers import *
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication



#email requirements for activation of these account
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.utils.text import slugify

from datetime import datetime, date, time, timedelta

# used for filtration of the order_by() queries 
from django.db.models import Case, CharField, Value, When


from collections import defaultdict

import uuid

from django.db.models import Sum

import base64
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from datetime import datetime
import urllib
from django.core.files.base import ContentFile

from chat.models import *
from chat.serializers import *
from django.views.generic import (ListView)
from django.core.paginator import Page, Paginator





# Create your views here.
from django.shortcuts import render
from .models import *

def home(request):
    # Assuming you have some logic to get the current participant (authenticated user)
    # current_participant = Participant.objects.get(id=1)  # Replace with your logic

    # # Get all available batches
    # batches = Batch.objects.all()

    # # Get the enrollment details for the current participant
    # enrollment = Enrollment.objects.filter(participant=current_participant).first()

    # # Get the monthly fee details for the current participant's enrollment
    # monthly_fees = MonthlyFee.objects.filter(enrollment=enrollment)

    context = {
        
    }

    return render(request, 'home_yoga.html', context)




class recive_payment(APIView):
    # checking Token From User Is Authenticated Or Not
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def post(self,request):
        print("===================---------------------=========================")
        print(request.data)
        return Response({'error':False})
        




class activate_yoga(APIView):
    def get(self,request,uidb64, token):
        try:
            uid  =urlsafe_base64_decode(uidb64).decode()
            user = Account._default_manager.get(pk=uid)
        except (TypeError ,ValueError,OverflowError,Account.DoesNotExist):
            user = None
            raise
        if user is not None and default_token_generator.check_token(user,token):
            user.is_active=True
            user.save()
            return render(request, 'registration_success.html',{})
        else:     
            return render(request, 'registration_error.html',{})





class register_user(APIView):
    def post(self,request):
        serializers=UserSerializer(data=request.data)
        # print(serializers)
        # print(serializers.error_messages)
        # print(serializers.is_valid())
        # print(request.data['email'])
        # print(serializers.data['email'])

        try:
            # serializers.save()
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            phone_number = request.data['phone_number']
            email = request.data['email']
            dob = request.data['dob'] # needs format as "YYYY-MM-DD"
            password = request.data['password']

            # state_officer= request.data['reg_state_officer']
            username = email.split("@")[0]

            user = Account.objects.create_user_yoga(first_name=first_name,last_name=last_name,email=email,username=username,dob=dob,password=password,)
            user.save()
            user.phone_number=phone_number
            user.save()
            
            au = about_user()
            au.user=user
            au.is_activated=True
            au.save()
            
            # Createthe user profile_form
            profile = UserProfile()
            profile.user_id=user.id
            profile.profile_picture ='default/default-user.png'
            profile.profile_background ='default/default-bg.png'
            profile.save()

            # User Activation
            current_site= get_current_site(request)
            mail_subject = "New Account Activation Verify Your Email "
            context_mail={
                'user': user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            }
            # print(context_mail)
            message = render_to_string('mails/registration_yoga_mail.html',context_mail)
            to_email=email
            send_email=EmailMessage(mail_subject,message,to=[to_email])
            send_email.content_subtype='html'
            send_email.send()
            # print('Done')
            return Response({'error':False})
        except:
        # print('Not Done')
            # raise
            return Response({'error':True})

