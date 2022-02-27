from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_images')

    def __str__(self):
        return f'{self.user.username} Profile'

    # @receiver(post_save, sender=User)
    # def update_profile_signal(sender, instance, created, **kwargs):
    #   if created:     
    #     Account.objects.create(user=instance)
    #     instance.account.save()
