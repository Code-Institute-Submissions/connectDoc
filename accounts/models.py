# from django.db import models
# from django.contrib.auth.models import UserDoctor
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# # Create your models here.
# class UserDoctorProfile(models.Model):
#     user = models.OneToOneField(UserDoctor, on_delete=models.CASCADE, related_name="profile")
#     image = models.ImageField(upload_to="avatars", blank=True, null=True, default="avatars/anonymous.jpeg")


# # @receiver(post_save, sender=User)
# # def create_user_profile(sender, instance, created, **kwargs):
# #     if created:
# #         UserProfile.objects.create(user=instance)

# # @receiver(post_save, sender=User)
# # def save_user_profile(sender, instance, **kwargs):
# #     instance.profile.save()
