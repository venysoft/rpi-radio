from gpiozero import Button
import vlc
from signal import pause
from radio_list import radios

but1 = Button(13)
but2 = Button(5)
but3 = Button(6)
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()
radio_station_number = 0  # this number is used to choose station from list stored in radio_list.py the number represents index  number the first station in list is 0


# this function will stop alredy plaing station and change to the choosen sation
def play():
    global media
    player.stop()
    media = vlc_instance.media_new(radios[radio_station_number].address)
    print("playing "+radios[radio_station_number].name)
    player.set_media(media)
    player.play()

# this function stops the station if it's playing and plays it if ot's stopped


def stop():
    global player
    if player.is_playing() == True:
        print("stop")
        player.stop()
    else:
        print("play")
        play()

# this function changes radio_station_number to radio_station_number-1 in other word s it. In other words it changes to the next station


def previous_station():
    global radio_station_number
    radio_station_number = radio_station_number-1
    if radio_station_number == -1:
        radio_station_number = len(radios)-1
    play()

# this function changes radio_station_number to radio_station_number+1. In other words it changes to the previous station


def next_station():
    global radio_station_number
    radio_station_number = radio_station_number+1
    if radio_station_number >= len(radios):
        radio_station_number = 0

    play()


play()  # runs the default station on startup

# runs functions when button is pressed
but1.when_pressed = previous_station
but2.when_pressed = stop
but3.when_pressed = next_station


pause()
