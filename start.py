import sys
import os
from subprocess import call

phantomjs = os.path.join(
  os.environ['HOME'],
  'site',
  'wwwroot',
  'bin',
  'phantomjs.exe'
)

port = os.environ['HTTP_PLATFORM_PORT']

print('Starting PhantomJS...')
print('Using PhantomJS in: ' + phantomjs)
print('Using port: ' + port)

call([phantomjs, "--webdriver=" + port])
