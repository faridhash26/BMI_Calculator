from django.db import models
from utils.base_model import BaseModel

from user.models import BMIUser
# Create your models here.

class UserBmiInfo(BaseModel):
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    age = models.IntegerField()
    user  = models.ForeignKey(BMIUser, on_delete=models.SET_NULL, blank=True, null=True,related_name='valid_question')
    bmi= models.DecimalField(max_digits=3, decimal_places=1 ,blank=True, null=True)
    STATUS_TYPE_CHOICES = (
        ('Underweight', 'UNDERWEIGHT'),
        ('Normal', 'NORMAL',),
        ('Overweight', 'OVERWEIGHT'),
        ('Obese', 'OBESE')
    )
    status= models.CharField(choices=STATUS_TYPE_CHOICES, max_length=15)

    def __str__(self):
        return f'{self.user.name}'
    
    @property 
    def get_status(self):
        if self.bmi:
            if self.bmi <= 18.5:
                return "Underweight"
            if 18.5< self.bmi <=24.9:
                return "Normal"
            if 25.0<= self.bmi <=30:
                return "Overweight"
            if 30.0 <self.bmi :
                return "Obese"
            return None

    def save(self, *args, **kwargs):
        self.status = self.get_status
        super(UserBmiInfo, self).save(*args, **kwargs)


