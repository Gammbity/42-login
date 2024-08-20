from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser
from django.contrib.auth.hashers import make_password

class CustomUserManager(UserManager):
    def _create_user(self, telegram_id, password, **extra_fields):
        if not telegram_id:
            raise ValueError("The telegram_id must be set")
        user = self.model(telegram_id=telegram_id, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, telegram_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(telegram_id, password, **extra_fields)

    def create_superuser(self, telegram_id, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(telegram_id, password, **extra_fields)

class User(AbstractBaseUser):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "telegram_id"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()


    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = 'foydalanuvchi'
        verbose_name_plural = 'faydalanuchilar'


class GeneratePassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user
    
    class Meta:
        ordering = ['-time']
        verbose_name = 'parol generatsiyasi'
        verbose_name_plural = 'parol generatsiyalari'