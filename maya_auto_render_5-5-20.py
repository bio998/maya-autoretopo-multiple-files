import maya.mel as mel 
from mtoa.cmds.arnoldRender import arnoldRender 
import random
import time
import datetime
import os
import pymel.core as pm

        
#vcount = [1000,2000,4000,6500,10000]
#vcount = [5000]
vcount = [10000,6500,4000,2000,1000]

test_path = 'C:\\Users\\benja\\OneDrive\\Documents\\maya'

examplefilepath = 'C:\\Users\\benja\\OneDrive\\Projects\\Unity\\KuruKuru4\\Squingle3DModels\\g_kingdom1_0000_05.fbx'

path = "C:\\Users\\benja\\OneDrive\\Projects\\Unity\\KuruKuru4\\Squingle3DModels\\"
outpath = 'C:\\Users\\benja\\OneDrive\\Projects\\Unity\\KuruKuru4\\MayaOutput\\'
folder = os.listdir(path)
pathlist = []
pathlistS = []

for item in folder:
    if item.endswith("_05.fbx") and item.endswith("S_05.fbx") == False:
        pathlist.append(path + item)
        
for item in folder:
    if item.endswith("S_05.fbx"):
        pathlistS.append(path + item)



def setImport(filepath):
    setImportPath = filepath
    cmds.file(setImportPath, i=True, mergeNamespacesOnClash=True, namespace=':')

counter = 0



for p in pathlist:
    
    
    test1 = False

    test_folder = os.listdir(test_path) 

    for test in test_folder:
        print(test)
        if test == "test.txt":
            print("next render " + str(counter))
            print(datetime.datetime.now()) 
            test1 = True

        if test1 == False:
            print("rendering inturrupted, interupt file was deleted")
            break
    
    
    if counter < 1000:
        

    
        setImport(p)
        
        #try:
        cmds.select('Squiggle_Clone_')
        #except:
        #    cmds.select('SquiggleSecret_Clone_')
        
        cmds.polyClean()
        
        cmds.polyRemesh()
        
        cmds.polyRetopo()
        
        print("initial retopo complete " + os.path.basename(p))
        
        
        time.sleep(1)
        

        
        for v in vcount:
            cmds.setAttr("polyRetopo1.targetFaceCount", v)
            #cmds.polyRetopo()
            
            print("retopo " + str(v))
        
            #pm.loadPlugin("fbxmaya") # LOAD PLUGIN
            time.sleep(1)
        
            #for example
            pm.mel.FBXExport(f=outpath + os.path.basename(p)[:-7] + "_" + str(v) + '.fbx')
            time.sleep(1)

        cmds.delete()
        
    counter = counter + 1


#repeat for secret ones
counter = 0

for p in pathlistS:

    test1 = False

    test_folder = os.listdir(test_path) 

    for test in test_folder:
        if test == "test.txt":
            print("next render " + str(counter))
            print(datetime.datetime.now()) 
            test1 = True

    if test1 == False:
        print("rendering inturrupted, interupt file was deleted")
        break
            
    counter = counter + 1
    
    if counter <= 1000:
    
        setImport(p)
        
        #try:
        #cmds.select('Squiggle_Clone_')
        #except:
        cmds.select('SquiggleSecret_Clone_')
        
        cmds.polyClean()
        
        cmds.polyRemesh()
        
        cmds.polyRetopo()
        
        print("initial retopo complete " + os.path.basename(p))
        
        
        time.sleep(1)
        
       
        
        for v in vcount:
            cmds.setAttr("polyRetopo1.targetFaceCount", v)
            #cmds.polyRetopo()
            
            print("retopo " + str(v))
        
            #pm.loadPlugin("fbxmaya") # LOAD PLUGIN
            time.sleep(1)
        
            #for example
            pm.mel.FBXExport(f=outpath + os.path.basename(p)[:-7] + "_" + str(v) + '.fbx')
            time.sleep(1)

        cmds.delete()

