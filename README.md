# UPassRequester
A Python script to request your UBC U-Pass.

Instructions:
* Put your CWL username in "account/username.txt"
* Put your CWL password in "account/password.txt"
* Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it at "lib/chromedriver"
* If you want to run this script on a schedule, point your operating system's task scheduler at "src/main.py"

Program outputs:
* If the given CWL credentials were invalid, the program raises a ValueError.
* If there are no pending U-Passes to request, the program prints a message saying so.
* If there are pending U-Pass(es) to request, the program requests them and prints a message saying so.
