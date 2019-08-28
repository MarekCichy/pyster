# Automate posting messages on a portal using pyautogui

import datetime
import winsound

import pyautogui as gui
import pyperclip as clip
import time
import csv


def set_coords():
    #Sets coordinates for the necessary points on screen.
    coords ={0:['browser address bar'], 
             1:['"more" button on the bottom of the People page'],
             2:['gray background to the left of any user photo on the People page'],
             3:['"AT" letters of the "CHAT" button on the profile page of any user that - TAKE NOTE - \n1) has NO background photo; \n2) is NOT among your favourite users'],
             4:['"AT" letters of the "CHAT" button on the profile page of any user that - TAKE NOTE - \n1) HAS a background photo; \n2) is NOT among your favourite users'],
             5:['"SEND" button in the message window of any user'],
             6:['"BACK" button of the browser']}

    gui.alert(text='First I need to gather coordinates for certain points on your screen.', 
              title='Pyster - automatic poster')
    for i in range(0, 7):
        gui.confirm('Press OK, set the mouse cursor on the'+str(coords[i][0])+
                    ', wait till you hear a beep and come back here.', 
                    title='Pyster - automatic poster')
        time.sleep(5)
        coords[i]=gui.position()
        winsound.Beep(frequency=500, duration=500)
    gui.alert('Coords set!'+str(coords), title='Pyster - automatic poster')
    with open('coords.csv', 'w') as f:
    for key in coords.keys():
        f.write("%s;%s;%s\n"%(key,coords[key][0],coords[key][1]))
    return coords



def scrape_dict(users=250):
    '''Scrape a given number of users from the portal.
    
    argument: number of users to be scraped
    
    returns: a dict with usernames as keys and current datetime as values.
    
    REFACTOR IT TO A LIST! dict is unnecessary.
    '''
    user_dict = dict()
    pages = int(users/50)
    for _ in range(0, pages):
        for _ in range(0, 23):
            gui.press('pgdn')
        gui.moveTo(coords[1])
        gui.click()
        time.sleep(1)
    gui.moveTo(coords[2])
    gui.keyDown('ctrl')
    gui.press('a')
    clip.copy('')
    gui.press('c')
    gui.keyUp('ctrl')
    a = clip.paste()
    b = a.split('FAVOURITES')[1]
    c = b.split('\r\nLOCATION')[0]
    d = c.split('\r\n\r\n')
    len(d)
    for e in d:
        f = e.split('\r\n')[0]
        user_dict[f] = datetime.datetime.today()
    return user_dict


def get_user_batch(user_input):
    #Scrape the desired number of users among those not recently messaged. REFACTOR - see scrape_dict()
    user_count = user_input
    mid_dict = {}
    last_dict = {}
    gui.alert('Enter the "People" tab and filter out the users as you like.\nReturn here, press OK, switch to the portal page an click the gray background. \nWait for the beep', 
              title='Pyster - automatic poster')
    time.sleep(5)
    while (len(mid_dict) < user_input) and (user_count < 3500):
        temp_dict = scrape_dict(users=user_count)
        for key, value in temp_dict.items():
            if (key not in main_dict) or ((value-main_dict[key]) > datetime.timedelta(days=14)):
                mid_dict[key] = datetime.datetime(2009, 7, 28, 7, 25, 58, 913124)
            else:
                pass
        if (last_dict == mid_dict):
            user_count = 3501
        user_count = user_count*2
        last_dict = mid_dict
    new_dict = {}
    keys = [*mid_dict][0:user_input]
    for key in keys:
        new_dict[key] = mid_dict[key]
    winsound.Beep(frequency=500, duration=500)
    return new_dict

def send_msg(user, msg):
    #Send msg to user, update main_dict.
    time.sleep(5)
    gui.moveTo(coords[0])
    gui.click()
    gui.typewrite('[portal address]'+str(user))
    gui.press('enter')
    gui.moveTo(coords[4])
    time.sleep(1)
    gui.click()
    time.sleep(1)
    gui.typewrite(str(msg))
    time.sleep(1)
    gui.moveTo(coords[5])
    time.sleep(1)
    #gui.click()
    time.sleep(1)
    gui.moveTo(coords[3])
    time.sleep(1)
    gui.click()
    time.sleep(1)
    gui.typewrite(str(msg))
    time.sleep(1)
    gui.moveTo(coords[5])
    time.sleep(1)
    #gui.click()
    main_dict[user] = datetime.datetime.today()



def backup():
    # Writes the current state of main_dict to CSV file
    with open('main_dict.csv', 'w') as f:
        for key in main_dict.keys():
            f.write("%s,%s\n"%(key,main_dict[key]))
    if len(coords)>1:


#Program core   
                
try:
    main_dict= {}
    with open('main_dict.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            main_dict[row[0]] = datetime.datetime.strptime(row[1],"%Y-%m-%d %H:%M:%S.%f")
    
    coords = {}    
    try:
        with open('coords.csv', newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                coords[int(row[0])] = gui.Point(row[1],row[2])
    except:
        coords = set_coords()
    
    
    user_input = int(gui.prompt('How many users do you want to message?', 
                                title='Pyster - automatic poster'))
    new_dict = get_user_batch(user_input)
    msg = str(gui.prompt('What message do you want to send?\nEnter the text below, click "OK" and wait a while.', 
                         title='Pyster - automatic poster'))
    for key,value in new_dict.items():
        send_msg(key,msg)
    winsound.Beep(frequency=500, duration=500)
    gui.alert('The message "'+msg+'" was succesfully sent to '+str(len(new_dict))+' users.', 
              title='Pyster - automatic poster')
    backup()

finally:
    backup()
