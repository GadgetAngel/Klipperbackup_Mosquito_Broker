## Klipper Backup of My Different 3D Printers Control Web Pages

I wanted a way to control the Tasmota power modules on my 3D printers and a way to access different
URL addresses that help me configure the corresponding printer.

This repository will contain the Index HTML files for these control web pages along with pictures of the web pages.

Resources I used to install the NGINX web server and the Mosquito broker:
1. [Install Mosquitto MQTT Broker on Raspberry Pi](https://randomnerdtutorials.com/how-to-install-mosquitto-broker-on-raspberry-pi/)
2. [Testing Mosquitto Broker and Client on Raspberry Pi](https://randomnerdtutorials.com/testing-mosquitto-broker-and-client-on-raspbbery-pi/)
3. [Build your own Raspberry Pi NGINX Web Server](https://pimylifeup.com/raspberry-pi-nginx/)
4. [SAMBA Setup - GCODE File Network Share Setup](https://github.com/rkolbi/voron2.4/tree/main/MY_V24-350#samba-setup---gcode-file-network-share-setup)
5. [The Solution to my CORS problem](https://gist.github.com/Stanback/7145487?permalink_comment_id=2824437#gistcomment-2824437)
6. [CORS setup for NGINX and PHP](https://gist.github.com/alexjs/4165271?permalink_comment_id=3373430#gistcomment-3373430)

For the mosquito broker server :
```
$ sudo nano /etc/nginx/sites-enabled/default
$ sudo nginx -t && sudo service php7.4-fpm restart && sudo service nginx restart
```

for the LDOkit :
```
$ sudo nano /etc/nginx/sites-available/resetrp2040.local.conf
$ sudo nginx -t && sudo service php7.4-fpm restart && sudo service nginx restart
``` 


---
## Main Web Page for All GadgetAngel 3D Printers

Here is a picture of the Main Web Page that is used to contain all the URL links to GadgetAngel's 3D Printers Web Control Pages:

![mainpage](/my_images/MainPrinterPage.jpg)

---
## Klipper Backup of the "LDO 300 Kit" Build Web Page Server

The files for the "LDO 300 kit" is located in the [LDO300Kit folder](/LDO300Kit/)

Here is the first section of the "LDO 300 Kit" web page:

![section 1](/LDO300Kit/my_images/Section_1.jpg)