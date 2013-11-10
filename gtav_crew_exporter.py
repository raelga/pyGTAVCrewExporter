#!/usr/bin/python


#### Import modules
from selenium import selenium
from selenium import webdriver
import sys, time, re, string, getopt

#### Constants
default_crew = 'elotrolado'
login_url = 'https://socialclub.rockstargames.com/profile/signin'
base_crew_url = 'http://socialclub.rockstargames.com/crew'
path_gtav_base_url = '/games/gtav'
path_gtav_overview_url = '/career/overview/gtaonline'

#### Global
username = ''
password = ''
crew_name = ''
output_file = ''
verbose_flag = ''

#### Class definition
class crew_member:
    def __init__(self):
        self.id = ''
        self.psn = ''
        self.url = ''
        self.level = ''
        self.playtime = ''
        self.country = ''
        self.rank = ''
        self.crew = ''
        self.platform = ''
        self.error = 'All ok.'

#### Function definitions

def print_help():
    print 'gtav_crew_exporter.py -c <crew_name> [-u <username> -p <password>] [-o <output_file>] [-v]'

def arg_parser(argv):
    global crew_name
    global username
    global password
    global output_file
    global verbose_flag
    try:
        opts, args = getopt.getopt(argv,"hvu:p:c:o:",["verbose","username","password","crew=","ofile="])
    except getopt.GetoptError:
        print_help()
        debug(2)
    for opt, arg in opts:
        if opt == '-h':
            print_help()
            debug()
        elif opt in ("-c", "--crew"):
            crew_name = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg
            if not output_file: print_help()
        elif opt in ("-v", "--verbose"):
            verbose_flag = 1
        elif opt in ("-u", "--username"):
            username = arg
            if not username: print_help()
        elif opt in ("-p", "--password"):
            password = arg
            if not password: print_help()

    if not crew_name:
        crew_name = default_crew

    return 0

def debug(msg):
    global verbose_flag
    if verbose_flag: print 'DBG : ' + msg

def WaitForElement(webdriver, path):
    limit = 10   # waiting limit in seconds
    inc = 1   # in seconds; sleep for 500ms
    c = 0
    while (c < limit):
        try:
            webdriver.find_element_by_xpath(path)
            return 1        # Success
        except:
            time.sleep(inc)
            c = c + inc 
 
    # print sys.exc_info()
    return 0   

####
def LoginSocialClub(driver):

    if not username or not password:
        print '!! Without login and password, only username and rank are available:'
        return 1
    
    driver.get(login_url)
        
    path = '//*[@id="submitBtn"]'
    result = WaitForElement(driver, path)

    if not result:              # interprets returned value
    #        driver.close()
        debug("\nThe page is not loaded yet.")
    else:
        debug('web - page fully loaded!')

    path='//input[@id="login-field"]'
    driver.find_element_by_xpath(path).clear()
    driver.find_element_by_xpath(path).send_keys(username)

    path='//input[@id="password-field"]'
    driver.find_element_by_xpath(path).clear()
    driver.find_element_by_xpath(path).send_keys(password)

    path = '//*[@id="submitBtn"]'
    driver.find_element_by_xpath(path).click()

    driver.get(login_url)
        
    path = '//*[@id="panelaccounts"]'
    result = WaitForElement(driver, path)

    if not result:              # interprets returned value
    #        driver.close()
        debug("\nThe page is not loaded yet.")
    else:
        debug('web - page fully loaded!')

    return 0


#### 
def GetMembersList(driver):

    crew_url = base_crew_url + '/' + crew_name + '/hierarchy'
    driver.get(crew_url)
        
    path = '//*[@id="muscleList"]'
    result = WaitForElement(driver, path)

    if not result:              # interprets returned value
    #        driver.close()
        debug("\nThe page is not loaded yet.")
    else:
        debug('web - page fully loaded!')
        

    path = '//a[@data-ga="footer_selectlanguage_en"]'
    viewall = driver.find_element_by_xpath(path)

    if not viewall:
        debug("meh.")
    else:
        debug("web - set page in english.")
    #    viewall.click()

    path = '//a[@class="viewAll"]'
    
    try:
        viewall = driver.find_element_by_xpath(path)
        debug("web - unfold users.")
        viewall.click()
    except:
        debug("web - all users visible.")

    path = '//div[contains(@id, "crewRank_")]'
    hierarchy = driver.find_elements_by_xpath(path)

    crew_members = list()

    for rank in hierarchy:

    #    print rank.get_attribute('id')
        path = '//div[@id="' + rank.get_attribute('id') + '"]//i[@class="icon-info"]'
        rank_name = rank.find_element_by_xpath(path).get_attribute('data-name')
        
    #    print rank_name

        path = '//div[@id="' + rank.get_attribute('id') + '"]//ul[@id="' + rank_name + 'List"]//div[@class="member"]//img'
        members = rank.find_elements_by_xpath(path)

        for member in members:
            
            cm = crew_member()
            cm.id = member.get_attribute('data-original-title')
            cm.url = member.find_element_by_xpath('..').get_attribute('href')
            cm.rank = rank_name

            crew_members.append(cm)

    return crew_members

#### Function definitions
def GetMemberInfo(driver, member):

    debug('[' + member.id + ']')
    

    retry = 0
    max_retry = 5

    # Add retry to avoid errors
    for rety in range(max_retry): 

        ## Load profile page
        driver.get(member.url)
        
        path = '//*[@id="cardInfoVitals"]'
        result = WaitForElement(driver, path)

        if not result:              # interprets returned value
        #        driver.close()
            debug("web - The page is not loaded yet. [" + str(retry) + "]")
            retry += 1
        else:
            debug('web - page fully loaded! [' + str(retry) + ']')
            break

    ## Check if profile is private

    try:
        path = '//div[@id="no-profile"]'
        profail = driver.find_element_by_xpath(path) 
        debug('[' + member.id + '] Profile is private!')
        member.error = 'Private profile.'
        return 1        # Success

    except: 
        ## Crew Principal
        path = '//div[@class="crew-info"]/a'
        member.crew = driver.find_element_by_xpath(path).get_attribute("href").rsplit('/',1)[1]

        debug('[' + member.id + '] main crew: ' + member.crew)

        try:
            ## PSN ID
            path = '//div[@class="PSN"]/h5'
            member.psn = driver.find_element_by_xpath(path).text
        except:
            member.psn = ''

        debug('[' + member.id + '] PSN ID: ' + member.psn)
        
        try:
            ## Language
            path = '//div[@id="cardInfoFooter"]//span[contains(@class,"Country")]'
            member.country = driver.find_element_by_xpath(path).get_attribute("data-original-title")
        except:
            member.country = ''

        debug('[' + member.id + '] country: ' + member.country)
    
        driver.get(member.url + '/'+ path_gtav_base_url + '/ps3' + path_gtav_overview_url)
    
        path = '//div[@id="freemodeRank"]'
        result = WaitForElement(driver, path)
        
        if not result:              # interprets returned value
            #        driver.close()
            debug("\nThe page is not loaded yet.")
        else:
            debug('web - page fully loaded!')

        try:
            path = '//div[@id="freemodeRank"]//h3'
            member.level = driver.find_element_by_xpath(path).text
        except:
            member.level = ''

        if member.level == 0:
            member.platform = 'XBOX360'

            driver.get(member.url + '/'+ path_gtav_base_url + '/xbox' + path_gtav_overview_url)
    
            path = '//div[@id="freemodeRank"]'
            result = WaitForElement(driver, path)
        
            if not result:              # interprets returned value
                #        driver.close()
                debug("\nThe page is not loaded yet.")
            else:
                debug('web - page fully loaded!')

            try:
                path = '//div[@id="freemodeRank"]//h3'
                member.level = driver.find_element_by_xpath(path).text
            except:
                member.level = ''

        else:
            member.platform = 'PS3'

        debug('[' + member.id + '] rank: ' + member.rank)
            
        try:
            ## Language
            path = '//div[@id="freemodeRank"]//div[@class="rankBar"]/h4'
            member.playtime = driver.find_element_by_xpath(path).text.rsplit(':',1)[1]
        except:
            member.playtime = ''

        debug('[' + member.id + '] playtime: ' + member.playtime)
    
        

    # print sys.exc_info()
    return member 

#### Main function

if __name__ == "__main__":
    arg_parser(sys.argv[1:])

    debug('web - starting browser')
    driver = webdriver.Firefox()

    print 'Crew: ' + crew_name
    
    crew_members = GetMembersList(driver)
    print 'Crew Size: ' + str(len(crew_members)) + ' members'

    error = LoginSocialClub(driver)

    if error:
        print 'Crew Members :'
        for cm in crew_members:
            print cm.rank + ", " + cm.id + ", " + cm.url

        debug('You need to provide login information to view each member info.')

    for cm in crew_members:
        cm = GetMemberInfo(driver, cm)

    if output_file:
        f = open(output_file,'w')
        
    for cm in crew_members:
        member_csv = str(cm.id) + ', ' \
                    + str(cm.country) + ', ' \
                    + str(cm.psn) + ', ' \
                    + str(cm.platform) + ', ' \
                    + str(cm.crew) + ', ' \
                    + str(cm.rank) + ', ' \
                    + str(cm.level)  + ', ' \
                    + str(cm.playtime) + ', ' \
                    + str(cm.error)
        if output_file:
            f.write(member_csv + '\n')
        else:
            print member_csv

    if output_file:
        print 'Output saved as ' + output_file + '.'
        f.close() # you can omit in most cases as the destructor will call if
      
    driver.close()

    sys.exit()

    # Grab URL
    #url = str(sys.argv[1])
    # Check if it's malformed
    #regex = re.compile(
    #        r'^(?:http|ftp)s?://' # http:// or https://
    #        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
    #        r'localhost|' #localhost...
    #        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
    #        r'(?::\d+)?' # optional port
    #        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    #vurl = regex.match(url)
    #if vurl:
    #	print ("Good url : %s" % url)
    #else:
    #	debug ("Malformed url : %s" % url)
