from pytube import YouTube
url = input("Video Bağlantısını Giriniz:")
yt = YouTube(url)

video1 = yt.streams.filter(progressive=True).get_by_itag(22)
video1.download()

