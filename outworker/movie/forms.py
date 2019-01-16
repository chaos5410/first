from django import forms
from . import models

class VideoForm(forms.ModelForm):
	class Meta:
		#model= Video
		fields = ["name", "videofile"]