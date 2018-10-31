""""This example is a program that interrupts/pauses
your study or work. Assuming your study session or work
lasts for 8 hours, it reminds you to take a
break after every 2hours from the time program starts running
opening a url to your favorite music video"""

import time
import webbrowser


print("Start time: " + time.ctime())
total_breaks = 4  # Number of breaks to be taken
break_count = 0  # Amount of times we've gone on break with an initial of 0.
url = "https://www.youtube.com/watch?v=mFI4LFbOeDc"  # A url to a music video. Change it to your link of choice.

while break_count < total_breaks:
    time.sleep(7200)  # Waiting time before carrying out task, Time is measured in seconds
    webbrowser.open(url)
    break_count += 1
    print("Break Time:" + time.ctime())
    print("Number of breaks: %d" % (break_count))

# Change the name <Absallam> to your name.
print("Hi Absallam, End of study session: " + time.ctime())
