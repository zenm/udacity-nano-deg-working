import time
import webbrowser

session = 0
total_sessions = 3

while session < total_sessions:
    print("Started on " + time.ctime())
    time.sleep(10)
    webbrowser.open('https://www.youtube.com/watch?v=RDZqIUfzDAc')
    session += 1
