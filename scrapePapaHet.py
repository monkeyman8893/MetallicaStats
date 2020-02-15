from bs4 import BeautifulSoup
import requests
import csv

'requesting the webpage contents'
source = requests.get('https://www.ipom.com/cgi-bin/tour_stats.pl#stats').text 
soup = BeautifulSoup(source, 'lxml')

songCategories = soup.find_all('strong')
songCategories.pop()

'uls are the songs itemized. The webpage was poorly formatted'
'had to extract all the ul tags first'
uls = soup.find_all('ul')

'uls 4 to 19 comprise of all the song categories'


songName = []
count = []
albumName = []

csv_file = open('songStatsMetallica.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['AlbumName', 'SongName', 'Counts'])
'doing the shit for one uls'
for i in range(len(songCategories)):
    ulsCat = uls[i+4]
    ulsCatLi = ulsCat.find_all('li')
    for songs in ulsCatLi:
        textSong = songs.text
        textSongList = textSong.split('\xa0')
        songName = textSongList[0]
        try:
            count = int(textSongList[2].split(' ')[3])
        except IndexError:
            count = 0
        except ValueError:
            count = int(textSongList[2].split(' ')[2])
        albumName = songCategories[i].text
        csv_writer.writerow([albumName, songName, count])
csv_file.close()
