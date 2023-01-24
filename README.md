## Python reverse shell

Reverse shells force the target to execute some code that connects back to your computer.

Script send code to the target machine, and setup a listener on your machine.

Afterwards you can run the payload and get a reverse shell on you machine.

Since the target machine is connecting to our machine, we can avoid firewalls.

# Basic configuration

 * `SERVER_HOST` - 0.0.0.0 by default to make server listening on all IPs. This can be changed to eg. localhost or 127.0.0.1
 
 * `SERVER_PORT` - 7001 by default, can be changed to other unused port above 1024. Sometimes it's useful to change port to 80 or 443 in order to bypass firewall restrictions

