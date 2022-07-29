import time

import ssl

from selenium.webdriver.chrome.options import Options

import threading

from collections import namedtuple

import datetime

import collections

import copy

from UtilClassDef2 import UtilClass

from EnvClassDef import EnvClass

from readConfig import read_config

from openURLTakeSC_ThreadDef2 import openURLTakeSC_Thread

import tink_drive3 as tkinD3 

import threading

from cryptography.fernet import Fernet

import codecs

 

def loadConfigInEnv ( p_envName, p_timeStr, p_configHandle, p_fernetKy ) :

 

    appEnv = EnvClass()

 

 

    appUrl1 = EnvClass.appProp3Cls(p_configHandle.get(p_envName,'appname1'), p_configHandle.get(p_envName,'url1'), p_configHandle.get(p_envName,'imageHandle1'))

    appUrl2 = EnvClass.appProp3Cls(p_configHandle.get(p_envName,'appname2'), p_configHandle.get(p_envName,'url2'), p_configHandle.get(p_envName,'imageHandle2'))

    appUrl3 = EnvClass.appProp3Cls(p_configHandle.get(p_envName,'appname3'), p_configHandle.get(p_envName,'url3'), p_configHandle.get(p_envName,'imageHandle3'))

    appUrl4 = EnvClass.appProp3Cls(p_configHandle.get(p_envName,'appname4'), p_configHandle.get(p_envName,'url4'), p_configHandle.get(p_envName,'imageHandle4'))

 

 

    appEnv.setUtilVals( \

    p_configHandle.get('Util','name'), p_configHandle.get('Util','root') , p_configHandle.get('Util','imageSourceStr'), p_timeStr, p_configHandle.get('Util','maxThreadCount'),\

    gEnvlist,p_configHandle.get('Util','imageSaveDestinationStr') , p_configHandle.get('Util','urlLoadHtmlWaitSleepTime') ,p_configHandle.get('Util','elementLaodHtmlWaitSleepTime'),\

    p_configHandle.get('Util','implicitlyWaitSleepTime') , p_configHandle.get('Util','chromeOption1'), p_configHandle.get('Util','chromeOption2') ,\

    p_configHandle.get('Util','chromeOption3') , p_configHandle.get('Util','waterMarkTxt') ,p_configHandle.get('Util','waterMarkColor') , p_configHandle.get('Util','waterMarkFont'),\

    p_configHandle.get('Util','utilIsDebug') , p_configHandle.get('Util','utilLogConfigPath') ,p_configHandle.get('Util','utilLogPath') \

    )

 

    appEnv.setEnvVals(p_configHandle.get(p_envName,'envname'), p_configHandle.get(p_envName,'user'), decryptString( p_fernetKy, p_configHandle.get(p_envName,'passo')), \

    p_configHandle.get(p_envName,'envname'), p_configHandle.get(p_envName,'envname'), appUrl1, appUrl2, appUrl3, appUrl4 )

 

    if (appEnv.utilIsDebug == 'True'): print ('\n appEnv ====>', appEnv )

    

    return appEnv

   

def decryptString(p_cipherKey, p_token):

 

 

    p_token = bytes(p_token,'utf-8')

    if (gUtilIsDebug): print ("\n in method p_token: ", p_token, '\t p_cipherKey : ',  p_cipherKey )

    if (gUtilIsDebug): print ("\n in method decrypted: ", p_cipherKey.decrypt(p_token).decode('utf-8') )

    return p_cipherKey.decrypt(p_token).decode('utf-8') 

    

    

def encryptString(p_cipherKey, P_string):

    # p_Msg = to_bytes(p_Msg)

    P_string = P_string.encode('utf-8')

    return p_cipherKey.encrypt(P_string)

      

 

  

    

def createThreadForEachEnv ( p_appEnv, p_threadManagerRef):

 

    tmp_threadList = []

    options = Options()

    options.add_argument(p_appEnv.chromeOption1)

    options.add_argument(p_appEnv.chromeOption2)

    options.add_argument(p_appEnv.chromeOption3) #    INFO = 0,     WARNING = 1,     LOG_ERROR = 2,     LOG_FATAL = 3.

    options.add_experimental_option('useAutomationExtension', False) 

    

        

    th1 = openURLTakeSC_Thread( p_appEnv.user, p_appEnv.passwd, p_appEnv.appRef1.url, p_appEnv.appRef1.imageHandle,   \

    p_appEnv.utilRoot + p_appEnv.imageSourceStr + p_appEnv.envName + '_' +  p_appEnv.appRef1.appName  +'_' +p_appEnv.utilPara1 +'_screenshot.png',   \

    p_appEnv.utilRoot + p_appEnv.imageSaveDestinationStr + p_appEnv.envName + '_' +  p_appEnv.appRef1.appName +'_'+p_appEnv.utilPara1 +'_screenshot.png',   \

    options, p_appEnv.utilPara1 , p_appEnv.waterMarkTxt, p_appEnv.waterMarkColor, p_appEnv.waterMarkFont, p_appEnv.utilIsDebug , p_threadManagerRef  )

    tmp_threadList.append ( th1)

   

    th2 = openURLTakeSC_Thread( p_appEnv.user, p_appEnv.passwd, p_appEnv.appRef2.url, p_appEnv.appRef2.imageHandle,   \

    p_appEnv.utilRoot + p_appEnv.imageSourceStr + p_appEnv.envName + '_' +  p_appEnv.appRef2.appName  +'_' +p_appEnv.utilPara1 +'_screenshot.png',   \

    p_appEnv.utilRoot + p_appEnv.imageSaveDestinationStr + p_appEnv.envName + '_' +  p_appEnv.appRef2.appName +'_'+p_appEnv.utilPara1 +'_screenshot.png',   \

    options, p_appEnv.utilPara1 , p_appEnv.waterMarkTxt, p_appEnv.waterMarkColor, p_appEnv.waterMarkFont, p_appEnv.utilIsDebug  , p_threadManagerRef ) 

    

    tmp_threadList.append ( th2)

   

    th3 = openURLTakeSC_Thread( p_appEnv.user, p_appEnv.passwd, p_appEnv.appRef3.url, p_appEnv.appRef3.imageHandle,   \

    p_appEnv.utilRoot + p_appEnv.imageSourceStr + p_appEnv.envName + '_' +  p_appEnv.appRef3.appName  +'_' +p_appEnv.utilPara1 +'_screenshot.png',   \

    p_appEnv.utilRoot + p_appEnv.imageSaveDestinationStr + p_appEnv.envName + '_' +  p_appEnv.appRef3.appName +'_'+p_appEnv.utilPara1 +'_screenshot.png',   \

    options, p_appEnv.utilPara1 , p_appEnv.waterMarkTxt, p_appEnv.waterMarkColor, p_appEnv.waterMarkFont, p_appEnv.utilIsDebug  , p_threadManagerRef  ) 

    

    tmp_threadList.append ( th3)

   

    th4 = openURLTakeSC_Thread( p_appEnv.user, p_appEnv.passwd, p_appEnv.appRef4.url, p_appEnv.appRef4.imageHandle,   \

    p_appEnv.utilRoot + p_appEnv.imageSourceStr + p_appEnv.envName + '_' +  p_appEnv.appRef4.appName  +'_' +p_appEnv.utilPara1 +'_screenshot.png',   \

    p_appEnv.utilRoot + p_appEnv.imageSaveDestinationStr + p_appEnv.envName + '_' +  p_appEnv.appRef4.appName +'_'+p_appEnv.utilPara1 +'_screenshot.png',   \

    options, p_appEnv.utilPara1 , p_appEnv.waterMarkTxt, p_appEnv.waterMarkColor, p_appEnv.waterMarkFont, p_appEnv.utilIsDebug  , p_threadManagerRef )

    

    tmp_threadList.append ( th4)

    if (p_appEnv.utilIsDebug == 'True'): print ('\n p_threadManagerRef:', p_threadManagerRef )

    if (p_appEnv.utilIsDebug == 'True'): print ('\n Appending 4 threads for env: ====>', p_appEnv.envName )

 

    return tmp_threadList

    

 

if __name__ == '__main__':

 

 

 

 

    try:

        config = read_config(['app2.properties'])

    except Exception as e:

        print( "Config file read Error:" % e )

       

    # key = Fernet.generate_key()

    key = b'RWbDJAUo2IoDh76J7GGir5YadAhAlTX1fvGo2l_xPmQ='

    cipherKey = Fernet(key)

 

 

 

    gTimeStr = time.strftime("%y%m%d_%H%M%S")

    gEnvlist = []

    gThreadList = []

    gThreadManagerRef = threading.BoundedSemaphore( value= ( int(config.get('Util','maxThreadCount'))))

    gUtilIsDebug = bool(config.get('Util','utilIsDebug'))

 

    if (gUtilIsDebug): print ("\n gThreadManagerRef: ", gThreadManagerRef)

 

    if (gUtilIsDebug): print ("\n Getting user input ")

    tkinD3.create_main_window(gEnvlist,config.get('Util','name'))

 

    if (gUtilIsDebug): print ("\n User input items in gEnvlist= ", gEnvlist)

   

    for i in range(len(gEnvlist)):

        if (gUtilIsDebug): print ( "gEnvlist item  = ", gEnvlist[i]) 

        tmp_Env = loadConfigInEnv (gEnvlist[i], gTimeStr, config, cipherKey )

        gThreadList.append(createThreadForEachEnv(tmp_Env, gThreadManagerRef))

 

    if (gUtilIsDebug): print ("\n Starting threads for gThreadList elements ", gThreadList)

 

    for envThreads in gThreadList:

        # t = threading.Thread(i)

        envThreads[0].start()

        envThreads[1].start()

        envThreads[2].start()

        envThreads[3].start()

       

    if (gUtilIsDebug): print ("\n Joining threads for gThreadList length:", len(gThreadList))      

    for envThreads in gThreadList:

        envThreads[0].join()

        envThreads[1].join()

        envThreads[2].join()

        envThreads[3].join()

           