from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Company_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companyName = models.CharField(max_length=200, blank=False)
    companyRegNum = models.CharField(max_length=30, blank=True)
    contactPerson = models.CharField(max_length=100, blank=False)
    contactNumber = models.CharField(max_length=20, blank=False)
    emailAddress = models.CharField(max_length=100, blank=False)
    companyAddress = models.TextField(max_length=500, blank=True)

    #below are the details of the person that handles billing.
    billingContactPerson = models.CharField(max_length=100, blank=False)
    billingContactNumber = models.CharField(max_length=20, blank=False)
    billingEmailAddress = models.CharField(max_length=100, blank=False)


@receiver(post_save, sender=User)
def create_company_profile(sender, instance, created, **kwargs):
    if created:
        Company_Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_company_profile(sender, instance, **kwargs):
    instance.company_profile.save()


'''from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _



class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username    = models.CharField(max_length=254, unique=True)
    first_name  = models.CharField(max_length=254, unique=True)
    last_name   = models.CharField(max_length=254, unique=True)
    email       = models.EmailField(max_length=255, unique=True)
    contact_number = models.CharField(max_length=254, unique=False)
    company_name= models.CharField(max_length=254, unique=False)
    company_reg_number= models.CharField(max_length=254, unique=True)
    company_address   = models.CharField(max_length=254, unique=True)
    area_code   = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    commodities = models.ManyToManyField('category')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name',
                       'contact_number', 'company_name',
                       'company_reg_number', 'company_address', 'area_code']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        #Returns the first name plus the last name with a space in between
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        #Returns the short name for the user.
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        #Sends an email to this user.
        send_mail(subject, message, from_email, [self.email])'''


