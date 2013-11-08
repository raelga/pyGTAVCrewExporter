gtav_crew_exporter
==================

Get information about crew members on Rockstar GTAV social club.

You need: 

python and selenium


Install:

Linux:

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


Mac
Install Python and then

# sudo pip install selenium

Windows:

I guess the samne as Mac
