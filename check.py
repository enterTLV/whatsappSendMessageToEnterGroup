import sys
import pywhatkit
import datetime
hours = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute + 1
file = open("message.txt", 'r')
message = str(file.read())
print(message)

pywhatkit.sendwhatmsg_to_group("HOYGYfwPu15H9ElvMqXUSJ", message, hours, minutes)
