from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save

# class User(AbstractUser):
#     firstname = models.CharField(max_length=15, blank=True, null=True)
#     lastname = models.CharField(max_length=15, blank=True, null=True)
#     email = models.EmailField()
#     password = models.CharField(max_length=128)
#     rpassword = models.CharField(max_length=128)
#     profilepicture = models.ImageField(upload_to='images/profilepictures', blank=True, null=True,default='images/profilepictures/rafid1.jpg')
#     role=models.TextField(default='user')
#     course=models.IntegerField(default=-1)
#     department=models.IntegerField(default=-1)
#     groups = models.ManyToManyField(
#         'auth.Group',
#         related_name='custom_user_set',
#         blank=True
#     )
#     user_permissions = models.ManyToManyField(
#         'auth.Permission',
#         related_name='custom_user_permissions_set',
#         blank=True
#     )

class User(AbstractUser):  # Extends default Django User
    profile_picture = models.ImageField(upload_to='images/profilepictures', blank=True, null=True)
    role=models.TextField(default='user')
    course=models.IntegerField(default=-1)
    department=models.IntegerField(default=-1)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True
    )

    def __str__(self):
        return self.username

# class View_Profile():
#     fullname = models.CharField(max_length=15, blank=True, null=True)
#     profilepicture = models.ImageField(upload_to='images/profilepictures', blank=True, null=True)
#     role = models.TextField(default='user')
#     email = models.CharField()

    # def __str__(self):
    #     return self.username  # Adjusted to remove raw password display
    
    # def create_profile(sender, instance, created, **kwargs):
    #      if created:
    #          user_profile = User(user = instance)
    #          user_profile.save()

    # post_save.connect(create_profile, sender = AbstractUser)