from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image as Img
from io import BytesIO

User = get_user_model()

class Category(models.Model):
	category = models.CharField(max_length=255, primary_key=True)


class Item(models.Model):
	'''
	Upload the items to be sold
	'''
	seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="seller")
	buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer", blank=True, null=True)
	category = models.ManyToManyField(Category)
	name = models.CharField(max_length=225)
	description = models.TextField()
	writer = models.CharField(max_length=225)
	thumbnail1 = models.ImageField(upload_to='thumbnail',default='default.jpg')
	thumbnail2 = models.ImageField(upload_to='thumbnail',default='default.jpg')
	cost_price = models.CharField(max_length=10)
	sell_price = models.CharField(max_length=10)
	sold = models.BooleanField(default=False)
	mobile_no = models.CharField(max_length=225, blank=True, null=True)
	country = models.CharField(max_length=225)
	state = models.CharField(max_length=225)
	city = models.CharField(max_length=225)
	landmark = models.TextField(blank=True, null=True)
	educational_institution = models.CharField(max_length=255, blank=True, null=True)

	def save(self, *args, **kwargs):
		"""
		method to make thumnail of uploaded file
		in the memory itself
		"""
		if self.thumbnail1:
			im = Img.open(self.thumbnail1)
			im.thumbnail((200,200), Img.ANTIALIAS)
			output = BytesIO()
			im.save(output, format='JPEG')
			output.seek(0)
			self.thumbnail1 = InMemoryUploadedFile(output,'ImageField', "%s.jpg"\
				%self.thumbnail1.name, 'thumbnail/jpeg', output.__sizeof__(), None)

		if self.thumbnail2:
			im = Img.open(self.thumbnail2)
			im.thumbnail((200,200), Img.ANTIALIAS)
			output = BytesIO()
			im.save(output, format='JPEG')
			output.seek(0)
			self.thumbnail = InMemoryUploadedFile(output,'ImageField', "%s.jpg"\
				%self.thumbnail2.name, 'thumbnail/jpeg', output.__sizeof__(), None)
		super(Item, self).save(*args, **kwargs)


class Messages(models.Model):
	'''
	Inbox messages
	'''
	sender = models.ForeignKey(User, related_name="senders", on_delete=models.DO_NOTHING)
	receiver = models.ForeignKey(User, related_name="receivers", on_delete=models.DO_NOTHING)
	content = models.TextField()