import os

# give your custom path
SAI_CODE_LOCATION = r'/home/ubuntuserver/dinesh/SAI/'
SAI_CODE_LOCATION = r'C:/github-keysight/SAI'
SAI_CODE_LOCATION = r'C:/github-mgheorghe/generate-sai-cases/generated'



ACTION = '''
    - name: Run API tests
      run: ./exec.sh --no-tty pytest --testbed=saivs_standalone -v -k "api/"'''


for root, dirs, files in os.walk(SAI_CODE_LOCATION):
    for file in files:
        if file.endswith('.py'):
            print('''\
    - name: Run API %s
      continue-on-error: true
      run: ./exec.sh --no-tty pytest --testbed=saivs_standalone -v -k "api/%s"''' % (file, file))
