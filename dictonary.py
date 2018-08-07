# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 22:41:01 2018
@author: Dev
"""
import json;
from difflib import get_close_matches

data = json.load(open("data.json"));

def translate(word):  
    if word in data:
        return data[word];
    elif len(get_close_matches(word,data.keys()))>0 :
        w =get_close_matches(word, data.keys())[0];
        YN =input("Did You Mean %s instead ? Enter y if Yes or n if No : " % w );
        if YN == "y":
            return data[w]
        elif YN == "n" :
            return "This Word Doesn't Exists, Please Double Check :) "
        else:
            return "We Can't get you Sorry . "
    else:
        return "This Word Doesn't exits ,Please Try Another Word :)";
    
word = input("Please Type A Word :").lower();  


outputs = translate(word);
if type(outputs) == list:
    for i in outputs:
        print ("Defination : " + i);
else:
    print(outputs);
    



