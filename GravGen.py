import hashlib
import sys

GRAVATAR_URL = 'http://www.gravatar.com/avatar/'

# class Gravtr(object):
#     def __init__(self, email):
#         self.email = email

#     def generate(self, size=None):
#         email = self.email.encode('utf-8')
#         self.url = GRAVATAR_URL + hashlib.md5(email).hexdigest()
#         if size:
#             self.url = self.url + '?' + 's={}'.format(str(size))
#         return self.url


def generate(email, size=None):
	email = email.encode('utf-8')
	print type(email)
	hexval = hashlib.md5(email).hexdigest
	print type(hexval)
	url = GRAVATAR_URL + hashlib.md5(email).hexdigest
	if size:
		url = url + '?' + 's={}'.format(str(size))
	
	return url