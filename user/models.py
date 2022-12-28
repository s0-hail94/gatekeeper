from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
   
    def __str__(self):
        return f"Username {self.username}"

    class Meta:
        verbose_name = "user "
        verbose_name_plural = "users"
