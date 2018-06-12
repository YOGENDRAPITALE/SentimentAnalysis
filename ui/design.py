#SentimentAnalysis
import tkFileDialog as filedialog
from Tkinter import*
import tkFont
import tweepy
import os.path
import csv
from PIL import ImageTk, Image, ImageGrab
from tweepy.auth import OAuthHandler
import time
import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email import encoders
from scipy.misc import imread
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
from matplotlib import colors as mcolors
import subprocess
from subprocess import Popen, PIPE
import os
import pynstagram
import ctypes 
import shutil
import ctypes

def doNothing():
   print("Sentiment Analysis")
   
   
def nightMode(event=None):
    global windowMT
    global windowMB
    global searchButton
    global shareButton
    global exportButton
    global shareButtonFacebook
    global shareButtonTwitter
    global saveButton
    windowMT["bg"]="#141d26"
    windowMB["bg"]="#141d26"
    searchButton["bg"]="#2979FF"
    shareButtonFacebook["bg"]="#2979FF"
    shareButtonTwitter["bg"]="#2979FF"
    shareButton["bg"]="#2979FF"
    exportButton["bg"]="#2979FF"
    saveButton["bg"]="#2979FF"
    
def dayMode(event=None):
    global windowMT
    global windowMB
    global searchButton
    global shareButton
    global exportButton
    global shareButtonFacebook
    global shareButtonTwitter
    global saveButton
    windowMT["bg"]="#1E88E5"
    windowMB["bg"]="#388E3C"
    searchButton["bg"]="#424242"
    shareButtonFacebook["bg"]="#424242"
    shareButtonTwitter["bg"]="#424242"
    shareButton["bg"]="#424242"
    exportButton["bg"]="#424242"
    saveButton["bg"]="#424242"
	
def isSearchEntered(event):       
    global isSearchBarClick

    if isSearchBarClick:
       isSearchBarClick = False
       search.delete(0, "end") 
	   
#Create window
window=Tk()
window.title("Sentiment Analysis Project")
window.geometry("1366x732+0+0")
window.resizable(width=False, height=False)
Tk.iconbitmap(window,default='y.ico')

#Define Font Style
mainMenuFont = tkFont.Font(family='Arial', size=8, weight=tkFont.NORMAL)
fontOne = tkFont.Font(family='helvetica', size=15, weight=tkFont.BOLD)
fontTwo = tkFont.Font(family='helvetica', size=15)
fontThree=tkFont.Font(family='helvetica', size=18, weight=tkFont.BOLD)
fontFour=tkFont.Font(family='helvetica', size=12)
setTextFoneForTopTweetst=tkFont.Font(family="helvetica", size=10)
setTextFoneForTopTrend=tkFont.Font(family="helvetica", size=12)
#menu bar
menu=Menu(window)
window.config(menu=menu)

#Select Category
selectCategory=Menu(menu,tearoff=0)
menu.add_cascade(font=mainMenuFont,label="Select Category", menu=selectCategory)

#education
education=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Education", menu=education)

competitiveExams=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="Competitive Exams", menu=competitiveExams)
competitiveExams.add_command(label="AIEEE", command=doNothing)
competitiveExams.add_command(label="CAT", command=doNothing)
competitiveExams.add_command(label="CPT", command=doNothing)
competitiveExams.add_command(label="GMAT", command=doNothing)
competitiveExams.add_command(label="GRE", command=doNothing)
competitiveExams.add_command(label="IELTS", command=doNothing)
competitiveExams.add_command(label="NEET", command=doNothing)
competitiveExams.add_command(label="TOFFEL", command=doNothing)

hsc=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="HSC", menu=hsc)
hsc.add_command(label="State Bord", command=doNothing)
hsc.add_command(label="CBSC", command=doNothing)
hsc.add_command(label="ICSE", command=doNothing)

ssc=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="SSC", menu=ssc)
ssc.add_command(label="State Bord", command=doNothing)
ssc.add_command(label="CBSC", command=doNothing)
ssc.add_command(label="ICSE", command=doNothing)

college=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="College", menu=college)
school=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="School", menu=school)
preschool=Menu(education,tearoff=0)
education.add_cascade(font=mainMenuFont,label="PreSchool", menu=preschool)

#finanace
finanace=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Finanace", menu=finanace)

business=Menu(finanace,tearoff=0)
finanace.add_cascade(font=mainMenuFont,label="Business", menu=business)
smallScaleIndustries=Menu(business,tearoff=0)
business.add_cascade(font=mainMenuFont,label="Small Scale Industries", menu=smallScaleIndustries)
mediumScaleIndustries=Menu(business,tearoff=0)
business.add_cascade(font=mainMenuFont,label="Medium Scale Industries", menu=mediumScaleIndustries)
largeScaleIndustries=Menu(business,tearoff=0)
business.add_cascade(font=mainMenuFont,label="Large Scale Industries", menu=largeScaleIndustries)
topIndustries=Menu(business,tearoff=0)
business.add_cascade(font=mainMenuFont,label="Top Industries", menu=topIndustries)

stockMarket=Menu(education,tearoff=0)
finanace.add_cascade(font=mainMenuFont,label="stock Market", menu=stockMarket)
nifty=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Nifty", menu=nifty)
nifty.add_command(label="Bank Nifty", command=doNothing)
nifty.add_command(label="Reliance", command=doNothing)
nifty.add_command(label="Mutual Funds", command=doNothing)
sensex=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Sensex", menu=sensex)
nasdaq=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Nasdaq", menu=nasdaq)
dowJones=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Dow Jones", menu=dowJones)
sandp=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="S&P", menu=sandp)
dax30=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Dax30", menu=dax30)
ftse=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="FTSE", menu=ftse)
hengseng=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Heng Seng", menu=hengseng)
shanghai=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Shanghai", menu=shanghai)
nikkei=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Nikkei", menu=nikkei)
straitstimes=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Straits Times", menu=straitstimes)
kospi=Menu(stockMarket,tearoff=0)
stockMarket.add_cascade(font=mainMenuFont,label="Kospi", menu=kospi)

tax=Menu(education,tearoff=0)
finanace.add_cascade(font=mainMenuFont,label="Tax", menu=tax)

#healthcare
helathcare=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Helath Care", menu=helathcare)

#movies
movies=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Movies", menu=movies)
bollywood=Menu(movies,tearoff=0)
movies.add_cascade(font=mainMenuFont,label="Bollywood", menu=bollywood)
bollywood.add_command(label="Sanju", command=doNothing)

#politics
politics=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Politics", menu=politics)

#research
research=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Research", menu=research)

#service
service=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Service", menu=service)

#sports
sports=Menu(selectCategory,tearoff=0)
selectCategory.add_cascade(font=mainMenuFont,label="Sports", menu=sports)

#ADD Category
addCategory=Menu(menu,tearoff=0)
menu.add_cascade(label="Add Category", menu=addCategory)

#Select Location 
selectLocation=Menu(menu,tearoff=0)
menu.add_cascade(font=mainMenuFont,label="Select Location", menu=selectLocation)

australia=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="Australia", menu=australia)
australia.add_command(label="Adelaide", command=doNothing)
australia.add_command(label="Brisbane", command=doNothing)
australia.add_command(label="Canberra", command=doNothing)
australia.add_command(label="Melbourne", command=doNothing)
australia.add_command(label="Perth", command=doNothing)
australia.add_command(label="Sydney", command=doNothing)



india=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="INDIA", menu=india)
india.add_command(label="Ahmedabad", command=doNothing)
india.add_command(label="Bangalore", command=doNothing)
india.add_command(label="Bhopal", command=doNothing)
india.add_command(label="Chennai", command=doNothing)
india.add_command(label="Hyderabad", command=doNothing)
india.add_command(label="Indore", command=doNothing)
india.add_command(label="Kolkata", command=doNothing)
india.add_command(label="Lucknow", command=doNothing)
india.add_command(label="Mumbai", command=doNothing)
india.add_command(label="Nagpur", command=doNothing)
india.add_command(label="Patna", command=doNothing)
india.add_command(label="Srinagar", command=doNothing)


unitedStates=Menu(selectLocation,tearoff=0)
selectLocation.add_cascade(font=mainMenuFont,label="United States", menu=unitedStates)
unitedStates.add_command(label="Chicago", command=doNothing)
unitedStates.add_command(label="Dallas", command=doNothing)
unitedStates.add_command(label="Denver", command=doNothing)
unitedStates.add_command(label="New York", command=doNothing)
unitedStates.add_command(label="Richmond City", command=doNothing)
unitedStates.add_command(label="San Francisco", command=doNothing)
unitedStates.add_command(label="Travis", command=doNothing)


#Select User Type
selectUserType=Menu(menu,tearoff=0)
menu.add_cascade(label="Select UserType", menu=selectUserType)
selectUserType.add_command(label="Verified User", command=doNothing)
selectUserType.add_command(label="All User", command=doNothing)

#Select Real Time Data

rTD=Menu(menu,tearoff=0)
menu.add_cascade(label="Real Time Data", menu=rTD)
rTD.add_command(label="Sentiment On Current Data", command=doNothing)


#Select GraphType
GraphType=Menu(menu,tearoff=0)
menu.add_cascade(label="Select Graph Type", menu=GraphType)
GraphType.add_command(label="Tag Cloud", command=doNothing)
GraphType.add_command(label="Positive Word Cloud", command=doNothing)
GraphType.add_command(label="Negative Word Cloud", command=doNothing)
GraphType.add_command(label="Sentiment Result", command=doNothing)
GraphType.add_command(label="Pie Chart", command=doNothing)
GraphType.add_command(label="Bar Chart", command=doNothing)
GraphType.add_command(label="Horizontal Bar Chart", command=doNothing)
GraphType.add_command(label="Percentage Graph", command=doNothing)

GraphType.add_command(label="Sentiment Analysis In 3D Model", command=doNothing)
GraphType.add_command(label="Sentiment Analysis In 3D Model In Percentage", command=doNothing)

#settings
settings=Menu(menu,tearoff=0)
menu.add_cascade(label="Settings", menu=settings)
settings.add_command(label="Night Mode", command=nightMode)
settings.add_command(label="Day Mode", command=dayMode)

#Create Frame From Search Bar Graph display 
windowMT=Frame(window,borderwidth=2, relief="ridge",bg="#1E88E5")
windowMT.place(x=00, y=0, width=1050, height=60)

#Add Search Bar 
search=Entry(windowMT, font=fontTwo,borderwidth=2,  relief="groove" )
search.insert(0, 'Enter Search Term...')
search.bind('<FocusIn>',isSearchEntered)
search.place(x=150, y=20, width=550, height=25)

#Add Search Button
searchButton=Button(windowMT,text="Search",fg='#ffffff', bg="#424242", font=fontOne,borderwidth=2, relief="raised",  command=doNothing)
searchButton.place(x=710, y=17, width=100, height=30)

#Create Frame For Graph Display Terms
windowMM=Frame(window,borderwidth=2, relief="ridge",bg="#FFFFFF")
windowMM.place(x=0, y=60, width=1050, height=600)


windowMB=Frame(window,borderwidth=2, relief="ridge",bg="#388E3C")
windowMB.place(x=0, y=600, width=1050, height=132)

#add save button
saveButton=Button(windowMB,text="Save Image", font=fontOne ,borderwidth=2, relief="raised", command=doNothing,fg='#ffffff', bg="#424242")
saveButton.place(x=25, y=85, width=120, height=30)

#add share  facebook button
shareButtonFacebook=Button(windowMB,text="Share On Facebook", font=fontOne,borderwidth=2, relief="raised", command=doNothing,fg='#ffffff', bg="#424242")
shareButtonFacebook.place(x=180,y=85, width=200, height=30)

#add share  twitter button
shareButtonTwitter=Button(windowMB,text="Share On Twitter", font=fontOne,borderwidth=2, relief="raised", command=doNothing,fg='#ffffff', bg="#424242")
shareButtonTwitter.place(x=430,y=85, width=200, height=30)

#add share  instagram button
shareButton=Button(windowMB,text="Share On Instagram", font=fontOne,borderwidth=2, relief="raised", command=doNothing,fg='#ffffff', bg="#424242")
shareButton.place(x=680,y=85, width=200, height=30)

#add email button
exportButton=Button(windowMB,text="Email It", font=fontOne,borderwidth=2, relief="raised",command=doNothing,fg='#ffffff', bg="#424242")
exportButton.place(x=920, y=85, width=95, height=30)

#Create Frame For Displaying Trends Name
windowRTC=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
windowRTC.place(x=1050, y=0, width=316, height=30)

#Create Lable For Twitter Trends
twitterTrends = Label(windowRTC,background="#263238",foreground="#FFFFFF", text="Current Trends",font=fontThree, borderwidth=2, relief="groove")
twitterTrends.place(x=0, y=0, width=314, height=30)

#Create Frame For Displaying Current Trends
windowRTT=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
windowRTT["bg"] = "#388E3C"
windowRTT.place(x=1050, y=30, width=316, height=270)

#Add Scrollbar Trends
scrollbarTrendss = Scrollbar(windowRTT)
scrollbarTrendss.pack( side = RIGHT, fill=Y )


#Create Frame For Displaying Trends Name
windowRTCC=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
windowRTCC.place(x=1050, y=300, width=316, height=30)

#Create Frame For Top Tweets
twitterTrends = Label(windowRTCC, background="#263238",foreground="#FFFFFF", text="Top Tweets",font=fontThree, borderwidth=2, relief="groove")
twitterTrends.place(x=0, y=0, width=314, height=30)

#Create Frame For Displaying Tweets From Verified Users
windowRBB=Frame(window,borderwidth=2, relief="ridge",bg="WHITE")
windowRBB["bg"] = "#1E88E5"
windowRBB.place(x=1050, y=330, width=316, height=400)

#Add Scrollbar Top Tweets
scrollbarTopTweetss = Scrollbar(windowRBB)
scrollbarTopTweetss.pack( side = RIGHT, fill=Y )


window.mainloop()
