import urllib.request
import webbrowser
try:
    url = input("enter url\n")
    u = urllib.request.urlopen(url)
    print(u.headers)
    header =u.headers
    if 'X-Frame-Options' in header:
        print("good way")
    else:
        print("your website is vulnerable to clickjacking")
        f = open("clickjacking.html",'w')
        message = """<html>
        <head></head>
        
        <body><iframe style="width:500px;height:500px;" src=  %s > </iframe></body>
        </html>"""% url
        f.write(message)
        f.close()
        webbrowser.open_new_tab('clickjacking.html')
        
except:
    print("error occured")