from django.db import models


class Users(models.Model):
	request_date = models.DateTimeField(auto_now_add=True)
	user_name = models.CharField(max_length=60)
	status = models.ForeignKey("Users_Status")
	device = models.ForeignKey("Devices_Status")
	note = models.CharField(max_length=300, blank=True, null=True)		   				       
	device_status = models.IntegerField(default=0)
	transaction_date = models.DateTimeField(blank=True, null=True)
	ip = models.GenericIPAddressField(protocol='IPv4')
	mac = models.CharField(max_length=20, blank=True, null=True)


class Users_Status(models.Model):
	user_status = models.CharField(max_length=60)

	def __unicode__(self):
		return '%s' % (self.user_status)


class Devices_Status(models.Model):
	device_status = models.CharField(max_length=60)

	def __unicode__(self):
		return '%s' % (self.device_status)
