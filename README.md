# SmallAutomations
Random small projects I am using to make life easier.


update.py - explanation. 
So for so small projects I ended up with a webhosting service.
Despite it being a great service, it only allows working within a set control panel. 
Which I havent quite figured out to automate updates, while I work towards making projects fully automated. 
To counter this, I created a small section on a RPI, that I use as my VPN when travelling to run a script to update for me. 
This script still has some untested sections (I have to learn ftp cli real quick). But it should be complete soon. 
Essentially this pulls a github version compares it with a hash of the previous version. 
If the hashes match it disregards and exits. It will likely become part of a cronjob I guess. 
If the hashes do not match, then the it should update through FTP (the part Im currently finishing).
