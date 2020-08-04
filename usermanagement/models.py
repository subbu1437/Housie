from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from Housie.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, email, mobile, password, cast):
        user = self.model(username=mobile, email=email, mobile=mobile, password=password, cast=cast)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, password):
        user = self.create_user(email="", mobile=mobile, password=password, cast="staff")
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class HUser(AbstractUser):
    name = models.CharField(max_length=32)
    email = models.EmailField(null=True)
    mobile = models.CharField(max_length=10, unique=True)
    cast = models.CharField(max_length=16)
    fcmtoken = models.CharField(max_length=256, null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'mobile'

    class Meta:
        db_table = 'user'
class GameWallet(BaseModel):
    amount=models.FloatField(default=0)
    user_id=models.ForeignKey(HUser,on_delete=models.PROTECT)
class GameWalletTransaction(BaseModel):
    wallet_id=models.ForeignKey(GameWallet,on_delete=models.PROTECT)
    amount=models.FloatField(default=0)
    payment_type = models.CharField(max_length=16, null=True)  # won,loss
    payment_ref_id = models.TextField()
    payment_details = models.TextField()
    response_status = models.CharField(max_length=128)
    payment_made_on = models.DateTimeField(null=True)
    remarks=models.CharField(max_length=90)
class Wallet(BaseModel):
    amount = models.FloatField(default=0)
    user_id = models.ForeignKey(HUser, on_delete=models.PROTECT)
class WalletTransaction(BaseModel):
    wallet_id = models.ForeignKey(Wallet, on_delete=models.PROTECT)
    amount = models.FloatField(default=0)
    payment_type = models.CharField(max_length=16, null=True)  # credit, debit
    payment_ref_id = models.TextField()
    payment_details = models.TextField()
    response_status = models.CharField(max_length=128)
    payment_made_on = models.DateTimeField(null=True)
    remarks = models.CharField(max_length=90)