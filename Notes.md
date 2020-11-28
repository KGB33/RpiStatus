# Getting the host's IP

One solution found online was to use `socket.gethostbyname(socket.gethostname())`
This "works" but not really, it gets the IP addr defined in `/etc/hosts`,
regardless of it is the acctual IP addr of the device.

A better solution is to parse the output if the `ip` command using the `-j` flag.
This formats the output in json, making it super easy to parse. Also, this command
gives the ip addr of every NIC, not just the ip thats defined in `/etc/hosts`
