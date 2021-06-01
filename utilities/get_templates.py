#!/usr/bin/env python
 
import urllib.request
import urllib.parse
  
def getTemplates(apikey):
    params = {'apikey': apikey}
    f = urllib.request.urlopen('https://api.textlocal.in/get_templates/?'
        + urllib.parse.urlencode(params))
    return (f.read(), f.code)
  
resp, code = getTemplates('NmU0YzM0NDUzNzRlNjI1NzZkNzg1MTQ5NjYzMDVhNmY=')
print (resp)
