import json

import time

import ssl

from selenium import webdriver

import selenium.webdriver.chrome

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

from selenium.common.exceptions import TimeoutException

import threading

from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from PIL import Image, ImageDraw, ImageFont

 

class openURLTakeSC_Thread(threading.Thread):

    def __init__(self, p_usr, p_pass,  p_url, p_imageHandle, p_filePath, p_filePathWaterMarked , p_options, p_timestr , p_waterText, \

    p_waterColor, p_waterFont, p_isDebug, p_threadManagerRef ):

        threading.Thread.__init__(self)

#        self.driver = driver

        self.p_url = p_url

        self.p_usr = p_usr

        self.p_pass = p_pass

        self.p_imageHandle = p_imageHandle

        self.p_filePath = p_filePath

        self.p_filePathWaterMarked = p_filePathWaterMarked

        self.p_options = p_options

        self.timestr = p_timestr

        self.waterText =  p_waterText

        self.waterColor =  p_waterColor

        self.waterFont = p_waterFont

        self.isDebug = p_isDebug

        self.threadManagerRef  = p_threadManagerRef

   

 

    def createDriverObj (self):

        driver = webdriver.Chrome(options=self.p_options)

        return driver

 

 

    def watermark_image_with_text (self):

 

        inputImage = Image.open(self.p_filePath).convert('RGBA')

        image2Watermark = Image.new('RGBA', inputImage.size, (255, 255, 255, 0))

        draw = ImageDraw.Draw(image2Watermark)

       

        width, height = inputImage.size

        margin = 10

        font = ImageFont.truetype(self.waterFont, int(height / 20))

        textWidth, textHeight = draw.textsize(self.waterText, font)

        x = width - textWidth - margin

        y = height - textHeight - margin

        if (self.isDebug == 'True'): print ('\n dBug x = ' , x, ' y = ',y ,'\n')

        finalWaterText = self.waterText + self.timestr

        draw.text((500, 500), finalWaterText, self.waterColor, font)

 

        return Image.alpha_composite(inputImage, image2Watermark)

 

 

 

       

    def run(self):

        if (self.isDebug == 'True'): print ('\n app params: ', self.p_url,  '  =====   ', self.p_imageHandle,'\nCreating driver and Getting thread lock \n ')

        driver = self.createDriverObj()

        self.threadManagerRef.acquire()

        if (self.isDebug == 'True'): print ('\n' + threading.current_thread().name + " <--- acquired the resource. \n")

        # time.sleep(50)

        try: 

            # url =

            driver.get(self.p_url)

            time.sleep(10)       

            driver.implicitly_wait(10)

            driver.find_element_by_id("username").send_keys(self.p_usr)

            driver.find_element_by_id("password").send_keys(self.p_pass)   

            driver.find_element_by_class_name("btn-submit").click()              

            try:

 

    #           driver.page_source to get the HTML of the website

                time.sleep(10)       

                driver.implicitly_wait(10)

                if ((WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, self.p_imageHandle))))!= None):  

                    time.sleep(20)

                    driver.save_screenshot(self.p_filePath)

                    if (self.isDebug == 'True'): print (" SC after first wait")

                else: 

                    if ((WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, self.p_imageHandle))))!= None):

                        time.sleep(10)

                        driver.save_screenshot(self.p_filePath)

                        if (self.isDebug == 'True'): print (" SC after 2nd wait")

                    else:

                        if (self.isDebug == 'True'): print (" No match found after 2 trials")

                   

                watermarked_image = self.watermark_image_with_text()

                watermarked_image.save(self.p_filePathWaterMarked)               

                print ( "\n Saved in ", self.p_filePathWaterMarked)

                   

            except NoSuchElementException as nse:

                print( "NoSuchElementException: Error:" % nse )

            

            except NoSuchElementException as nse:

                print( "NoSuchElementException: Error:" % nse )

                

            except TimeoutException as ex:

                print("Exception has been thrown in run SC. " + str(ex))

       

        except Exception as e:

            print( "Gen exception in login block : Error:" % e )

           

        finally:

          if (self.isDebug == 'True'): print ( "\n closing driver ....")

           driver.close()

           if (self.isDebug == 'True'): print ( "\n releasing  self.threadManagerRef. ....")

           self.threadManagerRef.release()

        # if (self.isDebug == 'True'): print ( "\n releasing  self.threadManagerRef. ....")

        # self.threadManagerRef.release()

 

 

 