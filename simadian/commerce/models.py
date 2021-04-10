from django.db import models
from django.contrib.auth import get_user_model
from PIL import Image as Img
from io import BytesIO

User = get_user_model()


class Item(models.Model):
	'''
	Upload the items to be sold
	'''
	seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
	buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer", blank=True, null=True)
	name = models.CharField(max_length=225)
	description = models.TextField()
	thumbnail1 = models.ImageField(upload_to='thumbnail',default='default.jpg')
	thumbnail2 = models.ImageField(upload_to='thumbnail',default='default.jpg')
	sold = models.BooleanField(default=False)
	mobile_no = models.CharField(max_length=225)
	country = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	city = models.CharField(max_length=225)
	landmark = models.TextField()
	category = models.CharField(max_length=225)

	def save(self, *args, **kwargs):
		"""
		method to make thumnail of uploaded file
		in the memory itself
		"""
		if self.thumbnail1:
			im = Img.open(self.thumbnail1)
			im.thumbnail1((200,200), Img.ANTIALIAS)
			output = BytesIO()
			im.save(output, format='JPEG')
			output.seek(0)
			self.thumbnail1 = InMemoryUploadedFile(output,'ImageField', "%s.jpg"\
				%self.thumbnail1.name, 'thumbnail/jpeg', output.__sizeof__(), None)

		if self.thumbnail2:
			im = Img.open(self.thumbnail)
			im.thumbnail((200,200), Img.ANTIALIAS)
			output = BytesIO()
			im.save(output, format='JPEG')
			output.seek(0)
			self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg"\
				%self.thumbnail2.name, 'thumbnail/jpeg', output.__sizeof__(), None)
		super(Profile, self).save(*args, **kwargs)

