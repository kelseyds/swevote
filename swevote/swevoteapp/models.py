from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User)
	
	def __str__(self):
		return self.user.username

def generate_filename(instance, filename):
	ext = filename.split('.')[-1]
	return 'candidate_pics/' + Candidate.firstname_text+ '_' + Candidate.lastname_text + ext

class Election(models.Model):
	position = models.CharField(max_length=200)
	num_elected = models.IntegerField(default=1)
	users_have_voted_list = models.ManyToManyField(settings.AUTH_USER_MODEL, symmetrical=False, null=True, blank=True)
	is_current = models.BooleanField(default=False)
	def __str__(self):
		return self.position

class Candidate(models.Model):
	firstname_text = models.CharField(max_length=50)
	lastname_text = models.CharField(max_length=50)
	candidate_pic = models.ImageField(upload_to=generate_filename, blank=True)
	num_votes = models.IntegerField(default=0)
	election = models.ForeignKey(Election)
	def __str__(self):
		return self.firstname_text+' '+self.lastname_text

@receiver(post_delete, sender=Candidate)
def candidate_post_delete_handler(sender, **kwargs):
	Candidate = kwargs['instance']
	if Candidate.candidate_pic:
		storage, path = Candidate.candidate_pic.storage, Candidate.candidate_pic.path
		storage.delete(path)

