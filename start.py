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

port = os.environ['HTTP_PLATFORM_PORT'] or sys.argv[1]

print('Starting PhantomJS...')
print('Using PhantomJS in: ' + phantomjs)
print('Using port: ' + port)

call([phantomjs, "--webdriver=" + port])
