# - * - coding: <utf-8> - * -

# This program is used to find the coordination of longitudes and latitudes
# according to the location information in TwitterData.csv
# and draw a distribution map based on the coordination information

import csv
import sys
import googlemaps
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


#reload(sys)
#sys.setdefaultencoding('utf-8')


gmapkey = 'AIzaSyBmtGkLR1hIEG6KC9Xe7tp5LRO_fP9azdc'



def getCoor(file):
    gmaps = googlemaps.Client(key=gmapkey)
    with open(file, 'rb') as csvFile1:
        csvFile2 = open('Coordinations.csv', 'wb')
        writeObj = csv.writer(csvFile2)
        readObj = csv.reader(csvFile1)

        #  Geocoding an address to get the coordinations
        for line in readObj:
            data = line[1]
            if data == "":
                continue
            else:
                geocode_result = gmaps.geocode(str(data).encode('utf-8'))
                lat = geocode_result[0]['geometry']['location']['lat']
                lng = geocode_result[0]['geometry']['location']['lng']
                # print [lat, lng]
                writeObj.writerow([lat, lng])

    csvFile2.close()
    drawMap('Coordinations.csv')



def drawMap(file):
    # plot the blank world map
    # set resolution='h' for high quality
    my_map = Basemap(projection='merc', lat_0=50, lon_0=-100,
                     resolution='l', area_thresh=5000.0,
                     llcrnrlon=-140, llcrnrlat=-55,
                     urcrnrlon=160, urcrnrlat=70)
    axs = plt.subplot(111)

    # draw elements onto the world map
    my_map.drawcountries()
    # my_map.drawstates()
    my_map.drawcoastlines(antialiased=False,
                          linewidth=0.005)

    # get coordinations from Coordination.csv
    with open(file, 'rb') as csvFile:
        readObj = csv.reader(csvFile)
        longslist = []
        lattslist = []

        # add coordinates as red dots
        for line in readObj:
            lngs = float(line[1])
            lats = float(line[0])
            longslist.append(lngs)
            lattslist.append(lats)
        # print longslist
        # print lattslist
        x, y = my_map(longslist, lattslist)
        axs.plot(x, y, 'ro', markersize=6, alpha=0.5)

    plt.savefig("Distribution Map.png")
    plt.show()


if __name__ == "__main__":
    getCoor('TwitterData.csv')

