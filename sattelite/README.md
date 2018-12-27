# Client Icinga 2 monitoring created with Ansible playbooks

# Requirements
- On the machine which will exectute these playbooks there has to be PBKF2 PIP module installed.
- ```pip install pbkf2```
- If you don't have ```pip``` installed you can get it here https://pip.pypa.io/en/stable/installing/  

# Recommendations:
- If you're on macOS don't install Ansible using ```brew```. Use ```pip``` instead.
- ```pip install ansible```

# How to use?
- Create an __inventory__ file and add the IP addresses of computers you wish to execute these playbooks on.
- Change variables ```playbooks/sattelite/vars/mains.yml```:
  - ```icinga2_master_ip``` - IP address of the Icinga 2 master server.
  - ```icinga2_ticket_salt``` - you can get this using ```master/get_master_ticket_salt.sh``` script
- Run ```ansible-playbook -i hosts playbooks/site.yml``` - assuming you inventory file is named hosts