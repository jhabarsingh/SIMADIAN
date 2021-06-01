import urllib.request
import urllib.parse
  
def sendSMS(apikey, numbers, sender, message):
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)
  
resp, code = sendSMS('NmU0YzM0NDUzNzRlNjI1NzZkNzg1MTQ5NjYzMDVhNmY=', '918123456789',
    'Jims Autos', 'Test with an ampersa')
print (resp)
