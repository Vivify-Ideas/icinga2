# This repo contains everything needed for monitoring PCs with Icinga 2.

## How to use?

### Icinga 2 has to be run on a master server which will poll clients for data, and also on client PCs which will respond to the master server.

- Inside ```master``` directory there is a Docker configuration which, when started will run Icinga 2 monitoring service and make it available at https://localhost/icingaweb2.
More info inside.

- Inside ```sattelite``` directory there is an Ansible configuration which will set everything up required to run Icinga 2 monitoring service on a client computer and also it will connect that computer to the master server defined in master directory. More info inside.