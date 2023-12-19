from django.db import models
from authentication.models import * 



class Participant(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE, null=True, blank=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True, blank=True)

class Enrollment(models.Model):
    batches={
        ('6-7AM', '6-7AM'),
        ('7-8AM', '7-8AM'),
        ('8-9AM', '8-9AM'),
        ('5-6PM', '5-6PM'),
    }
    user= models.ForeignKey(Account,on_delete=models.CASCADE, null=True, blank=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    selected_batch = models.CharField(max_length=100,null=True,blank=True)
    payment_status = models.BooleanField(default=False)
    datetime=models.DateTimeField(auto_now_add=True,null=True, blank=True)
    last_datetime=models.DateTimeField(auto_now=True,null=True, blank=True)


class MonthlyFee(models.Model):
    user= models.ForeignKey(Account,on_delete=models.CASCADE, null=True, blank=True)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE,null=True,blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=500.00,null=True,blank=True)
    paid_date = models.DateField(auto_now=True,null=True, blank=True)
    datetime=models.DateTimeField(auto_now_add=True,null=True, blank=True)

class PaymentInformation(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE,null=True,blank=True)
    batch_yoga = models.CharField(max_length=255,null=True,blank=True)  # Assuming batchYoga is a string field

    full_name = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    DD = models.CharField(max_length=2,null=True,blank=True)
    MM = models.CharField(max_length=2,null=True,blank=True)
    YYYY = models.CharField(max_length=4,null=True,blank=True)
    
    gender = models.CharField(max_length=10,null=True,blank=True)

    card_number = models.CharField(max_length=16,blank=True,null=True)
    card_cvc = models.CharField(max_length=3,blank=True,null=True)
    expiry_month = models.CharField(max_length=2,blank=True,null=True)
    expiry_year = models.CharField(max_length=4,blank=True,null=True)