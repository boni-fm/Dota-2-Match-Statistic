'''
blok code dibawah mengimport beberapa libary yaitu libary
requests, json, csv
pandas as pd
matplotlib.pyplot as plt
'''
import requests, json, csv
import pandas as pd
import matplotlib.pyplot as plt

'''
Dibawah merupakan code untuk mendapatkan data players dari API opendota
berdasarkan idnya. Program ini menggunakan data player dengan id 205853225.

data didapatkan dari 'https://api.opendota.com/api/players/205853225/matches'
dimasukan ke dalam variable link. Lalu meminta request dengan requests.get(link)
dari libary request. kemudian dijalankan json.loads(r.text) untuk menjadikan
request tersebut menjadi sebuah list

PENJELASAN VARIABLE
link : menyimpan link api dari opendota
r : berisi request dari link dalam bentuk json
data : merupakan list dari data matchs dota 2 dari player
'''
#-Mendapatkan data dari API opendota
link = 'https://api.opendota.com/api/players/205853225/matches'
r = requests.get(link)
data = json.loads(r.text)




'''
Data yang didapatkan diatas (variable data) diubah menjadi data frame, kemudian 
membuat data frame baru (variable df20) yang menyimpan 20 data match terbaru 
dan data yang disimpan yaitu match_id, game_mode, duration, hero_id, kills, 
deaths, assists

kemudian data pada df20 dimasukan kedalam file .csv agar user dapat mengetahui 
data user dalam bentuk csv pada excel.

PENJELASAN VARIABLE
df : merupakan data frame yang berisi data matchs player
df20 : data frame berisi 20 match paling baru 
'''
#-Membuat data frame 20 match terbaru & file csv-nya
df = pd.DataFrame(data)
df20 = df.iloc[0:20][['match_id', 'game_mode', 'duration', 'hero_id', 'kills', 'deaths', 'assists']]
df20.to_csv('/Not Data/Python/dota_statistics/data_20matches.csv')




'''
Blok code dibawah menampilkan informasi umum seperti player id, total matchs
player, dan menampilkan lengkap data 20 match terakhir

informasi player id sudah dimasukan lewat program.
total matchs player didapatkan dengan sintaks str(lens(data)). lens(data) diubah
menjadi string agar bisa ditampilkan dengan print

data 20 match terakhir ditampilkan dengan sintaks df20.to_string(index = False)
sintaks tersebut menampilkan df20 tanpa ada nomor index disampingnya, karena
jika ditampilkan hanya dengan sintaks print(df20), makan index akan muncul 
disamping kiri

blok code dibawah terdapat sintaks print(68 * '=') dan beberapa yang serupa. 
sintaks tersebut berfungsi untuk menampilkan '='/'-' sebanyak angka perkaliannya
dengan sintaks tersebut, akan ditampilkan garis putus-putus yang berfungsi 
sebagai pembatas. 
sintaks yang serupa dengan ini akan banyak muncul diprogram ini dan berfungsi 
sebagai pembatas dari kategori-kategori. 
'''
#Informasi Awal
print(68 * '=')
print(25 * ' ', "STATISTIK DOTA 2")
print(68 * '=')

print('Player ID\t : 205853225')
print('Total Match\t : ' + str(len(data)) + '\n')
print(22 * '-', "Data 20 Match Terakhir", 22 * '-')

print(df20.to_string(index = False))
print(68 * '-')




'''
block code dibawah akan menampilkan jenis game mode yang dimainkan player, 
kemudian ditampilkan jumlahnya

game mode : 
    '22' = all_pick
    '4' = single_draft

pertama program akan melakukan looping untuk mencari jumlah matchs dari tiap
game mode. kemudian hasil tersebut ditampilkan

PENJELASAN VARIABLE
all_pick : jumlah matchs dari game mode all pick
single_draft : jumlah matchs dari game mode single draft
'''
#total gamemode played
all_pick = 0
single_draft = 0

for mode in df20['game_mode']:
    if mode == 22:  
        all_pick = all_pick + 1
    elif mode == 4:
        single_draft = single_draft + 1
        
print('GAMEMODE PLAYED\t  ')
print('All-pick\t\t: ' + str(all_pick))
print('Single Draft\t: ' + str(single_draft))
print(68 * '-')




'''
blok code dibawah menampilkan data statistik dari duration selama 20 matchs 
terakhir. 

df20['duration'] merupakan durasi matchs dalam bentuk detik, agar terlihat 
lebih simpel program akan membagi 60 agar data menjadi dalam bentuk menit. 
data tersebut dibulatkan hingga dua angka terakhir dibelakang koma(,).

total durasi data didapatkan dengan sintaks df20['duration'].sum()
durasi maksimal didapatkan dengan sintaks df20['duration'].max()
durasi minimal didapatkan dengan sintaks df20['duration'].min()
rata-rata (average) durasi didapatkan dengan sintaks df20['duration'].mean()

PENJELASAN VARIABLE
total_duration : berisi total durasi (menit)
max_duration : berisi durasi terlama/maksimal (menit)
min_duration : berisi durasi tercepat/minimal (menit)
avg_duration : berisi rata-rata durasi (menit)
'''
#-Durasi Matchs
total_duration = round(df20['duration'].sum()/60, 2)
max_duration = round(df20['duration'].max()/60, 2)
min_duration = round(df20['duration'].min()/60, 2)
avg_duration = round(df20['duration'].mean()/60, 2)

print('DURATION STATISTICS')
print('Total\t: ' + str(total_duration) + ' Minutes')
print('Max\t\t: ' + str(max_duration) + '  Minutes')
print('Min\t\t: ' + str(min_duration) + '  Minutes')
print('Average\t: ' + str(avg_duration) + '  Minutes')
print(68 * '-')




''' 
blok code dibawah menampilkan data statistics dari kills, deaths, assists 
selama 20 matchs terakhir

untuk mendapat nilai total, maksimal, minimal, rata-rata dari kills, deaths,
dan assists menggunakan sintaks yang sama yaitu 
.sum() untuk mendapatkan nilai total, 
.max() untuk mendapatkan nilai maksimal, 
.min() untuk mendapatkan nilai minimal, 
.mean() untuk mendapatkan nilai rata2

yang membedakan mereka adalah kolom yang dipanggil, yaitu
df20['kills'] untuk kolom kills
df20['deaths'] untuk kolom deaths
df20['assists'] untuk kolom assists
'''
#-Kills, Deaths, Assists
print('KILL, DEATH, ASSIST\n')

print('*Kills')
print('Total\t: ' + str(df20['kills'].sum()) + '\n'
      'Max\t\t: ' + str(df20['kills'].max()) + '\n'
      'Min\t\t: ' + str(df20['kills'].min()) + '\n'
      'Average\t: ' + str(df20['kills'].mean()) + '\n')

print('*Death')
print('Total\t: ' + str(df20['deaths'].sum()) + '\n'
      'Max\t\t: ' + str(df20['deaths'].max()) + '\n'
      'Min\t\t: ' + str(df20['deaths'].min()) + '\n'
      'Average\t: ' + str(df20['deaths'].mean()) + '\n')

print('*Assist')
print('Total\t: ' + str(df20['assists'].sum()) + '\n'
      'Max\t\t: ' + str(df20['assists'].max()) + '\n'
      'Min\t\t: ' + str(df20['assists'].min()) + '\n'
      'Average\t: ' + str(df20['assists'].mean()) + '\n')
print(68 * '-')




'''
blok dibawah mencari nilai kda ratio tiap matchs dari data 20 matchs terakhir
kemudian dibuat kolom baru yaitu kolom 'kda', lalu ditampilkan

sebelum membuat kolom 'kda', program akan menghilangkan nilai null pada kolom
kills. kemudian dibuat kolom 'kda' dengan sintaks
df20['kda'] = round((df20['kills'] + df20['assists']) / df20['deaths'], 2)

kolom kda berisi kda ratio tiap matchs. rumus dari kda ratio adalah
    kda ratio = (kills + assist) / deaths

kemudian ditampilkan data total, maks, min, rata-rata dengan sintaks yang
sama dengan blok kode diatas, yaitu dengan sintaks .sum(), .max(), .min(),
.mean()

nilai dari sum() dan mean() dibulatkan 2 angka dibelakang koma dengan round() 
agar terlihat lebih simpel
'''
#-Informasi KDA Ratio
df20 = df20[df20['kills'].notnull()].copy()
df20['kda'] = round((df20['kills'] + df20['assists']) / df20['deaths'], 2)

print('KDA RATIO')
print('Total\t: ' + str(round(df20['kda'].sum(), 2)) + '\n'
      'Max\t\t: ' + str(df20['kda'].max()) + '\n'
      'Min\t\t: ' + str(df20['kda'].min()) + '\n'
      'Average\t: ' + str(round(df20['kda'].mean(), 2)) + '\n')

print('Terdapat diagram garis kda ratio pada plots\n')
print(68 * '-')




'''
blok program dibawah berfungsi untuk visualisasi data kda ratio tiap matchs

visualisasi ditampilkan dengan library matplotlib. plot dimodifikasi, sehingga 
warna garis menjadi merah dan dibuat grid agar visualisasi lebih jelas.

ISI PLOT
nilai dari x = total matchs
             = 20
             
nilai dari y = KDA ratio
             = tiap matchs memiliki value berbeda
'''
#-Visual KDA
x = []
for i in range (0, 20):
    x.append(i)

kill = df20['kills']
death = df20['deaths']
assist = df20['assists']
kda_ratio = df20['kda']

fig = plt.figure()
fig, ax = plt.subplots()

ax.plot(kda_ratio, label='KDA Ratio', color='red')
ax.set_xticks(x)
ax.grid(color='grey', linestyle='--')
ax.set_xlabel('Match 1-20')
ax.set_ylabel('KDA Ratio')
ax.legend()




'''
blok code dibawah mendapatkan data setiap hero yang ada di game dota 2. data
tersebut didapat dengan request dari API opendota dengan link
https://api.opendota.com/api/heroStats. data tersebut akan diubah menjadi 
json, kemudian diubah kembali menjadi csv

cara mengubah file json tersebut menjadi csv yaitu dengan sintaks csv.write()
kemudian tiap baris dari file json dimasukan kedalam kolom-kolom file csv
dengan looping. data tersebut disimpan dengan nama file hero_stats.csv

proses tersebut terdapat didalam get_hero_stats()

PENJELASAN VARIABLE
data : berisi data dari request dari API yang bertipe json
hero : memiliki isi yang sama dengan data
hero_file : merupakan file hero_stats.csv yang dibuka dengan sintaks open()
csv_writer : berisi file csv
'''
#-Get data hero dari API opendota
def get_hero_stats() :
    data = requests.get("https://api.opendota.com/api/heroStats").json()
    hero = data
    hero_file = open('/Not Data/Python/dota_statistics/hero_stats.csv', 'w')
    csv_writer = csv.writer(hero_file)
    count = 0
    for stat in hero:
        if count == 0:
            header = stat.keys()
            csv_writer.writerow(header)
            count += 1
        
        csv_writer.writerow(stat.values())
        
    hero_file.close()
        
# get_hero_stats() //sintaks untuk memindahkan data kedalam file csv. untuk
#                  //menghindari error program, sintaks ini dicomment




'''
blok dibawah membuat list/array yang berisi hero apa saja yang dipakai selama
20 matchs terakhir dengan jumlah berapa kali hero tersebut dipakai

pertama program akan membaca file hero_stats.csv untuk mendapakan data semua
hero yang ada di dota 2, terutamma nama dan id hero-nya
kemudian akan melakukan looping untuk mengisi list name yang didalamnya akan 
terdapat nama hero. cara mengisinya yaitu mendeteksi apakah hero_id dari 
id_hero sama dengan hero. jika ya, maka ditambahkan nama hero tersebut ke 
dalam list name[]

untuk mendapatkan jumlah pemakaian hero digunakan sintaks
heroes_count = [[i, heroes20.count(i)] for i in set(heroes20)]

PENJELASAN VARIABLE
'''
#mendapat nama hero dari csv hero
def get_hero_name(data20):
    hero_stat = pd.read_csv('/Not Data/Python/dota_statistics/hero_stats.csv')
    name = []
    
    for i, id_hero in data20.iterrows():
        for j, hero in hero_stat.iterrows():
            if id_hero['hero_id'] == hero['hero_id']:
                name.append(hero['localized_name'])
    return name

heroes20 = get_hero_name(df20)
heroes_count = [[i, heroes20.count(i)] for i in set(heroes20)]




'''
blok code dibawah menampilkan hero yang digunakan dengan jumlah berapa kali
hero tersebut digunakan

program akan melakukan looping untuk menampilkan hero dan jumlah pemakaian, 
looping dilakukan karena data tersebut disimpan didalam sebuah list dua 
dimensi (heroes_count). didalam looping, jika j == 0 maka data heroes_count[i][j]
akan disimpan sementara dalam temp, jika j != 0 akan ditampilkan 
print(temp + str(heroes_count[i][j]))

hal tersebut dilakukan agar tampilannya lebih menarik, menjadi : 
    winranger : 1
    .
    .
    phantom lancer : 2
'''
#menampilkan hero yang dimainkan dengan jumlah dimainkan
print('HEROES\n')

for i in range(0, len(heroes_count)):
    for j in range(0, 2):
        if j == 0:
            temp = str(heroes_count[i][j]) + ' : '
        else:
            print(temp + str(heroes_count[i][j]) + ' match')
   
print(58 * '=')
print()

