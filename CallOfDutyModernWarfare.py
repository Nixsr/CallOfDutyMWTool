from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

import re, sys, datetime, string, os, subprocess

#Get the html code
codMWRequest = Request('http://www.gametracker.com/search/cod4/600/?searchipp=50#search', headers={'User-Agent': 'Mozilla/5.0'})
codMWData = urlopen(codMWRequest).read()


#Convert the html in BeautifulSoup object to scrape it

bsObj = BeautifulSoup(codMWData, 'html.parser')

#print(bsObj)
#Get Rank
def rank(bsObj):
    ranks = []
    for rank in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("tr")[1:-1]:
        rankField = rank.findAll("td")[0]
        ranks.append(rankField.get_text().replace("\t", '').replace("\n", '').replace('.' , ''))
    return ranks

#Get Server Name
def serverName(bsObj):
    serverList = []
    for name in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("a", {"class":"c03serverlink"}):
    #for name in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("b"):
        serverList.append(name.get_text().replace("\t", '').replace("\n", ''))
    return serverList

#Get Players
def playersCounts(bsObj):
    Players = []
    for player in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("tr")[1:-1]:
        slots = player.findAll("td")[3]
        Players.append(slots.get_text().replace("\t", '').replace("\n", ''))
    return Players

#Get Server Location
def serverLocation(bsObj):
    Locations = []
    for location in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("tr")[1:-1]:
        flags = location.findAll("td")[5].find("img")
        Locations.append(flags['src'])
    return Locations[:-1]

#Get Ip:Port
def getIpPort(bsObj):
    ipPorts = []
    for ipPort in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("tr")[1:-1]:
        ipPortField = ipPort.findAll("td")[6]
        ipPorts.append(ipPortField.get_text().replace("\n", ''))
    return ipPorts

#Get serverMap
def serverMap(bsObj):
    serverMaps = []
    for ipPort in bsObj.find("table", {"class":"table_lst table_lst_srs"}).findAll("tr")[1:-1]:
        servermapField = ipPort.findAll("td")[7]
        serverMaps.append(servermapField.get_text().replace("\n", '').replace("\t", '').replace("mp_", ""))
    return serverMaps

Names = serverName(bsObj)
Players = playersCounts(bsObj)
#Locations = serverLocation(bsObj)
IpPorts = getIpPort(bsObj)
ServerMaps = serverMap(bsObj)
Ranks = rank(bsObj)

#IP

#print(len(Names))
#print(len(Players))
#print(len(Locations))
#print(len(IpPorts))
#print(len(ServerMaps))
#print(len(Ranks))

#print(Names)
#print(Players)
#print(Locations)
#print(IpPorts)
#print(ServerMaps)
#print(Ranks)

#TO do

#1) Add the statement to remove the "Players" String from the playersCounts function [Done]
#2) Add the OS call to the game exe 'iw3mp.exe" +connect 66.225.232.198:28970' [Done]
#3) Add the game mode


print("ID".ljust(7, ' ') + "Players/slots".ljust(20, ' ') + "IP:PORT".ljust(38, ' ') + "Server Map".ljust(30, ' ') + "Server Name".ljust(110, ' ') + "\n")
for n in range(len(Ranks)):
    #print(Ranks[n] + "\t\t" + Players[n] + "\t\t connect " + IpPorts[n] + "\t\t" + ServerMaps[n] + "\t\t\n___________________________________________________________________________________")
    print(Ranks[n].ljust(7, ' ') + Players[n].ljust(20, ' ') + "connect " + IpPorts[n].ljust(30, ' ') + ServerMaps[n].ljust(30, ' ') + Names[n].ljust(110, ' ') + "\t\t\n")

ID = input('Scegli l\'ID di un server (dalla prima colonna sulla sx):\n')

if ID in Ranks:
    idPosition = 0
    idPosition = int(Ranks.index(ID))
    print(idPosition)
    print(IpPorts[idPosition])
    #subprocess.call(['C:\Windows\System32\cmd.exe', 'D:\Software\Proprietary\Steam\steamapps\common\Call of Duty 4\iw3mp.exe +connect '+ IpPorts[idPosition]])
    subprocess.call(['D:\Software\Proprietary\Steam\steamapps\common\Call of Duty 4\iw3mp.exe', ' +connect '+ IpPorts[idPosition]])

print(ID)