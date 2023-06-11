from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
import json
#from django.utils import timezone

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)
    

    
    
class User(AbstractBaseUser, PermissionsMixin):

    cin = models.CharField(max_length=10, primary_key= True)
    first = models.CharField(max_length=255)
    last = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, default='', unique=True) 
    tel = models.CharField(max_length=10 , unique = True)
    birth_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add= True)
    img = models.ImageField(null = True, blank=True) 

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    #date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def get_full_name(self):
        return f'{self.first} {self.last}'
    

class Vacataire(User):
    dept = models.CharField(max_length= 30, default = '')
    present = models.BooleanField(default = False)
    date_presence = models.DateTimeField(auto_now_add= True)  
    cours = models.TextField(default='')

    def set_data(self, data_list):
        self.data = json.dumps(data_list)

    def get_data(self):
        return json.loads(self.data)  



class Contrat(models.Model):
    
    id = models.CharField(max_length=20 , primary_key= True)
    prof = models.ForeignKey(Vacataire, on_delete = models.CASCADE)
    #emp = models.ForeignKey(User, on_delete = models.CASCADE)
    debut = models.DateField( auto_now=False, auto_now_add=False)
    fin = models.DateField(auto_now=False, auto_now_add=False)
    nbre_heures = models.PositiveIntegerField()
    remuniration = models.DecimalField(max_digits=6, decimal_places=2)
    termes = models.TextField()
    date = models.DateTimeField(auto_now_add= True)


    def __str__(self) :
        return f"Contract N: {self.id} \n Debiteur : {self.emp} \n Creancier : {self.prof}"


class Absence(models.Model):

    prof = models.OneToOneField(User, on_delete=models.CASCADE, primary_key= True)
    date_abs = models.DateTimeField(auto_now=False, auto_now_add=False)
    justifiee = models.BooleanField()
    motif = models.CharField(max_length = 100)
    #file = models.FileField(upload_to='files/')



class OperationHistory(models.Model):
    pass

