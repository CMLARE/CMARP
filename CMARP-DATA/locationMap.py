import requests;

rootURL = "https://maps.googleapis.com/maps/api/geocode/json?address="
footURL = "&key= AIzaSyBloJXnNzRttSXIC7i_NZ9L6WrDFojMKbE "
transmissionTowers = open('./formattedWeatherStations.txt', "a");
with open('./weatherStations.txt') as f:
    for line in f:
        loc = line.split('-')[0];
        address = loc.split('_')[0]
        url = rootURL + address +',Sri Lanka'+ footURL;
        print(url);
        response = requests.get(url=url);
        try:
            location = response.json()['results'][0]['geometry']['location'];
            formattedLocation = ""+str(location['lat'])+","+str(location['lng'] )+ "{"+line.rstrip() + "- Weather Underground } <default>\n"
            transmissionTowers.writelines(formattedLocation)
            # print(formattedLocation)
        except: IndexError

transmissionTowers.close();
