# 0x13. Firewall

# More Info
As explained in the web stack debugging guide concept page, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:


# Tasks

## 0. Block all incoming traffic but
mandatory

Lets install the ufw firewall and setup a few rules on web-01.

Requirements:
- The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it wont be checked)
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
	- 22 (SSH)
	- 443 (HTTPS SSL)
	- 80 (HTTP)
- Share the ufw commands that you used in your answer file
