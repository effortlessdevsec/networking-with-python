import socket
import pandas as pd
import numpy as np
import requests
import urllib.request
from colorama import Fore, Back, Style
try:
    s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print(s)
    url = input("enter your web address\n")
    x = urllib.request.urlopen("http://www."+url)
    y = x.headers
    print(y)
    df = pd.DataFrame(y.items())
    df.columns = ['header', 'value']
    p = df[df.columns[0]]
    list = p.tolist()
    miss = ['Content-Type', 'Cache-Control', 'X-XSS-Protection', 'X-Frame-Options']
    s =  set(miss) - set(list)
    if(len(s)>0):
        p=print(Back.RED,Fore.RED,"These security header missing:",s)
    else:
        print(Back.RED,Fore.LIGHTGREEN_EX,"security headers are implemented")

except:
    print("please enter right url")



