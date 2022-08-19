from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
  class Types(models.TextChoices):
    PROFESSIONAL= "PROFESSIONAL", "Professional"
    INSTITUTION_STAFF = "INSTITUTION_STAFF", "Institution Staff"
    UNDEFINED = "UNDEFINED", "Undefined"

  base_type = Types.UNDEFINED

  type = models.CharField( "Type", max_length=50, choices=Types.choices, default=base_type
  )
  #user_type = models.CharField(max_length=50, choices=USER_TYPE_CHOICES, null=True, blank=True)
  is_professional = models.BooleanField(default=False)
  is_institution_staff = models.BooleanField(default=False)


class InstitutionStaffManager(models.Manager):
	
	def get_queryset(self):
		return super().get_queryset().filter(type = User.Types.INSTITUTION_STAFF)

class InstitutionStaff(User):
  base_type = User.Types.INSTITUTION_STAFF
  objects = InstitutionStaffManager()
  
  class Meta:
    proxy = True
  
  def save(self, *args, **kwargs):
    if not self.pk:
      self.type = self.base_type
    return super().save(*args, **kwargs)

class ProfessionalManager(models.Manager):
	
	def get_queryset(self):
		return super().get_queryset().filter(type = User.Types.PROFESSIONAL)


class Professional(User):
  base_type = User.Types.PROFESSIONAL
  objects = ProfessionalManager()
  
  class Meta:
    proxy = True
  
  def save(self, *args, **kwargs):
    if not self.pk:
      self.type = self.base_type
    return super().save(*args, **kwargs)



class ProfessionalProfile(models.Model):
  user = models.OneToOneField(Professional, on_delete = models.CASCADE, primary_key=True)
  pro_category = models.CharField(max_length=100)
  pro_level = models.PositiveIntegerField()


class BaseModel(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  modified_on = models.DateTimeField(auto_now=True)

  class Meta:
    abstract=True


class Institution(BaseModel):
  name = models.CharField(max_length=250)
  slug = models.CharField(max_length=250)
