'''
    Description: Get information from Youtube in a simple way.
    Author: aulerjbailey
    Version: 0.1.0
'''
import AVMYT as yt

channel = yt.getChannelInfo("luisito") # get channel
print(channel["name"] + " tiene " + channel["subs"] + " y un total de " + channel["videos"]) # prints info of Luisito Comunica