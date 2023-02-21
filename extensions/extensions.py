


s = input("Type your file " ).lower()

if (".jpg") in s:
    print('image/jpeg')
elif ('.jpeg') in s:
    print('image/jpeg')
elif (".png") in s:
    print('image/png')
elif 'gif' in s:
    print('image/gif')
elif ".pdf" in s:
    print('application/pdf')
elif ".zip" in s:
    print('application/zip')
elif ".txt" in s:
    print('text/plain')
else:
    print('application/octet-stream')


