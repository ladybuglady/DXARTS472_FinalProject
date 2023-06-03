import pyfirmata
from pyfirmata import Arduino, util, STRING_DATA
import word_gen
import random
import time

# https://gist.github.com/varlen/91170e7cdd61032107e833fce6b7106a

# https://pubmed.ncbi.nlm.nih.gov/28445740/


#ser = serial.Serial('/dev/cu.usbmodem142201', 9800, timeout=1)
#print(ser.readline())
board = pyfirmata.Arduino('/dev/cu.usbmodem1422301') # this sometimes need to change. Check port.
board.send_sysex( STRING_DATA, util.str_to_two_byte_iter('starting up!') ) 
print("Starting up!")

# Pins
left = 13
cer = 12
amy = 11
right = 10

board.digital[left].write(0)
board.digital[right].write(0)
board.digital[amy].write(0)
board.digital[cer].write(0)

emotions = ['sadness', 'anger', 'neutral', 'love', 'surprise', 'fear', 'happy', 'worry']
good_emotions = ['love', 'surprise', 'happy']
sad_emotions = ['sadness', 'neutral', 'worry']
anxious_emotions = ['anger', 'fear']

it = pyfirmata.util.Iterator(board)
it.start()

#time.sleep(1)
sensor = board.get_pin('a:0:i')
mic = board.get_pin('a:1:i')

def msg( text ):
    if text:
        board.send_sysex( STRING_DATA, util.str_to_two_byte_iter( text ) )

time.sleep(3)

while True:
    distance = sensor.read() * 100

    hear = False

    # Need a range of time to detect sound
    for i in range(1000):
        volume = mic.read() * 1000
        if volume > 1000:
            hear=True
            print("     I hear you...")
            msg("I hear you...")
            break
    
    #print("VOL: ", volume)
    #print("DISTANCE: ", distance)

    if distance > 100 and volume > 1000:

        emo = "love"
        say, theme = word_gen.theme_emotion_selector(emo)
    
        print("     I feel connected to you.")
        msg("I feel connected to you.")
        print("     Activating all regions.")
        board.digital[left].write(1)
        board.digital[right].write(1)
        board.digital[amy].write(1)
        board.digital[cer].write(1)

        #time.sleep(5)
        print("     I feel ")
        #time.sleep(1)
        print("     "+emo)
        time.sleep(2)
        print("     I'm thinking")
        print("         about ")
        print("     "+theme)
        print("     Don't go.")
        msg("Don't go.")


    elif distance > 95 or hear:
        entry = random.choice(["Well hello", "See me", "Stop talking", "Be quiet!", "Don't tell me what to do", 
                               "I don't want to work", "Come closer...", "Let's talk!", "There you are!"])
        
        print("     "+entry)

        emo = random.choice(good_emotions)
        say, theme = word_gen.theme_emotion_selector(emo)

        #print("Emotion:")
        #print(emo)
        
        print("     I can hear you...")
        print("     I feel ")
        #time.sleep(1)
        print("     "+emo)
        time.sleep(2)
        print("     I'm thinking")
        print("     about ")
        print("     "+theme)
        time.sleep(2)

        print("     Activating all regions.")
        board.digital[left].write(1)
        board.digital[right].write(1)
        board.digital[amy].write(1)
        board.digital[cer].write(1)


    else: 
        #print("     I am alone.")
        emo = random.choice(sad_emotions + anxious_emotions)
        say, theme = word_gen.theme_emotion_selector(emo)

        print("     I feel ")
        #time.sleep(1)
        print("     "+emo)
        time.sleep(2)
        print("     I'm thinking")
        print("     about ")
        print("     "+theme)
        
        if emo == 'neutral':
            print("     Activating brain stem.")
            board.digital[cer].write(1)
            board.digital[left].write(0)
            board.digital[right].write(0)
            board.digital[amy].write(0)

        elif emo in sad_emotions:
            print("     Activating left brain.")
            board.digital[left].write(1)
            board.digital[right].write(0)
            board.digital[amy].write(0)
            board.digital[cer].write(0)

        elif emo in anxious_emotions:
            print("     Activating amygdala.")
            board.digital[amy].write(1)
            board.digital[left].write(0)
            board.digital[right].write(0)
            board.digital[cer].write(0)


        
    print()
    print("     Statement:")
    print("     "+say)
    print()
    time.sleep(10)
    i = 0
    
    
    