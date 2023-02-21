


s = input("Type your file " ).lower().strip()
if "jpg" or "jpeg" in s:
    print('image/jpeg')
elif 'png' in s:
    print('image/png')
elif "pdf" in s:
    print('application/pdf')
else:
    print('application/octet-stream')


