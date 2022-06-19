# Welcome to my youtube video downloader with python
# This downloader select the highest resolution of video + audio 
# Currently download bar is not yet available and will be implemented in the future.
# Enjoy!


#Using pytube library to download the videos
from pytube import YouTube

#Taking link as input and checking for validity
def valid():
    try :
        link = input("Please enter link :")
        youtube_link = YouTube(link)
    except:
        print("Incorrect Link")
        return False
    return youtube_link

#function to display information
def information(yt):
    print("Title :",yt.title)
    print("Author :",yt.author)
    print("Video lenght :",yt.length)

#Checking for user decision whether the video is the right one or not
def decision():
    user_choice = input("Is the information correct? [Y/N]").upper()
    if user_choice == "N":
        return False
    return True

#function that stores download function
def download(yt):
    yd = yt.streams.get_highest_resolution()
    yd.download("./download")

#function to determine repetition
def repeat():
    rep = input("repeat? [Y/N] ").upper()
    return rep

def main():
    rep = "Y" #repeat variable
    while rep == "Y":
        yt =valid()
        while not yt:
            yt = valid()
        information(yt)
        if decision():
            download(yt)
            print("Download Completed")
        rep = repeat()

if __name__ == "__main__":
    main()