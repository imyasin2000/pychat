import urllib.request
import os


url = 'http://8upload.ir/uploads/f0371645.mp4'
urllib.request.urlretrieve(url, os.getcwd() + '/UI/Ads/images/Ads_file.png')

