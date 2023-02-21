


s = input("Type your file " ).lower()

if ("jpg" or "jpeg") in s:
    print('image/jpeg')
if ("png") in s:
    print('image/png')
elif 'png' in s:
    print('image/png')
elif "pdf" in s:
    print('application/pdf')
elif "zip" in s:
    print('application/zip')
else:
    print('application/octet-stream')


