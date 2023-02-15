from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):
    def create_user(self, username,password=None):
        
        if not username:
            raise ValueError('Users must have an username')
        
        if not password:
            raise ValueError('Users must have a Password')

        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
    
        user = self.create_user(
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Custom User Model

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
    
    @property
    def is_Active(self):
        return self.is_active
    
    @property
    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        refresh['username'] = self.username
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
    def refresh(self):
        refresh=RefreshToken.for_user(self)
        return str(refresh)
    def access(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)
    
class PrivateTaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=200,null=True,blank=True)
    is_completed = models.BooleanField(default=False)
    time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.user.username} -- {self.task}'