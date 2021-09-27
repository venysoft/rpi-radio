import keyboard
import vlc
from radio_list import radios
from win10toast import ToastNotifier

vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
radio_station_number = 0  # this number is used to choose station from list stored in radio_list.py the number represents index  number the first station in list is 0
notifi = True


class radio:
    def __init__(self, name, address):
        self.name = name
        self.address = address


# this function will stop alredy plaing station and change to the choosen sation
def play():
    global media
    player.stop()
    media = vlc_instance.media_new(radios[radio_station_number].address)
    print("playing "+radios[radio_station_number].name)
    player.set_media(media)

    player.play()


# this function stops the station if it's playing and plays it if ot's stopped


def stop(_):
    global player
    if player.is_playing() == True:
        print("stop")
        player.stop()
    else:
        print("play")
        play()

# this function changes radio_station_number to radio_station_number-1 in other word s it. In other words it changes to the next station


# the _ is used beacause keyboard.on_press sends keyboard event to the function
def previous_station(_):
    global radio_station_number
    radio_station_number = radio_station_number-1
    if radio_station_number == -1:
        radio_station_number = len(radios)-1
    play()

# this function changes radio_station_number to radio_station_number+1. In other words it changes to the previous station


def next_station(_):
    global radio_station_number
    radio_station_number = radio_station_number+1
    if radio_station_number >= len(radios):
        radio_station_number = 0

    play()


def station_name(_):
    # create windows notification with the name of curently playing station
    ToastNotifier().show_toast("playing "+radios[radio_station_number].name)


play()  # runs the default station on startup


keyboard.on_press_key("f12", next_station)
keyboard.on_press_key("f11", stop)
keyboard.on_press_key("f10", previous_station)
keyboard.on_press_key("f9", station_name)
input()
