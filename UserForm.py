#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



def callback():    
    val1=name.get()
    val2=family.get()
    if not age.get():
        messagebox.showinfo(message="! لطفاً سن خود را وارد کنید")
    else:
        val3=age.get()
   
    if not job.get():
        messagebox.showinfo(message="! لطفا شغل خود را وارد کنید")
    else:
        val5=job.get()  
    

window=tkinter.Tk()
window.geometry('600x300')
window.title('movies Raiting')
window.resizable(False, False) 


lbl_name=Label(text='لطفاً به فیلم هایی که دیده اید امتیاز بدهید')
lbl_name.config(font='Ubuntu 14',bg='#e6d67e',fg='#141414',width=22,height=1)
lbl_name.grid(sticky=N,padx=200,pady=10)

lbl_name=Label(text='بابت زمانی که صرف می کنید سپاسگزار شما هستم')
lbl_name.config(font='Raleway 14',bg='#e6d67e',fg='#141414',width=40,height=1)
lbl_name.grid(sticky=N,padx=40,pady=2)

name=Entry(width=30)
lblname=ttk.Label(text=": نام ")
lblname.grid(row=3,column=0,sticky='E',pady=10,padx=50)
name.grid(sticky=E, padx=70,pady=15,row=3,column=0)

family=Entry(width=30)
lblfamily=ttk.Label(text=": نام خانوادگی ")
lblfamily.grid(row=3,column=0,sticky='W',pady=10,padx=230)
family.grid(sticky=W, padx=70,pady=15,row=3,column=0)

age=Entry(width=30)
lblage=ttk.Label(text=":*سن ")
lblage.grid(row=4,column=0,sticky='E',pady=2,padx=50)
age.grid(sticky=E, padx=70,pady=2,row=4,column=0)

    
gender=tkinter.StringVar()
option1 = BooleanVar(value=False)
R1 = tkinter.Radiobutton(window,text='آقا',value=1,variable=gender,var=option1).grid(row=4,column=0,sticky=W,padx=195,pady=2)
option2 = BooleanVar(value=False)
R2 = tkinter.Radiobutton(window,text='خانم',value=2,variable=gender,var=option2).grid(row=4,column=0,sticky=W,padx=70,pady=2)
lblgender=ttk.Label(text=": جنسیت ")
lblgender.grid(row=4,column=0,sticky='W',pady=2,padx=255)



job=Entry(width=30)
lbljob=ttk.Label(text=":*شغل")
lbljob.grid(row=5,column=0,sticky='E',pady=10,padx=50)
job.grid(sticky=E, padx=70,pady=15,row=5,column=0)

button1=Button(window,text='مرحله بعد',width=10,command=callback)
button1.grid(row=6,column=0,sticky='W',pady=2,padx=250)


window.mainloop()
# label=tk.Label(text='به فیلم هایی که دیده اید امتیاز بدهید')


# In[2]:


#! /usr/bin/python
import visualizer
# from visualizer import Visualize
import statistics
import numpy as np
from datagen import constructData
from sklearn import svm
'''
Methods to construct various statistical plots for the load time series
'''
# Plot the original load series
def plotOriginal():
    data = constructData()
    # Plot of aggregate electricity demand over the past 5 years
    section = data[1][0:len(data[1])-365]
    visualizer.yearlyPlot(section,
        2009,1,1,"Average Total Electricity Load : 2009-2013","Kilowatts")
# Plot the load series after detrending with least squares
# linear regression
def plotDetrended():
    data = constructData()
    # Plot of data after detrending with least squares regression
    indices = np.arange(len(data[1]))
    detrendY = statistics.detrend(indices,data[1])[0]
    visualizer.yearlyPlot(detrendY,
        2009,1,1,"Detrended Aggregate Electricity Demand","Residual Kilowatts")
# Plot the correlogram for the load series
# - plots autoregressive correlation coefficients against time lags
def plotCorrelogram():
    data = constructData()
    visualizer.autoCorrPlot(data[1][len(data[1])-730:len(data[1])-365],"Average Total Electricity Load Autocorrelations : 2013")
# Plot the lag plot for the load series
# - use to determine whether time series data is non-random
def plotLag():
    data = constructData()
    visualizer.lagPlot(data[1][0:len(data[1])-365],"Average Total Electricity Load Lag : 2009-2013")   
# Plot the periodogram for the load series
# - plots frequency strength against frequencies over the spectrum
def plotPeriodogram():
    data = constructData()
    visualizer.periodogramPlot(data[1][len(data[1])-730:len(data[1])-365],
        "Periodogram of Average Total Electricity Load : 2013")
# Plot the original load series vs. the detrended load series
def plotOrigVsDetrend():
    data = constructData()
    # Original time series
    data1 = constructData()
    origY = data1[1][0:len(data[1])-365]
    # Detrended time series
    indices = np.arange(len(data[1])-365)
    detrendY = statistics.detrend(indices,data[1][0:len(data[1])-365])[0]
    visualizer.comparisonPlot(2009,1,1,origY,detrendY,
        "Original","Detrended",plotName="Aggregate Electric Load : Original & Detrended", yAxisName="Kilowatts")
if __name__=="__main__":
    plotCorrelogram()


# In[5]:


#! /usr/bin/python
import visualizer
# from visualizer import Visualize
import statistics
import numpy as np

from datagen import constructData
from sklearn import svm
'''
Methods to construct various statistical plots for the load time series
'''
# Plot the original load series
def plotOriginal():
    data = constructData()
    # Plot of aggregate electricity demand over the past 5 years
    section = data[1][0:len(data[1])-365]
    visualizer.yearlyPlot(section,
        2009,1,1,"Average Total Electricity Load : 2009-2013","Kilowatts")
# Plot the load series after detrending with least squares
# linear regression
def plotDetrended():
    data = constructData()
    # Plot of data after detrending with least squares regression
    indices = np.arange(len(data[1]))
    detrendY = statistics.detrend(indices,data[1])[0]
    visualizer.yearlyPlot(detrendY,
        2009,1,1,"Detrended Aggregate Electricity Demand","Residual Kilowatts")
# Plot the correlogram for the load series
# - plots autoregressive correlation coefficients against time lags
def plotCorrelogram():
    data = constructData()
    visualizer.autoCorrPlot(data[1][len(data[1])-730:len(data[1])-365],"Average Total Electricity Load Autocorrelations : 2013")
# Plot the lag plot for the load series
# - use to determine whether time series data is non-random
def plotLag():
    data = constructData()
    visualizer.lagPlot(data[1][0:len(data[1])-365],"Average Total Electricity Load Lag : 2009-2013")   
# Plot the periodogram for the load series
# - plots frequency strength against frequencies over the spectrum
def plotPeriodogram():
    data = constructData()
    visualizer.periodogramPlot(data[1][len(data[1])-730:len(data[1])-365],
        "Periodogram of Average Total Electricity Load : 2013")
# Plot the original load series vs. the detrended load series
def plotOrigVsDetrend():
    data = constructData()
    # Original time series
    data1 = constructData()
    origY = data1[1][0:len(data[1])-365]
    # Detrended time series
    indices = np.arange(len(data[1])-365)
    detrendY = statistics.detrend(indices,data[1][0:len(data[1])-365])[0]
    visualizer.comparisonPlot(2009,1,1,origY,detrendY,
        "Original","Detrended",plotName="Aggregate Electric Load : Original & Detrended", yAxisName="Kilowatts")
if __name__=="__main__":
    plotCorrelogram()


# In[ ]:




