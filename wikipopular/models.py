from django.db import models
from django.forms import ModelForm
from django.utils.encoding import smart_unicode

# Create your models here.

class wikiTitle(models.Model):
	title = models.CharField(max_length=30, null=True, blank=False)

	def __unicode__(self):
		return smart_unicode(self.title)
