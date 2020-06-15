from pygame import mixer
mixer.init()
mixer.music.load("song.mp3")
mixer.music.play(10)

print("\t\t\t\t\t\t\t Tonmay Music Production")

while True:
    print("\t\t\t\t Press p for pause and r for resume and q for ")
    option = input()

    if option == "p" :
        mixer.music.pause()
    elif option == "r" :
        mixer.music.unpause()
    elif option == "q" :
        mixer.music.stop()
        break



