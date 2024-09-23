from django.db import models
from django.contrib.auth.models import User


from django.contrib.auth.models import User
from django.db import models

class ContactRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Reference to User
    name = models.CharField(max_length=200, null=False, blank=False)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=80, null=False, blank=False)
    message = models.TextField(max_length=80, null=False, blank=False)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Contact form sent by {self.name}"

    def save(self, *args, **kwargs):
        # Check if the user is authenticated
        is_authenticated_user = self.user and self.user.is_authenticated

        # Store email in ContactEmailList with name and is_user fields
        email_entry, created = ContactEmailList.objects.get_or_create(
            email=self.email,
            defaults={'name': self.name, 'is_user': is_authenticated_user}
        )
        if not created:  # Update name and user status if entry already exists
            email_entry.name = self.name
            email_entry.is_user = is_authenticated_user
            email_entry.save()

        super(ContactRequest, self).save(*args, **kwargs)


class ContactEmailList(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)  # Store the name
    company_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=80, unique=True)
    is_user = models.BooleanField(default=False)  # Indicates if the email is from an authenticated user

    def __str__(self):
        return f"{self.name} ({self.email})"
