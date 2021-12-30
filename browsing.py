import urllib.request
import re
import webbrowser
import main
    
#getting our url
main.speak("What would you like to search")
input = main.get_audio()
search = input.replace(" ","+")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
main_url = "https://www.youtube.com/watch?v=" + video_ids[0]

#opening the url
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open(main_url)