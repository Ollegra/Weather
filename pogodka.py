import ttkbootstrap as tk
from ttkbootstrap.dialogs import Messagebox
import requests
from datetime import datetime
import time
import json
#from geopy import GoogleV3
from timezonefinder import TimezoneFinder
import pytz
import locale

locale.setlocale(locale.LC_ALL, '')

par = {
    "lang": "ru",
    "lat": 50.9594,
    "lon": 28.6386,
    "appid": "0a8577490b8d30bfb89290cd0b8f9246",
    "units": "metric"
    # "cnt": 5
}


def power_bind(event):
    zapros()


def current_time(loc_lon, locv_lat):
    # geolocator = Nominatim(user_agent='geoapiExercises')
    # ocation = geolocator.geocode(name)
    #location = GoogleV3(
    #    api_key='AIzaSyCPzX7PCM5wy16eQ9OKnxpkxfSxRhole9c',
    #    domain='maps.google.ru').geocode(name)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=loc_lon, lat=locv_lat)
    home_time = pytz.timezone(result)
    local_time = datetime.now(home_time)
    time_current = local_time.strftime("%H:%M")
    loc_time.config(text=f'локальное время: {time_current}')


def zapros():
    s_name = gorod.get()
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" +
        s_name +
        "&APPID=0a8577490b8d30bfb89290cd0b8f9246&lang=ru&units=metric")
    r_hourly = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?q=" +
        s_name +
        "&APPID=0a8577490b8d30bfb89290cd0b8f9246&lang=ru&units=metric")
    data = r.json()
    city_lon = data.get('coord').get('lon')
    city_lat = data.get('coord').get('lat')
    current_time(city_lon, city_lat)
    try:
        descript = data.get("weather")[0].get("description")
    except TypeError:
        Messagebox.show_info('Внимание', 'Название города введено не верно! ')

    temp = data.get("main").get("temp")
    feel = data.get("main").get("feels_like")
    hum = data.get("main").get("humidity")
    press = int(data.get('main').get('pressure')) / 1.33
    wind_speed = data.get("wind").get("speed")
    d_img = data.get("weather")[0].get("icon") + '_.gif'
    sunrise = time.strftime('%H:%M:%S', time.gmtime(
        int(data.get('sys').get('sunrise')) + int(data.get('timezone'))))
    sunset = time.strftime('%H:%M:%S', time.gmtime(
        int(data.get('sys').get('sunset')) + int(data.get('timezone'))))
    # sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
    # sunset = datetime.fromtimestamp(data['sys']['sunset'])

    forecast = r_hourly.json().get('list')[0:]
    list_dat = []
    list_des = []
    list_min = []
    list_max = []
    list_icn = []
    list_wnd = []
    list_prs = []
    par6 = 4
    for i in forecast:
        idata = i.get('dt_txt')
        # print(idata)
        if idata[11:] == "12:00:00":
            list_dat.append(
                datetime.strptime(
                    i.get('dt_txt'),
                    '%Y-%m-%d %H:%M:%S').strftime('%d %b %a'))
            list_icn.append(i.get("weather")[0].get("icon") + '.gif')
            list_des.append(i.get("weather")[0].get("description"))
            list_min.append(i.get('main').get('temp'))
            list_max.append(i.get('main').get('feels_like'))
            list_wnd.append(i.get("wind").get("speed"))
            list_prs.append(int(i.get("main").get("pressure")) / 1.33)

    img_d1 = tk.PhotoImage(file="OW\\" + list_icn[0])
    img_d2 = tk.PhotoImage(file="OW\\" + list_icn[1])
    img_d3 = tk.PhotoImage(file="OW\\" + list_icn[2])
    img_d4 = tk.PhotoImage(file="OW\\" + list_icn[3])
    img_d5 = tk.PhotoImage(file="OW\\" + list_icn[4])
    img1 = tk.PhotoImage(file="OW\\" + d_img)
    lab0['image'] = img1
    lab0.image = img1
    lab1['text'] = f"{data.get('name')} {data.get('sys').get('country')}"
    lab2[
        'text'] = f"д. {data.get('coord').get('lon')}, ш. {data.get('coord').get('lat')} \n восход: {sunrise} \n закат: {sunset} "
    # lab3['text'] = f'Сейчас {descript}'
    lab4[
        'text'] = f"Сейчас {descript}\nТемпература: {temp} \N{DEGREE CELSIUS}, ощущается как {feel} \N{DEGREE CELSIUS} \nДавление: {press:.2f} мм.р.ст., Влажность: {hum} %,  \nСкорость ветра: {wind_speed} м/с"
    lab6['image'] = img_d1
    lab6.image = img_d1
    lab6[
        'text'] = f" {list_dat[0]} : {list_des[0]}, \n температура: {list_min[0]} \N{DEGREE CELSIUS}, ощущается как: {list_max[0]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[0]:.2f} м/с, давление: {list_prs[0]:.2f} мм.р.ст."
    lab7['image'] = img_d2
    lab7.image = img_d2
    lab7[
        'text'] = f" {list_dat[1]} : {list_des[1]}, \n температура: {list_min[1]} \N{DEGREE CELSIUS}, ощущается как: {list_max[1]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[1]:.2f} м/с, давление: {list_prs[1]:.2f} мм.р.ст."
    lab8['image'] = img_d3
    lab8.image = img_d3
    lab8[
        'text'] = f" {list_dat[2]} : {list_des[2]}, \n температура: {list_min[2]} \N{DEGREE CELSIUS}, ощущается как: {list_max[2]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[2]:.2f} м/с, давление: {list_prs[2]:.2f} мм.р.ст."
    lab9['image'] = img_d4
    lab9.image = img_d4
    lab9[
        'text'] = f" {list_dat[3]} : {list_des[3]}, \n температура: {list_min[3]} \N{DEGREE CELSIUS}, ощущается как: {list_max[3]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[3]:.2f} м/с, давление: {list_prs[3]:.2f} мм.р.ст."
    lab10['image'] = img_d5
    lab10.image = img_d5
    lab10[
        'text'] = f" {list_dat[4]} : {list_des[4]}, \n температура: {list_min[4]} \N{DEGREE CELSIUS}, ощущается как: {list_max[4]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[4]:.2f} м/с, давление: {list_prs[4]:.2f} мм.р.ст."


win = tk.Window(
    title='Прогноз погоды',
    themename='morph',
    resizable=(
        False,
        False))
photo = tk.PhotoImage(file="OW\\" + 'sun.gif')
win.iconphoto(False, photo)


r = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=par)
r_hourly = requests.get(
    'http://api.openweathermap.org/data/2.5/forecast?',
    params=par)
data = r.json()

with open('pogoda.json', 'w') as f:
    json.dump(data, f)
with open('pogoda2.json', 'w') as f:
    json.dump(r_hourly.json(), f)
descript = data.get("weather")[0].get("description")
temp = data.get("main").get("temp")
feel = data.get("main").get("feels_like")
hum = data.get("main").get("humidity")
press = int(data.get('main').get('pressure')) / 1.33
wind_speed = data.get("wind").get("speed")
d_img = data.get("weather")[0].get("icon") + '_.gif'
sunrise = time.strftime('%H:%M:%S', time.gmtime(
    int(data.get('sys').get('sunrise')) + int(data.get('timezone'))))
sunset = time.strftime('%H:%M:%S', time.gmtime(
    int(data.get('sys').get('sunset')) + int(data.get('timezone'))))
# sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
# sunset = datetime.fromtimestamp(data['sys']['sunset'])

forecast = r_hourly.json().get('list')[0:]
list_dat = []
list_des = []
list_min = []
list_max = []
list_icn = []
list_wnd = []
list_prs = []
par6 = 4
for i in forecast:
    idata = i.get('dt_txt')
    # print(idata)
    if idata[11:] == "12:00:00":
        list_dat.append(
            datetime.strptime(
                i.get('dt_txt'),
                '%Y-%m-%d %H:%M:%S').strftime('%d %b %a'))
        list_icn.append(i.get("weather")[0].get("icon") + '.gif')
        list_des.append(i.get("weather")[0].get("description"))
        list_min.append(i.get('main').get('temp'))
        list_max.append(i.get('main').get('feels_like'))
        list_wnd.append(i.get("wind").get("speed"))
        list_prs.append(int(i.get("main").get("pressure")) / 1.33)

# print(list_icn)
img_d1 = tk.PhotoImage(file="OW\\" + list_icn[0])
img_d2 = tk.PhotoImage(file="OW\\" + list_icn[1])
img_d3 = tk.PhotoImage(file="OW\\" + list_icn[2])
img_d4 = tk.PhotoImage(file="OW\\" + list_icn[3])
img_d5 = tk.PhotoImage(file="OW\\" + list_icn[4])
img1 = tk.PhotoImage(file="OW\\" + d_img)
lab0 = tk.Label(win, image=img1)
lab0.grid(row=0, column=0, stick='wens', padx=15)
lab1 = tk.Label(
    win,
    text=f"{data.get('name')} {data.get('sys').get('country')}",
    foreground='red',
    font=(
        'Tahoma',
        12,
         'bold'))
lab1.grid(row=1, column=0, stick='wens', padx=15, pady=5)
lab2 = tk.Label(
    win,
    anchor='e',
    text=f"д. {data.get('coord').get('lon')}, ш. {data.get('coord').get('lat')}, \n восход: {sunrise} \n закат: {sunset} ",
    foreground='grey',
    font=(
        'Arial',
        8,
         'italic'))
lab2.grid(row=0, column=1, stick='wens', padx=7)
local_time = datetime.now()
time_current = local_time.strftime("%H:%M")
loc_time = tk.Label(
    win,
    anchor='c',
    text=f'локальное время: {time_current}',
    foreground='grey',
    font=(
        'Arial',
        8,
         'italic'))
loc_time.grid(row=1, column=1, stick='wens')

lab4 = tk.Label(
    win,
    relief='groove',
    anchor='center',
    text=f"Сейчас {descript}\nТемпература: {temp} \N{DEGREE CELSIUS}, ощущается как {feel} \N{DEGREE CELSIUS} \nДавление: {press:.2f} мм.р.ст., Влажность: {hum} %,  \nСкорость ветра: {wind_speed} м/с",
    foreground='blue',
    font=(
        'Arial',
         10))
lab4.grid(row=3, column=0, stick='wens', padx=5, pady=1, columnspan=2)
lab6 = tk.Label(
    win,
    relief='groove',
    image=img_d1,
    text=f" {list_dat[0]} : {list_des[0]}, \n температура: {list_min[0]} \N{DEGREE CELSIUS}, ощущается как: {list_max[0]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[0]:.2f} м/с, давление: {list_prs[0]:.2f} мм.р.ст.",
    compound='left',
    foreground='black',
    font=(
        'Arial',
         10))
lab6.grid(row=5, column=0, stick='wens', padx=5, pady=1, columnspan=2)
lab7 = tk.Label(
    win,
    relief='groove',
    image=img_d2,
    text=f" {list_dat[1]} : {list_des[1]}, \n температура: {list_min[1]} \N{DEGREE CELSIUS}, ощущается как: {list_max[1]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[1]:.2f} м/с, давление: {list_prs[1]:.2f} мм.р.ст.",
    compound='left',
    foreground='black',
    font=(
        'Arial',
         10))
lab7.grid(row=6, column=0, stick='wens', padx=5, pady=1, columnspan=2)
lab8 = tk.Label(
    win,
    relief='groove',
    image=img_d3,
    text=f" {list_dat[2]} : {list_des[2]}, \n температура: {list_min[2]} \N{DEGREE CELSIUS}, ощущается как: {list_max[2]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[2]:.2f} м/с, давление: {list_prs[2]:.2f} мм.р.ст.",
    compound='left',
    foreground='black',
    font=(
        'Arial',
         10))
lab8.grid(row=7, column=0, stick='wens', padx=5, pady=1, columnspan=2)
lab9 = tk.Label(
    win,
    relief='groove',
    image=img_d4,
    text=f" {list_dat[3]} : {list_des[3]}, \n температура: {list_min[3]} \N{DEGREE CELSIUS}, ощущается как: {list_max[3]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[3]:.2f} м/с, давление: {list_prs[3]:.2f} мм.р.ст.",
    compound='left',
    foreground='black',
    font=(
        'Arial',
         10))
lab9.grid(row=8, column=0, stick='wens', padx=5, pady=1, columnspan=2)
lab10 = tk.Label(
    win,
    relief='groove',
    image=img_d5,
    text=f" {list_dat[4]} : {list_des[4]}, \n температура: {list_min[4]} \N{DEGREE CELSIUS}, ощущается как: {list_max[4]} \N{DEGREE CELSIUS}, \n ветер: {list_wnd[4]:.2f} м/с, давление: {list_prs[4]:.2f} мм.р.ст.",
    compound='left',
    foreground='black',
    font=(
        'Arial',
         10))
lab10.grid(row=9, column=0, stick='wens', padx=5, pady=1, columnspan=2)

gorod = tk.Entry(win, justify='center', width=25, foreground='blue')
gorod.bind('<FocusIn>', lambda e: gorod.delete('0', 'end'))
gorod.bind('<Return>', power_bind)
gorod.grid(row=10, column=0, stick='wens', padx=10, pady=10)
gorod.insert(0, 'Korosten')
butn = tk.Button(
    win,
    bootstyle='outline-primary',
    width=25,
    text='Обновить',
    command=zapros)
butn.grid(row=10, column=1, stick='wens', padx=10, pady=10)

win.update_idletasks()
mw = win.geometry()
mw = mw.split('+')
mw = mw[0].split('x')
w_win = int(mw[0])
h_win = int(mw[1])
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
ws = ws // 2 - w_win // 2
hs = hs // 2 - h_win // 2
win.geometry(f'+{ws}+{hs}')

# win.grid_columnconfigure(0, minsize=100)
# print(lab0.winfo_reqwidth())
# win.grid_rowconfigure(0, minsize=50)

win.mainloop()
