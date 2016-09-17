from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from devices_registration.models import *
from django.http import HttpRequest  # for get ip address
from django.template import RequestContext # for csrf_token
import re

# For Debian isc_dhcpd service...
dhcp_file = "/var/lib/dhcp/dhcpd.leases"

def get_mac(ip_address):
	
	pattern = re.compile(r"lease ([0-9.]+) {.*?hardware ethernet ([:a-f0-9]+);.*?}", re.MULTILINE | re.DOTALL)

	with open(dhcp_file) as f:
	    for match in pattern.finditer(f.read()):
	    	if ip_address == match.group(1):
	    		return(match.group(2))

def index(request):
	if request.method == "POST":
		register = {}
		f1 = request.POST.get('f1')
		register['user_name'] = f1 
		f2 = request.POST.get('f2')
		register['status_id'] = f2
		f3 = request.POST.get('f3')
		register['device_id'] = f3
		f4 = request.POST.get('f4')
		register['note'] = f4
		register['device_status'] = '0'
		ip_address = request.META['REMOTE_ADDR']
		register['ip'] = ip_address
		mac = get_mac(ip_address)
		register['mac'] = mac

		user_add = Users(**register)
		user_add.save()

		return render_to_response('info.html',{'register':register})


	elif request.method == "GET":
		data = {}
		user_status_list = Users_Status.objects.values_list()
		data['user_status_list'] = user_status_list
		device_list = Devices_Status.objects.values_list()
		data['device_list'] = device_list
		return render_to_response('index.html',{'data':data}, context_instance=RequestContext(request)) # context_instance for csrf
