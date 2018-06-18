import httplib, re, urllib2, urllib

if __name__=='__main__':
    conn = httplib.HTTPConnection('192.168.159.131')
    captcha = raw_input('enter captcha:')
    seshcookie = raw_input('enter cookie:')
    headers = {'Cookie': 'rack.session='+seshcookie}
    url = '/captcha/example4/submit?captcha='+captcha+'&submit=Submit'
    full_url = 'http://192.168.159.131'+url
    conn.request('GET',url,'',headers)
    res = conn.getresponse()
#    page = res.read()
#    print page
    if re.search(r'Success!!!', res.read()):
        print 'V'
