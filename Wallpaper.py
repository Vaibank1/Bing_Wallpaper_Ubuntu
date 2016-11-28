
#call the script


import os
os.system("./bing.sh")

#search the today's date file 
import glob
#newest = max(glob.iglob('/home/ankit/Pictures/bing-wallpapers/*.jpg'), key=os.path.getctime)

list_dir= glob.iglob('/home/ankit/Pictures/bing-wallpapers/*.jpg')
newest = max(list_dir, key=os.path.getctime)

commandToRun='gsettings set org.gnome.desktop.background picture-uri file://' + newest
os.system(commandToRun)