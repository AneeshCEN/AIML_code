# -*- coding: utf-8 -*-
"""
Created on Fri Jan 06 12:07:44 2017

@author: aneesh.c
"""

import aiml
import os
path = 'C:\Users\\aneesh.c\Desktop\chatbot\healthcare'
brain_file = "gunbroker_modified.brn"
os.chdir(path)



if __name__ == '__main__':
    kern = aiml.Kernel()
    kern.bootstrap(learnFiles=path+'/std-startup_medical.xml', 
                   commands="load aiml b")
    kern.saveBrain(brain_file)
    kern.bootstrap(brainFile = brain_file)
    while True:
        print kern.respond(raw_input())
    