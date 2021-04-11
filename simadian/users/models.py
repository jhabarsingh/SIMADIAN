from django.db import models
from django.db.models.signals import pre_save, post_save
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone
from PIL import Image as Img
from io import BytesIO
import secrets
import os


class MyUserManager(BaseUserManager):
    def create_user(self, username, first_name,last_name, email,
                    date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name,last_name, email,
                        date_of_birth, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            first_name,
            last_name,
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField("Date of joining",default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def full_name(self):
        "Return full name of user"
        # firstname + lastname
        return f'{first_name} {last_name}'

class Profile(models.Model):
    '''
    Profile of every User  created when user registers
    '''
    profile = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to='profile_pic',default='default.jpg')

    def save(self, *args, **kwargs):
        """
        method to make thumnail of uploaded file
        in the memory itself
        """
        if self.profile_pic:
            im = Img.open(self.profile_pic)
            im.thumbnail((200,200), Img.ANTIALIAS)
            output = BytesIO()
            im.save(output, format='JPEG')
            output.seek(0)
            self.profile_pic= InMemoryUploadedFile(output,'ImageField', "%s.jpg"\
                %self.profile_pic.name, 'profile_pic/jpeg', output.__sizeof__(), None)
        super(Profile, self).save(*args, **kwargs)


@receiver(post_save, sender=MyUser)
def create_profile(sender, instance, **kwargs):
    profile = Profile(profile=instance)
    profile.save()