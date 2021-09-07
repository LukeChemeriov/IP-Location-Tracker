# IMPORTS
from geolite2 import geolite2
import requests


# thanks to W3W3W3

#main function
def my_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    # geolite database dict values and fine tunning
    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\ncountry: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivisions: %s\n'''
     % (a,b,c,d,e,f,g))

print('Enter IP')
ip = input()

my_ip_location(ip)
