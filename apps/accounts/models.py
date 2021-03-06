from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from ckeditor.fields import RichTextField
from django.contrib.auth.models import Group

# from apps.blogs.models import BlogPost


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        """Creating new user and saving the user."""
        if not email:
            raise ValueError("Admin must have a valid email")
        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Creates and saves a new super user"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    # is_agent = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"


User = get_user_model()


class UserProfile(models.Model):
    USER_TYPES = (
        ("b", "Bon-Admin"),
        ("g", "Agent"),
        ("c", "Customer"),
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, related_name="profile", on_delete=models.CASCADE
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default="g")
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    company_name = models.CharField(max_length=255, default="")
    email_address = models.EmailField(default="abc@abc.com")
    phone_number = models.CharField(max_length=255, default="")
    experience = models.IntegerField(default=10)
    commission = models.CharField(max_length=50, default="15%")
    avatar = models.ImageField(blank=False)

    thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(100, 50)],
        format="JPEG",
        options={"quality": 60},
    )
    # cover_photo = models.ImageField(blank=True, null=True)
    languages = models.CharField(max_length=255)
    expert_countries = models.TextField()
    about = RichTextField()
    travel_advice = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        if self.id and self.avatar:
            current_avatar = UserProfile.objects.get(pk=self.id).avatar
            if current_avatar != self.avatar:
                current_avatar.delete()
        super(UserProfile, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     target = reverse('accounts:profile', args=[self.user.email])
    #     return target

    def is_admin(self):
        return self.user_type == "a"

    def is_agent(self):
        return self.user_type == "g"

    def is_customer(self):
        return self.user_type == "c"


class PartnerApplication(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    email_address = models.EmailField()
    phone = models.CharField(max_length=255)
    state = models.CharField(max_length=255)


class BookmundiAccount(models.Model):
    # personal details
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    nationality = models.CharField(max_length=255)
    spoken_languages = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    short_bio = models.TextField(max_length=255)
    website_if_any = models.CharField(max_length=255, null=True)

    # contact details
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)

    # passport details
    passport_number = models.CharField(max_length=255)
    issue_date = models.DateField()
    expiry_date = models.DateField()
