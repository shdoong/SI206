# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.
from bs4 import BeautifulSoup
import urllib
import requests
import re

base_url = 'http://collemc.people.si.umich.edu/data/bshw3StarterFile.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'html.parser')

str_soup = soup.encode("ascii", "ignore").decode("utf-8") #encode and decode will convert to string


main_img_replace = str_soup.replace("https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg", "media/IMG_6293.jpg") #replacing main picture with personal picture
local_img_replace = main_img_replace.replace("logo2.png", "media/logo.png") #replacing logo pictures with photo from media file

x = local_img_replace.replace("student", "AMAZING student") #replaces student with AMAZING student

fout = open("new_html.html", "w") #creating a write-able html file
fout.write(x) #writing into html file
fout.close()