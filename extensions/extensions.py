


s = input("Type your file " ).lower()

if ("jpg" or "jpeg") in s:
    print('image/jpeg')
if ("png") in s:
    print('image/png')
elif 'gif' in s:
    print('image/gif')
elif "pdf" in s:
    print('application/pdf')
elif "zip" in s:
    print('application/zip')
else:
    print('application/octet-stream')


