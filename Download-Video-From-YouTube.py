import yt_dlp

video_url = input("Enter YouTube video link: ")

try:
    ydl_opts = {'outtmpl': '%(title)s.%(ext)s'}  # Save as video title
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("Download completed!")
except Exception as e:
    print(f"An error occurred: {e}")

