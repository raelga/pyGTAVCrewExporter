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

** [505] rael@mbw:~/ws/gtav_crew_exporter$ ./gtav_crew_exporter.py -c the_pollasos -u raelga -p *********** **

```
./gtav_crew_exporter.py -c the_pollasos -u raelga -p *********
Crew: the_pollasos
Crew Size: 9 members
Member: adrianrgvez
[adrianrgvez] main crew: the_pollasos
[adrianrgvez] PSN ID: --
[adrianrgvez] country: Spain
Member: corderius10
[corderius10] main crew: the_pollasos
[corderius10] PSN ID: --
[corderius10] country: Spain
Member: oscartc14
[oscartc14] main crew: the_pollasos
[oscartc14] PSN ID: --
[oscartc14] country: Spain
Member: alfi_de_pumarin9
[alfi_de_pumarin9] main crew: the_pollasos
[alfi_de_pumarin9] PSN ID: --
[alfi_de_pumarin9] country: Spain
Member: capableuncle3020
capableuncle3020 profile is private.
Member: rodri799
[rodri799] main crew: the_pollasos
[rodri799] PSN ID: --
[rodri799] country: Spain
Member: yex_gr
[yex_gr] main crew: the_pollasos
[yex_gr] PSN ID: yex_
[yex_gr] country: Spain
Member: OrignalBEAST
[OrignalBEAST] main crew: lossantosdiamondz
[OrignalBEAST] PSN ID: ORIGNALBEASSTT
[OrignalBEAST] country: United Kingdom
Member: raelga
[raelga] main crew: elotrolado
[raelga] PSN ID: raelga
[raelga] country: Spain
```

## And more?

Follow [@raelga](http://twitter.com/raelga) on Twitter for the latest news.

For feedback, just contact me.
