
# coding: utf-8

# In[1]:

from ipywidgets import interact, interactive, fixed, interact_manual, IntSlider, Checkbox
import ipywidgets as widgets
import requests
import time


# In[2]:

robotstate = {"rv":128, "rh":128, "lv":128, "lh":128, "b0":0, "b1":0, "b2":0, "b3":1, "b4":1, "b5":1, "b6":1, "b7":1}


# In[3]:

def send2robot():
    global robotstate
    response= requests.post("http://euclid:9100/", json=robotstate)
    if response.status_code == 200:
        return response.text
    else:
        return (response, response.text)
    


# In[4]:

send2robot()


# In[37]:

def updater(**args):
    global robotstate

    a=args.copy()
    for i in range(8):
        key='b{}'.format(i)
        a[key] = int(a[key])
    robotstate= a
    time.sleep(0.1)
    return send2robot()


# In[40]:

sliders={n: IntSlider(min=0, max=255, value=128) for n in ['lv','lh','rv','rh']} 
sliders.update({b: Checkbox() for b in ["b{}".format(n) for n in range(8)] })


# In[41]:

interact(updater, **sliders)


# In[ ]:



