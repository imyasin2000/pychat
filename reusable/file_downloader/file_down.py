import urllib.request
import os


url = 'http://8upload.ir/uploads/f452685660.jpeg'
urllib.request.urlretrieve(url, os.getcwd() + '/UI/Ads/images/Ads_file.jpeg')

