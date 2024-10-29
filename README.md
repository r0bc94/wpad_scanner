# WPAD.dat Scanner

This is a simple scanner tool which reads all top level domains from the provided `TLDFILE` and
tries to connect to `http://wpad.tld/wpad.dat`. The tool is inspired by the talk at defcon24 refering to the
openly acessible _Web Proxy Autodiscovery Protocol_ configuration files. 
Please go ahead and watch it: https://www.youtube.com/watch?v=uwsykPWa5Lc&t=1599s

## What does this script do? 

It basically tries to obtain a wpad proxy configuration file from the open internet. If it suceeds, the results will
be written into an output file named `results.txt`. 
