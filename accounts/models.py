from PIL import Image
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
		now = timezone.now()
		if not email:
			raise ValueError(_('Users must have an email address'))
		if not username:
			raise ValueError(_('Users must have a username'))
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, is_staff=is_staff, is_active=True, is_superuser=is_superuser, last_login=now, date_joined=now, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, **extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # A full User model with admin-compliant permissions that uses a full-length email field as the username
	# Email and password are required but all other fields are optional
	email = models.EmailField(_('email address'), max_length=254, unique=True)
	username = models.CharField(max_length=50, unique=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	section = models.CharField(max_length=30)
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into this admin site.'))
	is_superuser = models.BooleanField(_('superuser status'), default=False, 
		help_text=_('Designates that this user has all permissions without explicitly assigning them.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

	objects = UserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_absolute_url(self):
		return "/users/%s/" % urlquote(self.email)

	def get_full_name(self):
        # Returns the first_name plus the last_name, with a space in between
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		# Returns the short name (first name) for the user
		return self.first_name

	#def email_user(self, subject, message, from_email=None):
        # Sends an email to this User
		#send_mail(subject, message, from_email, [self.email])

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='media/profile_pics/default.jpg', upload_to='profile_pics') # When in development remove 'media/' in upload_to

	def __str__(self):
		return f'{self.user.username} Profile'

	# def save(self, *args, **kwargs):
		# super().save(*args, **kwargs)
		
		# img = Image.open(self.image.path)

		# if img.height > 300 or img.width > 300:
			# output_size = (300, 300)
			# img.thumbnail(output_size)
			# img.save(self.image.path)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()