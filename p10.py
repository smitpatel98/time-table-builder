import urllib
from bs4 import BeautifulSoup
import  requests
import jsbeautifier
import xlwt 
from datetime import datetime
from xlwt import Workbook 
import  xlsxwriter
import itertools 

wb= Workbook()

workbook = xlsxwriter.Workbook('TB.xlsx') 
worksheet = workbook.add_worksheet() 
worksheet.write(0,0,'NAME')
worksheet.write(0,2,'Place')
worksheet.write(0,3,'TIME')
worksheet.write(0,1,'Days')
worksheet.write(0,4,'Type')

#makes shortform for the building names
def shortform(j):
    if(j.rfind("Comp")):
        return("ECS")
    if(j.rfind("Bob")):
        return("BWC")
    if(j.rfind("David")):
        return("DTB")
    if(j.rfind("Elliot")):
        return("Ell")
    if(j.rfind("Contin")):
        return("CST")
    if(j.rfind("Lab")):
        return("ELW")
    if(j.rfind("Fine Arts")):
        return("FIA")
    if(j.rfind("Hickman")):
        return("HH")
    if(j.rfind("uman")):
        return("HSD")
    if(j.rfind("McLauri")):
        return("MAC")
    if(j.rfind("McKi")):
        return("MCK")
    if(j.rfind("Petch")):
        return("PCh")
    if(j.rfind("Strong")):
        return("DSB")
    if(j.rfind("Social Sciences")):
        return("SSM")
    if(j.rfind("Visua")):
        return("VIA")
    if(j.rfind("Clearihu")):
        return("CLE")

def daysign(now):
    name=now.weekday()
    print(name)
    if(name==0):
        return("M")
    elif(name==1):
        return("T")
    elif(name==2):
        return("W")
    elif(name==3):
        return("R")
    elif(name==4):
        return("F")
    elif(name==5):
        return("S")


# this function will create xl file. NOT COMPLETED. Author- Saumya & Vibhu
def xlgenerator(place,time,day,typ,crsname,crsnum ):
    url=urlmaker(crsname,crsnum)
    n=1
    name=crsname+' '+crsnum
    while(n<=len(place)):
        d=day[n-1]
        t=time[n-1]
        p=place[n-1]
        ty=typ[n-1]
        temp=shortform(p)
        worksheet.write(n,0,name)
        worksheet.write(n,1,d)
        worksheet.write(n,2,p)
        worksheet.write(n,3,t)
        worksheet.write(n,4,ty)
        n+=1
    # worksheet.write(n,3,time)
    
    # for j in type:
    #     sheet.write(n,3,j)

        # sheet.write(n,3,j)
        # sheet.write(n,4,k)
        # sheet.write(n,5,l)
    
    
    workbook.close()

        

def combinations(place,time,day,typ):
    print (day)
    lec=[]
    lab=[]
    sec=["A01","A02","B01","B02","B03","B04"]
    sec_comb=[]
    sec_comb_lab=[]
    section_combi=[]
    c=0
    for i in typ:
        if(i=="Lecture"):
            lec+= [day[c]]
            sec_comb+=[sec[c]]
            c+=1
            
        elif(i=="Lab" or i=="Tutorial"):
            lab+= [day[c]]
            sec_comb_lab+=[sec[c]]
            c+=1
    comb=(itertools.product(lec, lab))
    sections=(itertools.product(sec_comb,sec_comb_lab))
    #for l in comb:
        #print(l)
    #for x,y in sections:
        #section_combi+=[x+" "+y]
    #print(section_combi)
   
    # c1=len(lec)+1
    # start=0
    # comb1=[]
    # try
    # for i in range(start:len(lec)-c1):
    #     for j in range(len(i)):
    #         comb1+=[lec[j]]
    #     c1+=1
    #     start+=1
    
#this function creates initital list that lister needs. Author- Saumya
def listmaker(list1,url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    l=""
    lis1=[]
    lis2=[]
    text=""
    lis=soup.find_all("td",{"class":"dddefault"})
    for i in range(len(lis)):
        lis1+=lis[i].find_all("td")
    lis2+=lis1
    for j in lis2:
        text=""
        for k in j:
            
            for char in '<>tdclass="dddefaultEveryWeek/<=abbr titlr>TBA':
                if(k==char):
                    k=(k.replace(char," "))
                    k=k.strip(" ")
        

        list1+=[k]
      

def listmaker(list1,url):
    soup = BeautifulSoup(urllib.request.urlopen(url).read())
    l=""
    lis1=[]
    lis2=[]
    text=""
    lis=soup.find_all("td",{"class":"dddefault"})
    for i in range(len(lis)):
        lis1+=lis[i].find_all("td")
    lis2+=lis1
    for j in lis2:
        text=""
        for k in j:
            
            for char in '<>tdclass="dddefaultEveryWeek/<=abbr titlr>TBA':
                if(k==char):
                    k=(k.replace(char," "))
                    k=k.strip(" ")
        

        list1+=[k]
      

#this function will create the final list - Author- Vibhu
def lister(l,date1,place,time1,day,typec,crn):
    i=0
    l1=[]
    date=[]
    for a in l:
        i+=1
        if(a!= None):
            try:
                alpha=a.split()
                temp=''
                #print("here")
                for b in alpha:
                    temp+=b  
                #print(temp)
                if ((temp.rfind("am")) or (temp.rfind("pm"))):
                    l1.append(temp)
                
                
            except:
                alpha=None
                #print("none")
        else:
            i=1
    #print(l1)
    for a in l1:
        temp=a.splitlines()
        try:
            here=temp[0]
            #print(here)
            if ((here.rfind("am")>0) or (here.rfind("pm")>0)):
                time1.append(here)
            elif((here.rfind("ab")>0) or (here.rfind("utorial")>0) or (here.rfind("ecture")>0)):
                typec.append(here)
            elif(here=="TWF" or here=="R" or here=="M" or here == "T" or here=="W" or here=="F" or here== "MWF" or here=="MWR" or here=="TRF" or here=="MW" or here=="MR"):
                day.append(here)
            elif((here.rfind("ichael")>0) or (here.rfind("avid")>0) or (here.rfind("lliot")>0) or (here.rfind("ngineering")>0) or (here.rfind("ob")>0) or (here.rfind("uisness")>0) or (here.rfind("arquhar")>0)  or (here.rfind("raser")>0) or (here.rfind("ickman")>0) or (here.rfind("uman")>0) or (here.rfind("acLaurin")>0) or (here.rfind("cean")>0) or (here.rfind("trong")>0) or (here.rfind("isual")>0) or (here.rfind("learihue")>0)):
                place.append(here)
            elif((here.rfind("201")>0)):
                date.append(here)
            elif((here.rfind("10")>0)):
                crn.append(here)
                    
        except:
            continue
    i=0
    while(i<len(date)):
        if(date[i]== None):
            i+=1
            continue
        else:
            a=date[i]
            flag=0
            temp=''
            for z in a:
                if(z=="-"):
                    break
                if(z.isnumeric() and flag==0):
                    temp+=" "
                    temp+=z
                    flag=1
                else:
                    temp+=z       
            now=datetime.strptime(temp,'%B %d,%Y')
            year=2019
            month=None
            date1.append(now)
            i+=1
    i=0
    a=''
    while(i<len(date)):
        if((i+1)>len(day)):
            day.append(a)
        elif((i+1)==len(day)):
            a=day[i]
        i+=1
    print(len(date))

        
    


def urlmaker(crsname,crsnum):
    base='https://www.uvic.ca/BAN1P/bwckctlg.p_disp_listcrse?term_in=201905&subj_in='
    end='&schd_in=%'
    url=base+crsname+'&crse_in='+crsnum+end
    return url

def main():
    url=urlmaker('CSC','115')
    list1=[]
    date=[]
    place=[]
    time=[]
    day=[]
    typec=[]
    prof=[]
    time1=[]
    crn=[]
    listmaker(list1,url)
    print(list1)
    lister(list1,date,place,time1,day,typec,crn)    
    xlgenerator(place,time1,day,typec,"CSC","115" )
    day10=["TWF", "MWR","T","R","W","M"]
    combinations(place,time,day10,typec)


main()