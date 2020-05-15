from selenium import webdriver
import pandas as pd
import math

data =  pd.read_csv('Flightmap.csv')
data = data['Address']

set10 = math.ceil(len(data)/10)
my_url = 'https://www.google.com.sg/maps/dir///@1.372787,103.9492056,15z/data=!4m2!4m1!3e3'
press = webdriver.common.keys.Keys

#initialize first tab
driver = webdriver.Chrome()
driver.get(my_url)
driver.implicitly_wait(3)

for k in range(set10):
    #split data into max row of 10 due to googlemaps limit
    start = max((10*k)-1,0)
    end = 0
    
    if(k!=set10-1):
        end = 9*(k+1)+1

    else:
        end = len(data)

    data1 = data[start:end].reset_index(drop=True)

    #new tab
    if (k!=0):
        driver.execute_script('window.open('');')
        driver.switch_to.window(driver.window_handles[k])
        driver.get(my_url)

    #select drive setting   
    driver.find_elements_by_class_name("directions-drive-icon")[0].click()

    for i,j in enumerate(data1):
        #initilizing starting and ending point
        if i <2:
            
            start = driver.find_element_by_id("sb_ifc%s" %(50+i)).find_elements_by_class_name("tactile-searchbox-input")
            start[0].send_keys('%s' % data1[i])

            #press enter after entering end point
            if i==1:
                start[0].send_keys(press.ENTER)

        #adding more destination
        if i >= 2:

            add_dest = driver.find_elements_by_class_name("waypoint-add")
            add_dest[0].click()

            add_dest  = driver.find_element_by_id("sb_ifc%s" %(50+i)).find_elements_by_class_name("tactile-searchbox-input")
            add_dest[0].send_keys('%s' % data1[i])
            add_dest[0].send_keys(press.ENTER)
