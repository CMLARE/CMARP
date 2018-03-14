import requests;
from datetime import datetime;
rootURL = "https://api.darksky.net/forecast/0d63da2966e33f334ce6d48727f60f5e/"

lat = float(raw_input("Enter Latitiude  :   "));
lang = float(raw_input("Enter Longitude   :   "));
date   =    raw_input("Enter date (Default NOW ) :   ");
time   =    raw_input("Enter Time (Default-00:00:00)  :   ");
exclude = raw_input("Enter Comma separated exclude parameters :  ");
cordStepSize = raw_input(" Size of the cordinate steo(Default 1)  : ");
sizeOfBlock  = raw_input("Size of the block need to cover(No of steps   :   ");

if(date == ""):
    date = str(datetime.now().date());
    print("Date is :" + date);
else:
    date = str(date);
if(time== ""):
    time = "00:00:00";
else:
    time = str(time);
if(exclude==""):
    excludes = "";
else:
    excludes="exclude="+exclude;
if(cordStepSize == ""):
    cordStepSize = 1.00;
else:
    cordStepSize = float(cordStepSize);
if(sizeOfBlock== ""):
    sizeOfBlock = 1;
else:
    sizeOfBlock = int(sizeOfBlock);


if(sizeOfBlock*sizeOfBlock >=1000):
    print("Exceeds the total posible requests");
    exit();


for i in range(sizeOfBlock):
    for j in range(sizeOfBlock):
        lLat = str(lat+(cordStepSize*i));
        lLang = str(lang+(cordStepSize*j));

        url = rootURL + lLat + "," + lLang + "," + date + "T" + time +"?"+excludes;
        print(url);
        response = requests.get(url=url);

        print(response.json());

