def main():
  months =  [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        s = input('Date: ')
        try:
            month, day, year = date.split('/')
            if(  1<= int(month) <= 12) and ( 1<= int(day) <=31):
              break
        except:
              try:
                 old_m, old_d, old_y = date.split(' ')
                 for i in range(len(months)):
                    if old_m ==  month[i]:
                       month = i + 1
                 day = old_d.replace(',', '')
                 if ( 1<= int(month) <= 12) and ( 1<= int(day) <=31):
                    break
                except:
                 print()
                 pass
    print(f'(year)-(int(month):02)-(int(day):02)')

main()