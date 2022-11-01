from django.conf import settings
from django.db.models.signals import post_delete, post_save

from .models import Profile


def createProfile(sender, instance, created: bool, **kwargs):
    """createProfile sets a signal to create a profile when a user registers for an account"""

    if created:
        user = instance

        firstname = ""
        lastname = ""

        if user.firstname:
            firstname = user.firstname
        if user.lastname:
            lastname = user.lastname
        print(f"Profile {user.username}-FirstName {firstname}")
        profile: Profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            firstname=firstname,
            lastname=lastname,
        )


def updateUser(sender, instance, created: bool, **kwargs):
    profile = instance
    user = profile.user

    if not user:  # no qa
        print("No user")
        return

    if not created:
        user.firstname = profile.firstname
        user.lastname = profile.lastname
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
        print("Deleting user...")
    except:  # noqa
        pass


post_save.connect(createProfile, sender=settings.AUTH_USER_MODEL)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
