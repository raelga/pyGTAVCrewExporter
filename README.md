# gtav_crew_exporter
==================

## Overview
Get information about crew members on Rockstar GTAV social club.

## Prerequisites
==================


* python | <http://www.python.org/download/>
* selenium for python | <https://pypi.python.org/pypi/selenium>
* firefox | <http://www.mozilla.org/en-US/firefox/new/>

** Firefox must be in english due to Rockstar Social Club source code, in the final version it will not be necessary. **


### Installation

##### Linux

**\# aptitude install python-pip**

**\# easy_install selenium**

```                                                                 
[327] root@eva:~# aptitude install python-pip
The following NEW packages will be installed:
  python-pip python-pkg-resources{a} python-setuptools{a}
0 packages upgraded, 3 newly installed, 0 to remove and 18 not upgraded.

Need to get 648 kB of archives. After unpacking 2,938 kB will be used.
Do you want to continue? [Y/n/?] y
Get: 1 http://ftp.es.debian.org/debian/ jessie/main python-pkg-resources all 0.6.49-2 [62.5 kB]
Get: 2 http://ftp.es.debian.org/debian/ jessie/main python-setuptools all 0.6.49-2 [320 kB
Get: 3 http://ftp.es.debian.org/debian/ jessie/main python-pip all 1.4.1-2 [266 kB
Fetched 648 kB in 2s (223 kB/s)       
Selecting previously unselected package python-pkg-resources.
(Reading database ... 156790 files and directories currently installed.)
Unpacking python-pkg-resources (from .../python-pkg-resources_0.6.49-2_all.deb) ...
Selecting previously unselected package python-setuptools.
Unpacking python-setuptools (from .../python-setuptools_0.6.49-2_all.deb) ...
Selecting previously unselected package python-pip.
Unpacking python-pip (from .../python-pip_1.4.1-2_all.deb) ...
Processing triggers for man-db ...
Setting up python-pkg-resources (0.6.49-2) ...
Setting up python-setuptools (0.6.49-2) ...
Setting up python-pip (1.4.1-2) ...                                                                    
[328] root@eva:~# easy_install selenium
Searching for selenium
Reading http://pypi.python.org/simple/selenium/
Best match: selenium 2.37.2
Downloading https://pypi.python.org/packages/source/s/selenium/selenium-2.37.2.tar.gz#md5=f3fffaae0bc789676c4e2ab285f7b04f
Processing selenium-2.37.2.tar.gz
Writing /tmp/easy_install-shFcgY/selenium-2.37.2/setup.cfg
Running selenium-2.37.2/setup.py -q bdist_egg --dist-dir /tmp/easy_install-shFcgY/selenium-2.37.2/egg-dist-tmp-_CdLcZ
Adding selenium 2.37.2 to easy-install.pth file

Installed /usr/local/lib/python2.7/dist-packages/selenium-2.37.2-py2.7.egg
Processing dependencies for selenium
Finished processing dependencies for selenium
```


##### Mac

Download and install python from

<http://www.python.org/download/>

Then install selenium using pip:

**$ sudo pip install selenium**

```
[502] rael@mbw:~$ sudo pip install selenium
Downloading/unpacking selenium
  Downloading selenium-2.37.2.tar.gz (2.6MB): 2.6MB downloaded
  Running setup.py egg_info for package selenium
    
Installing collected packages: selenium
  Running setup.py install for selenium
    
Successfully installed selenium
Cleaning up...
```


##### Windows

Not tested yet, but I guess similar as in Mac.



## Usage
==================


Basic usage

### Command interface

```
./gtav_crew_exporter.py --help
gtav_crew_exporter.py -c <crew_name> [-u <username> -p <password>] [-o <output_file>] [-v]
```

##### --help
	View the basic usage
##### -c, --crew=
	The name of the crew to export
#####  -u, --username=
	The username of your Rockstar social club (needed to view each user information, only crew hierarchy information is public).
#####  -p, --password=
	The password of your Rockstar social club (needed to view each member information, only crew hierarchy information is public).
#####  -o
	Output file, not implemented yet.
#####  -v
	Verbose mode, for debug.

### Examples



#### Only members and ranks

** [501] rael@mbw:~/ws/gtav_crew_exporter$ ./gtav_crew_exporter.py -c elotrolado **

```
./gtav_crew_exporter.py -c elotrolado
Crew: elotrolado
Crew Size: 300 members
!! Without login and password, only username and rank are available:
Crew Members :
leader, nihael, http://socialclub.rockstargames.com/member/nihael
commissioner, FJTR23, http://socialclub.rockstargames.com/member/fjtr23
lieutenant, Racso25, http://socialclub.rockstargames.com/member/racso25
representative, AntonLaveyX, http://socialclub.rockstargames.com/member/antonlaveyx
representative, beerna, http://socialclub.rockstargames.com/member/beerna
representative, lierhoff, http://socialclub.rockstargames.com/member/lierhoff
representative, raelga, http://socialclub.rockstargames.com/member/raelga
representative, rubi7410, http://socialclub.rockstargames.com/member/rubi7410
representative, Sd-Snatcher, http://socialclub.rockstargames.com/member/sd-snatcher
muscle, _XiloX_, http://socialclub.rockstargames.com/member/_xilox_
muscle, 4LUFLiNT, http://socialclub.rockstargames.com/member/4luflint
muscle, A_Rebato, http://socialclub.rockstargames.com/member/a_rebato
```

#### With member information (need login and password)

** [505] rael@mbw:~/ws/gtav_crew_exporter$ ./gtav_crew_exporter.py -c the_pollasos -u raelga -p xxxxxxxxx **

```
./gtav_crew_exporter.py -c the_pollasos -u raelga -p *********
Crew: the_pollasos
Crew Size: 9 members
adrianrgvez, Spain, , PS3, the_pollasos, leader, 108,  5D 4H 17M, All ok.
corderius10, Spain, , PS3, the_pollasos, commissioner, 79,  78H 42M 24S, All ok.
oscartc14, Spain, , PS3, the_pollasos, lieutenant, 11,  8H 34M 36S, All ok.
alfi_de_pumarin9, Spain, , PS3, the_pollasos, representative, 24,  17H 23M 9S, All ok.
capableuncle3020, , , , , representative, , , Private profile.
rodri799, Spain, , PS3, the_pollasos, representative, 12,  14H 47M 50S, All ok.
yex_gr, Spain, yex_, PS3, the_pollasos, representative, 21,  24H 50M 26S, All ok.
OrignalBEAST, United Kingdom, ORIGNALBEASSTT, PS3, lossantosdiamondz, muscle, 24,  48H 40M 23S, All ok.
raelga, Spain, raelga, PS3, elotrolado, muscle, 65,  6D 13H 53M, All ok.
```

#### With member information (need login and password) and file as output

** [505] rael@mbw:~/ws/gtav_crew_exporter$ ./gtav_crew_exporter.py -c the_pollasos -u raelga -p xxxxxxxxx **

```
./gtav_crew_exporter.py -c The_pollasos -u raelga -p ********* -o pollasos.csv
Crew: The_pollasos
Output file : pollasos.csv
Crew Size: 9 members
Output saved as pollasos.csv.
```

#### Verbose mode

** [505] rael@mbw:~/ws/gtav_crew_exporter$ ./gtav_crew_exporter.py -c the_pollasos -u raelga -p xxxxxxxxx -v **

```
./gtav_crew_exporter.py -v -c the_pollasos -u raelga -p *********
Crew: the_pollasos
DBG : web - starting browser
DBG : web - page fully loaded!
DBG : web - set page in english.
DBG : web - all users visible.
Crew Size: 9 members
DBG : web - page fully loaded!
DBG : web - page fully loaded!
DBG : [adrianrgvez]
DBG : web - page fully loaded!
DBG : [adrianrgvez] main crew: the_pollasos
DBG : [adrianrgvez] PSN ID: 
DBG : [adrianrgvez] country: Spain
DBG : web - page fully loaded!
DBG : [adrianrgvez] rank: leader
DBG : [adrianrgvez] playtime:  5D 4H 20M
DBG : [corderius10]
DBG : web - page fully loaded!
DBG : [corderius10] main crew: the_pollasos
DBG : [corderius10] PSN ID: 
DBG : [corderius10] country: Spain
DBG : web - page fully loaded!
DBG : [corderius10] rank: commissioner
DBG : [corderius10] playtime:  78H 42M 24S
DBG : [oscartc14]
DBG : web - page fully loaded!
DBG : [oscartc14] main crew: the_pollasos
DBG : [oscartc14] PSN ID: 
DBG : [oscartc14] country: Spain
DBG : web - page fully loaded!
DBG : [oscartc14] rank: lieutenant
DBG : [oscartc14] playtime:  8H 34M 36S
DBG : [alfi_de_pumarin9]
DBG : web - page fully loaded!
DBG : [alfi_de_pumarin9] main crew: the_pollasos
DBG : [alfi_de_pumarin9] PSN ID: 
DBG : [alfi_de_pumarin9] country: Spain
DBG : web - page fully loaded!
DBG : [alfi_de_pumarin9] rank: representative
DBG : [alfi_de_pumarin9] playtime:  17H 23M 9S
DBG : [capableuncle3020]
DBG : web - page fully loaded!
DBG : [capableuncle3020] Profile is private!
DBG : [rodri799]
DBG : web - page fully loaded!
DBG : [rodri799] main crew: the_pollasos
DBG : [rodri799] PSN ID: 
DBG : [rodri799] country: Spain
DBG : web - page fully loaded!
DBG : [rodri799] rank: representative
DBG : [rodri799] playtime:  14H 47M 50S
DBG : [yex_gr]
DBG : web - page fully loaded!
DBG : [yex_gr] main crew: the_pollasos
DBG : [yex_gr] PSN ID: ***
DBG : [yex_gr] country: Spain
DBG : web - page fully loaded!
DBG : [yex_gr] rank: representative
DBG : [yex_gr] playtime:  24H 50M 26S
DBG : [OrignalBEAST]
DBG : web - page fully loaded!
DBG : [OrignalBEAST] main crew: lossantosdiamondz
DBG : [OrignalBEAST] PSN ID: ***
DBG : [OrignalBEAST] country: United Kingdom
DBG : web - page fully loaded!
DBG : [OrignalBEAST] rank: muscle
DBG : [OrignalBEAST] playtime:  48H 40M 23S
DBG : [raelga]
DBG : web - page fully loaded!
DBG : [raelga] main crew: elotrolado
DBG : [raelga] PSN ID: raelga
DBG : [raelga] country: Spain
DBG : web - page fully loaded!
DBG : [raelga] rank: muscle
DBG : [raelga] playtime:  6D 13H 53M
adrianrgvez, Spain, , PS3, the_pollasos, leader, 108,  5D 4H 20M, All ok.
corderius10, Spain, , PS3, the_pollasos, commissioner, 79,  78H 42M 24S, All ok.
oscartc14, Spain, , PS3, the_pollasos, lieutenant, 11,  8H 34M 36S, All ok.
alfi_de_pumarin9, Spain, , PS3, the_pollasos, representative, 24,  17H 23M 9S, All ok.
capableuncle3020, , , , , representative, , , Private profile.
rodri799, Spain, , PS3, the_pollasos, representative, 12,  14H 47M 50S, All ok.
yex_gr, Spain, ****, PS3, the_pollasos, representative, 21,  24H 50M 26S, All ok.
OrignalBEAST, United Kingdom, ****, PS3, lossantosdiamondz, muscle, 24,  48H 40M 23S, All ok.
raelga, Spain, raelga, PS3, elotrolado, muscle, 65,  6D 13H 53M, All ok.
```

## And more?

Follow [@raelga](http://twitter.com/raelga) on Twitter for the latest news.

For feedback, just contact me.
