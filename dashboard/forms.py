from django import forms

class SettingsForm(forms.Form):
	dhcp_file_path  =  forms.CharField(
		label='DHCP leases dosya yolu', 
		help_text='Debian dağıtımında dosyanın yolu: /var/lib/dhcpd/dhcpd.leases',
		widget=forms.TextInput(attrs={'class': 'form-control'})
		)
	network = forms.GenericIPAddressField(
		label='Network', 
		help_text="Örneğin: 192.168.1.0",
		widget=forms.TextInput(attrs={'class':'form-control'})
		)
	netmask = forms.ChoiceField(
		label ="Netmask", 
		choices= ((str(x), x) for x in range(0,33)),
		help_text = "Örneğin: 24 = 255.255.255.0",
		widget=forms.Select(attrs={'class':'form-control'})
		)