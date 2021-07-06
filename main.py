from logging import exception
import pytube  
from pytube import YouTube  
userInput = input("Enter the link of the Youtube video:   ")
try:
    video_url = userInput   
    youtube = pytube.YouTube(video_url)  
    video = youtube.streams.first()  
    video.download('E:/')  
except Exception as e:
    print("error")