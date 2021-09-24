
#!/usr/bin/python3
#
#  [Program]
#
#  pHONE NUMBER INFO
#  PNI
#
#  [Author]
#  HorridHanu
#
#
#
#  [License]
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#
#  See 'LICENSE' for more information.


import phonenumbers
from opencage.geocoder import OpenCageGeocode
import folium
import sys
from pyfiglet import Figlet


__author__ = "Hanu"
__license__ = "GPL"
__version__ = "1.3"




""" Don't tried to copy key. """
key = "6c88f3edf15448a582a99183d722b39c"

class color :
    RED = '\033[91m'    # Red color
    GREEN = '\033[92m'  # Green color
    YELLOW = '\033[93m' # Yellow color



class Banner:
    custom_fig = Figlet(font='graffiti')
    print(color.YELLOW + custom_fig.renderText('||  H A N U  ||'))
    print(color.YELLOW + '+[+[+[ PHONE NUMBER INFO ]+]+]+')
    print(color.YELLOW+ '+[+[ CONTACT US +919910384164 ]+]+ || NO SPAM PLEASE! ')

class Number:

    def __init__(self):
        from phonenumbers import geocoder, carrier
        try:
            print(color.RED + "\n+[+[+[ Initializing program ]+]+]+")
            target = str(input(color.RED +'Enter target number, e.g. +1 XXXX <: '))
            if target == "" or target == " " or target == "   ":
                print('ERROR: Invalid Number. Goodbye.')
                sys.exit(1)

            print(color.YELLOW + "\n+[+[+[ Setting Up program wait! ]+]+]+")
            Target = phonenumbers.parse(target)
            Location = geocoder.description_for_number(Target, "en")
            geocoder = OpenCageGeocode(key)
            query = str(Location)
            result = geocoder.geocode(query)
            lat = result[0]['geometry']['lat']
            lng = result[1]['geometry']['lng']
            print(color.GREEN + "\n\n[+[+[ <: Result :> ]+]+]+")

            myMap = folium.Map(locations=[lat, lng], zoom_start=90)
            folium.Marker([lat, lng], popup=Location).add_to((myMap))




            print(color.GREEN + "\nHome Country <: " + Location)
            print(color.GREEN+'Service provider <: '+carrier.name_for_number(Target, "en"))
            print(color.GREEN +f"Latitude <: {lat} || Longitude <: {lng}")

            """     <: setting up file Name :>     """

            TargetFile = str(input(color.RED + '\nEnter the file to save location <: '))
            myMap.save(TargetFile + ".html")

            print(color.RED + "+[+[+[ <: Done :> ]+]+]+")
            print(color.RED + f"+[+[+[ Check current directory for location {TargetFile}.html> ]+]+]+")
            print(color.GREEN + '\nGOOD BYE. THANKS FOR USING!')
            sys.exit(1)

        except Exception as e:
            print(color.YELLOW+f'ERROR: {e}')





if __name__=='__main__':
    Banner()
    Number.__init__(1)

