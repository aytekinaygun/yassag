from django.db import models

class Settings(models.Model):
	dhcp_file_path  = models.CharField(max_length=100)
	network = models.GenericIPAddressField(protocol='IPv4')
	netmask = models.IntegerField()
