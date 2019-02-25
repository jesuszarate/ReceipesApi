from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Respents a "user profile" inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name."""

        return self.name

    def get_short_name(self):
        """Used to get a users short name."""

        return self.name

    def __str__(self):
        """Django uses this when it needs to convert the object to a string"""

        return self.email


class ProfileFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string."""

        return self.status_text


'''
****************************
* This is the receipe area *
****************************
'''


class Receipe(models.Model):

    title = models.CharField(max_length=255)
    # ingredient_list = models.ForeignKey(
    #     'IngredientList', on_delete=models.CASCADE)
    # instructions = models.ForeignKey(
    #     'InstructionList', on_delete=models.CASCADE)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Ingredient(models.Model):

    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    portion = models.ForeignKey('Portion', on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class IngredientList(models.Model):

    list_id = models.ForeignKey('Receipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.PROTECT)

    def __str__(self):
        return "{0}:{1}".format(self.list_id, self.ingredient)


class Instruction(models.Model):

    instruction = models.CharField(max_length=255)

    def __str__(self):
        return self.instruction


class InstructionList(models.Model):

    list_id = models.ForeignKey('Receipe', on_delete=models.CASCADE)
    instruction = models.ForeignKey('Instruction', on_delete=models.CASCADE)

    def __str__(self):
        return "{0}:{1}".format(self.list_id, self.instruction)


class Portion(models.Model):

    amount = models.FloatField()
    portion_type = models.CharField(max_length=255)

    def __str__(self):
        return '{0} {1}'.format(self.amount, self.portion_type)
