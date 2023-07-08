import webbrowser 

def open_modified_url(original_url):
    
    if "youtu.be/" in original_url:
        modified_url = original_url.replace("youtu.be/", "youtubepp.com/watch?v=")
        
        webbrowser.open_new_tab(modified_url)
    
    elif "youtube.com" in original_url:
        modified_url = original_url.replace("youtube.com", "youtubepp.com")
        
        webbrowser.open_new_tab(modified_url)



print("Welcome to Youtube Video Downloader Prompt")

option = int(input("Choose an option: \n1. Download from YouTube video URL \n2. Download from YouTube video URL file\n--> "))

if option == 1:
    youtubeUrl = input("Enter YouTube Video URL/LINK: ")
    open_modified_url(youtubeUrl)
elif option == 2:
    youtubeUrlFile = input("Enter YouTube Video URL File Path: ")
    with open(youtubeUrlFile, "r", encoding="utf-8") as file:
        video_urls = file.read().splitlines()
    video_urls = [url.strip() for url in video_urls if url.strip()]
    print(f"Total links found in the file: {len(video_urls)}")
    count = 0
    for video_url in video_urls:
        
        open_modified_url(video_url)
        count += 1
    print(f"Total links opened: {count}")
