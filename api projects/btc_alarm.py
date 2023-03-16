import cryptocompare
from time import sleep
from pygame import mixer
import pyttsx3

mixer.init()
engine = pyttsx3.init()

tresh_dec = int(input('Enter decrease tresh'))
tresh_inc = int(input('Enter increase tresh'))
treshold = int(input('Enter the treshold'))

while True:
    sleep(4)
    btc_price = cryptocompare.get_price('BTC', currency='USD')['BTC']['USD']
    
    if btc_price < tresh_dec:
        mixer.music.load('alarm.mp3')
        mixer.music.play()
        print(f"Oh! btc decreased! {btc_price}")
        engine.say(f"btc is {btc_price}")
        engine.runAndWait()
        
        tresh_dec -= treshold
        tresh_inc -= treshold
        
    elif btc_price > tresh_inc:
        mixer.music.load('alarm2.mp3')
        mixer.music.play()
        print(f"Oh! btc increased! {btc_price}")
        engine.say(f"btc is {btc_price}")
        engine.runAndWait()
        
        tresh_dec += treshold
        tresh_inc += treshold
        
    else:
        print(f"{tresh_dec} < {btc_price} < {tresh_inc}")
