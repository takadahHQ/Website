from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.forms.widgets import TextInput
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse, reverse_lazy
import secrets

def create_token():
    token = secrets.token_urlsafe(20)
    return token


class Kycs(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    middle_name = models.CharField(max_length=70, blank=True, null=True)
    country_id = models.PositiveIntegerField()
    document_type = models.CharField(max_length=15)
    selfie = models.ImageField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    rejected_reason = RichTextField(blank=True, null=True)
    approved_at = models.DateTimeField(blank=True, null=True)
    rejected_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural =  'kycs'
    
    def __str__(self):
        return self.first_name

class KycDocuments(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    kyc = models.ForeignKey(Kycs, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kyc.first_name +' '+ self.name

    class Meta:
        verbose_name_plural =  'kyc_documents'        


class Languages(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    native_name = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural =  'languages'


class Menus(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    position_choices = (
        ('header', 'Header'),
        ('footer', 'Footer'), 
        )
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100, choices=position_choices, default='header')
    parent_id = models.ForeignKey('Menus', on_delete=models.CASCADE, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    icon = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =  'menus'
    

class Settings(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tagline = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    theme = models.CharField(max_length=255)
    footer = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =  'settings'

class Socials(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =  'socials'


class Transactions(models.Model):
    id = models.BigAutoField(primary_key=True)
    payable_type = models.CharField(max_length=255)
    payable_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wallet = models.ForeignKey('Wallets', models.DO_NOTHING)
    trans_type = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=64, decimal_places=0)
    confirmed = models.IntegerField()
    meta = models.JSONField(blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.amount

    class Meta:
        verbose_name_plural =  'transactions'


class Transfers(models.Model):
    status_choices = (
        ('active', 'Active'),
        ('inactive', 'Inactive'), 
        )
    id = models.BigAutoField(primary_key=True)
    from_type = models.CharField(max_length=255)
    from_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
    to_type = models.CharField(max_length=255)
    to_id = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='reciever', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=status_choices, default='active')
    status_last = models.CharField(max_length=8, blank=True, null=True)
    deposit = models.ForeignKey(Transactions, related_name='deposits', on_delete=models.DO_NOTHING)
    withdraw = models.ForeignKey(Transactions, related_name='withdrawals', on_delete=models.DO_NOTHING)
    discount = models.DecimalField(max_digits=64, decimal_places=0)
    fee = models.DecimalField(max_digits=64, decimal_places=0)
    uuid = models.CharField(unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fee

    class Meta:
        verbose_name_plural =  'transfers'

class CustomUserManager(UserManager):
    def get_by_natural_key(self, username):
        case_insensitive_username_field = '{}__iexact'.format(self.model.USERNAME_FIELD)
        return self.get(**{case_insensitive_username_field: username})

class Users(AbstractUser): 
    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('human', 'Human'), 
        ) 
    kyc_choices = (
        ('pending', 'Pending Submission'),
        ('verification', 'Pending Verification'),
        ('approved', 'Approved'),
        ('declined', 'Declined'),
        )
    pseudonym = models.CharField(max_length=255, blank=True, null=True)
    bio = RichTextField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(max_length=2048, blank=True, null=True)
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    # created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=100, choices=gender_choices, default='human')
    kyc_status = models.CharField(max_length=100, choices=kyc_choices, default='active')
    kyc_verified_at = models.DateTimeField(blank=True, null=True)
    language = models.ForeignKey('Languages', on_delete=models.CASCADE, blank=True, null=True)
    ref_code = models.CharField(max_length=20,  blank=True)
    referrer = models.ForeignKey('Users', on_delete=models.CASCADE, blank=True, null=True)


    objects = CustomUserManager()

    def __str__(self):
        return self.name()

    def save(self, *args, **kwargs):
        if not self.id:
            self.ref_code =  self.referral_code()
        if not self.ref_code:
            self.ref_code=  self.referral_code()
        return super().save(*args, **kwargs)

    def referral_code(self):
        token = secrets.token_urlsafe(3)
        code = "%s%s" % (self.username[0:3], token)
        return code.strip()

    def get_referral_code(self):
        if not self.ref_code:
            self.ref_code=  self.referral_code()
        return self.ref_code

    def get_profile_image(self):
        image = "https://avatars.dicebear.com/api/open-peeps/%s.svg" %(self.username)
        return image

    def following_count(self):
        return self.following.count()

    def followers_count(self):
        return self.followers.count()
        
    def name(self):
        if self.pseudonym:
            return self.pseudonym
        elif self.get_full_name():
            return self.get_full_name()
        else:
            return self.get_username()

    def get_absolute_url(self):
        return reverse_lazy("core:author", kwargs={"username": self.username.lower()})

    class Meta:
        verbose_name_plural =  'users'


class Wallets(models.Model):
    id = models.BigAutoField(primary_key=True)
    holder_type = models.CharField(max_length=255)
    holder_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    uuid = models.CharField(unique=True, max_length=36)
    description = models.CharField(max_length=255, blank=True, null=True)
    meta = models.JSONField(blank=True, null=True)
    balance = models.DecimalField(max_digits=64, decimal_places=0)
    decimal_places = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural =  'wallets'
        unique_together = (('holder_type', 'holder_id', 'slug'),)