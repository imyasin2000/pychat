import urllib.request
import os


print('Beginning file download with urllib2...')

url = 'http://8upload.ir/uploads/f0371645.mp4'
print(os.getcwd()+"/cat.mp4")
# os.popen("cat.mp4")
urllib.request.urlretrieve(url, 'cat.mp4')

