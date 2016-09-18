#from django.shortcuts import render
from dashboard.models import *
from devices_registration.models import *
#from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpRequest  # for get ip address
from django.template import RequestContext # for csrf_token
from django.utils import timezone
from django.shortcuts import redirect
from .forms import SettingsForm

def calculate_totals():
	# pending = 0, save = 1, not save = 2
	number_of_pending = Users.objects.filter(device_status="0").count()
	number_of_save = Users.objects.filter(device_status="1").count()
	number_of_rejected = Users.objects.filter(device_status="2").count()
	totals = {'number_of_pending':number_of_pending, 'number_of_save':number_of_save, 'number_of_rejected':number_of_rejected}
	return totals


def dashboard(request):
	totals = calculate_totals()
	return render_to_response('dashboard.html', totals)

def device_save_reject_del(request):
	if request.method == "POST":
		user_id = request.POST.get('user_id')
		transaction_date = timezone.now()

		if 'device_save' in request.POST:
			device_status = '1'
			# UPDATE FIELD
			Users.objects.filter(id=user_id).update(device_status=device_status, transaction_date=transaction_date)

		elif 'device_reject' in request.POST:
			device_status = '2'
			# UPDATE FIELD
			Users.objects.filter(id=user_id).update(device_status=device_status, transaction_date=transaction_date)

		elif 'device_del' in request.POST:
			Users.objects.filter(id=user_id).delete()

	return redirect('/dashboard')

def dev_edit(request):
	if request.method == "POST":
		user_id = request.POST.get('user_id')
		context = Users.objects.filter(id=user_id).select_related()
		return render_to_response('dev_edit.html', {'context':context}, context_instance=RequestContext(request))	

def dev_request(request):	
	if request.method == "POST":
		if 'device_save' in request.POST:
			device_status = '1'
		elif 'device_reject' in request.POST:
			device_status = '2'

		transaction_date = timezone.now()
		user_id = request.POST.get('user_id')
		# UPDATE FIELD
		Users.objects.filter(id=user_id).update(device_status=device_status, transaction_date=transaction_date)

	# TABLE JOIN
	context = Users.objects.filter(device_status="0").select_related() 
	return render_to_response('dev_request.html', {'context':context}, context_instance=RequestContext(request))


def dev_check(request):
	context = Users.objects.filter(device_status="1").select_related() 
	return render_to_response('dev_check.html', {'context':context}, context_instance=RequestContext(request))


def dev_rejected(request):	
	context = Users.objects.filter(device_status="2").select_related() 
	return render_to_response('dev_rejected.html', {'context':context}, context_instance=RequestContext(request))

# def settings(request):
# 	data = Settings.objects.get(id="1")

# 	if request.method == "POST":
# 		form = SettingsForm(request.POST)
# 		if form.is_valid():
# 			f = form.cleaned_data
# 			data.dhcp_file_path = f['dhcp_file_path']
# 			data.network = f['network']
# 			data.netmask = f['netmask']
# 			data.save()
# 			return redirect('/dashboard')
# 		else:
# 			print (form.errors)
# 			return render_to_response('settings.html', {'errors': form.errors}, context_instance=RequestContext(request))


# 	form = SettingsForm(initial=data.__dict__)
# 	return render_to_response('settings.html', {'form': form}, context_instance=RequestContext(request))

def settings(request):
	if request.method == "GET":
		saved_info = ""

	data = Settings.objects.get(id="1")
	form = SettingsForm(initial=data.__dict__)

	if request.method == "POST":
		form = SettingsForm(request.POST or None)
		if form.is_valid():
			f = form.cleaned_data
			data.dhcp_file_path = f['dhcp_file_path']
			data.network = f['network']
			data.netmask = f['netmask']
			data.save()
			saved_info = "Ayarlar kayıt edildi."
		else:
			saved_info = ""
	
	context = {
		"saved_info" : saved_info,
		"form" : form
		}

	return render_to_response('settings.html', context, context_instance=RequestContext(request))