from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog 
import util
import magicScript as ms
s=Tk()
s.title('CV shortlisting')
s.geometry('800x500')
bgcolor="lemon chiffon"
s.configure(background=bgcolor)
name=''
def home():
    s1=Tk()
    s1.title('Home')
    s1.geometry('850x500')
    s1.configure(background=bgcolor)
    welcome=Label(s1,text="Welcome "+name,font='bold 18',bg=bgcolor).pack()
    option=Menu(s1)
    def clear():
        list=[]
        for w in s1.children.values():
            list.append(w)
        for i in range(2,len(list)):
            list[i].destroy()            

    menus=Menu(option,tearoff=0)
    option.add_cascade(label="Menu",menu=menus)
    def apply():
        clear()
        l=Label(s1,text="Select a job title : ",bg=bgcolor).place(x=55,y=50)
        #code to fetch all the job titles available in db
        #give all the job titles in list named 'job'
        c = util.Utility()
        job = []
        for row in c.fetchJobs():
            job.append(row[1])
        #code ends
        var=StringVar()
        var.set(job[0])
        def select():
            jobtitle=var.get()
            #title selected in variable 'jobtitle'
            #fetch all the jobs posted on this title along with their perks.
            #get the variables company name,salary,jobtype,requirements,location,experience,description
            c = util.Utility()
            xp = c.fetchJobWhere(jobtitle)
            print(xp)
            for row in c.fetchJobWhere(jobtitle):
                print(row)
                jobId = row[0]
                title = row[1]
                company=row[2]
                salary=row[3]
                jobtype=row[4]
                requirements=row[8].split(',')
                location=row[5]
                exp=row[6]
                desc=row[7]
                companyl=Label(s1,text="Company Name : "+company,bg=bgcolor).place(x=55,y=100)
                salaryl=Label(s1,text="Salary : Rs. "+str(salary),bg=bgcolor).place(x=55,y=120)
                jobypel=Label(s1,text="Job Type : "+jobtype,bg=bgcolor).place(x=55,y=140)
                reql=Label(s1,text="Requirements : ",bg=bgcolor).place(x=55,y=160)
                xp=100
                for i in requirements:
                    txt=", "+i
                    xp=xp+30
                    reql=Label(s1,text=txt,bg=bgcolor).place(x=xp,y=160)
                locationl=Label(s1,text="Location : "+location,bg=bgcolor).place(x=55,y=180)
                expl=Label(s1,text="Experience : "+str(exp),bg=bgcolor).place(x=55,y=200)
                descl=Label(s1,text="Description : "+desc,bg=bgcolor).place(x=55,y=220)
                
                def apply():
                    c = util.Utility()
                    
                    c.applyJob(name,cvPath,jobId,title,company,userId,"Applied")
                    l=Label(s1,text="Applied successfully",bg=bgcolor,fg="blue").place(x=100,y=240)
                    
                apply=Button(s1,text="Apply",command=apply).place(x=55,y=240)
                
                
        title=OptionMenu(s1,var,*job)
        title.place(x=200,y=45)
        select=Button(s1,text="Select",command=select).place(x=320,y=45)

    def post():
        clear()
        title=Label(s1,text="Enter job title : ",bg=bgcolor).place(x=55,y=50)
        title=Entry(s1)
        title.place(x=137,y=50)
        company=Label(s1,text="Company name : ",bg=bgcolor).place(x=300,y=50)
        company=Entry(s1)
        company.place(x=400,y=50)
        salary=Label(s1,text="Salary : Rs. ",bg=bgcolor).place(x=570,y=50)
        salary=Entry(s1)
        salary.place(x=633,y=50)
        jobtype=Label(s1,text="Job Type : ",bg=bgcolor).place(x=55,y=95)
        jobtype=IntVar()
        full=Radiobutton(s1,text="Full time",bg=bgcolor,variable=jobtype,value=1)
        part=Radiobutton(s1,text="Part time",bg=bgcolor,variable=jobtype,value=2)
        home=Radiobutton(s1,text="Work from home",bg=bgcolor,variable=jobtype,value=3)
        full.place(x=120,y=95)
        part.place(x=210,y=95)
        home.place(x=300,y=95)
        require=Label(s1,text="Requirements : ",bg=bgcolor).place(x=55,y=140)
        require=Entry(s1)
        require.place(x=150,y=140)
        requirements=[]
        def add():
            # global requirements =[]
            r=require.get()
            requirements.append(r)  #all requirements stored in list 'requirements'
            require.delete(0,END)

        add=Button(s1,text="+ Add",command=add).place(x=290,y=137)
        location=Label(s1,text="Location : ",bg=bgcolor).place(x=55,y=190)
        location=Entry(s1)
        location.place(x=115,y=190)
        exp=Label(s1,text="Experience : ",bg=bgcolor).place(x=55,y=230)
        exp=Spinbox(s1,from_=0,to=15,increment=1,width=5)
        exp.place(x=125,y=230)
        expe=Label(s1,text="yrs",bg=bgcolor).place(x=170,y=230)
        desc=Label(s1,text="Job Description : ",bg=bgcolor).place(x=55,y=275)
        desc=Entry(s1)
        desc.place(x=150,y=275)
        def post_submit():
            title1=title.get()
            company1=company.get()
            salary1=salary.get()
            jobtype1=jobtype.get()
            if(jobtype1 == 1):
                jobType = "Full Time"
            elif(jobtype1 == 2):
                jobType = "Part Time"
            else:
                jobType = "Work From Home"
            location1=location.get()
            exp1=exp.get()
            desc1=desc.get()
            #to database
            c = util.Utility()
            if(c.insertJob(title1,company1,salary1,jobType,location1,exp1,desc1,requirements,userId)):
                # Zeel Iske baad write Code TO clear Screen And go to Home 
                pass
            
        post=Button(s1,text="Post",command=post_submit).place(x=65,y=320)
    menus.add_command(label="Apply for job",command=apply)
    menus.add_command(label="Post a job",command=post)
    menus.add_separator()
    menus.add_command(label="Exit",command=s1.destroy)

    view=Menu(option,tearoff=0)
    option.add_cascade(label="View",menu=view)
    def score():
        pass
    def jobs():
        def applied():
            #users name is stored in variable 'name'
            #fetch data of all the applied jobs
            #give job title in variable 'jobtitle'
            #give company name in variable 'company'
            #start loop
            c = util.Utility()
            for row in c.fetchApplied(name,userId):
                jobtitle = row[4]
                company = row[5]
                status = row[7]
                title=Label(s1,text="Jobtitle : "+jobtitle,bg=bgcolor).place(x=55,y=100)
                compname=Label(s1,text="Company : "+company,bg=bgcolor).place(x=55,y=120)
                #give status like shortlisted,selected,rejected in variable 'status'
                statusl=Label(s1,text="Status : "+status,fg="white")
                statusl.place(x=205,y=110)
                if(status=='Rejected'):
                    statusl.configure(bg="red")
                elif(status=='Shortlisted'):
                    statusl.configure(bg="maroon")
                elif(status=='Selected'):
                    statusl.configure(bg="green")
                elif(status == 'Applied' or status == 'Sorted'):
                    statusl.configure(bg="blue")
                else:
                    statusl.configure(bg=bgcolor)
        def posted():
            #fetch data of all posted jobs
            #give job title in variable 'jobtitle'
            #give vacancy in variable 'vacancy'
            #start loop
            jobtitle = "Maybe no one applied or all rejected"
            candidate = []
            vacancy =2
            c = util.Utility()
            ms.startToShortlist(userId)
            title=Label(s1,text="Jobtitle : "+jobtitle,bg=bgcolor).place(x=445,y=100)
            vacancy=Label(s1,text="Vacancy : "+str(vacancy),bg=bgcolor).place(x=600,y=100)
            yp=120
            xp=500
            for row in c.fetchPostedJobs_status_Sorted(userId):
                jobtitle = row[2]
                cvpath = row[1]
                userIdx = row[5]
                jobIdx = row[4]
                cvs = cvpath.split("/")
                theCV = ""  
                for cv in cvs:
                    if(cv.find(".pdf") != -1):
                        theCV = cv
                def select():
                    select.configure(relief=SUNKEN)
                    c.updateStatus(userIdx,jobIdx,"Selected")
                def reject():
                    c.updateStatus(userIdx,jobIdx,"Rejected")
                def hire():
                    c.updateStatus(userIdx,jobIdx,"Hired")
                l=Label(s1,text=theCV,bg=bgcolor).place(x=xp,y=yp)
                select=Button(s1,text="Select",command=select)
                select.place(x=xp+50,y=yp)
                reject=Button(s1,text="Reject",command=reject)
                reject.place(x=xp+100,y=yp)
                hire=Button(s1,text="HIRE",command=hire)
                hire.place(x=xp+200,y=yp)
                yp=yp+50
        applied=Button(s1,text="Applied Jobs",command=applied).place(x=285,y=60)
        posted=Button(s1,text="Posted Jobs",command=posted).place(x=445,y=60)
    def progress():
        pass
    view.add_command(label="Resume Score",command=score)
    view.add_command(label="Jobs",command=jobs)
    view.add_command(label="Progress",command=progress)

    
    settings=Menu(option,tearoff=0)
    option.add_cascade(label="Settings",menu=settings)
    def resume():
        pass
    def password():
        clear()
        p=Label(s1,text="Enter your previous password : ",bg=bgcolor).place(x=60,y=100)
        p=Entry(s1)
        p.place(x=61,y=123)
        cp=Label(s1,text="Enter your new password : ",bg=bgcolor).place(x=60,y=155)
        cp=Entry(s1)
        cp.place(x=61,y=178)
        def change():
            prevpass=p.get() #old password in variable 'prevpass'
            newpass=cp.get() #old password in variable 'newpass'
            c = util.Utility()
            if(c.authenticate(name,prevpass)):
                c.changePassword(name,prevpass,newpass)
                l=Label(s1,text="Successfully changed !!!",bg=bgcolor).place(x=60,y=270)
        change=Button(s1,text="Change",width=7,bg="blue",fg="white",command=change).place(x=70,y=228)
    def editinfo():
        pass
    def delete():
        pass
    settings.add_command(label="Update resume",command=None)
    settings.add_command(label="Change Password",command=password)
    settings.add_command(label="Edit Info",command=None)
    settings.add_separator()
    settings.add_command(label="Delete account",command=None)

    help=Menu(option,tearoff=0)
    option.add_cascade(label="Help",menu=help)
    def improve():
        pass
    def process():
        pass
    def contact():
        pass
    help.add_command(label="Improve Score",command=None)
    help.add_command(label="Shortlisting process",command=None)
    help.add_command(label="Contact",command=None)
    s1.config(menu=option)
    s1.mainloop()
def newuser():
    s.destroy()
    s2=Tk()
    s2.title('Sign up')
    s2.geometry('850x550')
    s2.configure(background=bgcolor)
    welcome=Label(s2,text="Please enter your details . . .",bg=bgcolor,font="bold").pack()
    username=Label(s2,text="*Name : ",bg=bgcolor).place(x=55,y=50)
    username=Entry(s2)
    username.place(x=105,y=50)
    sname=Label(s2,text="*Surame : ",bg=bgcolor).place(x=330,y=50)
    sname=Entry(s2)
    sname.place(x=390,y=50)
    ages=Label(s2,text="*Age : ",bg=bgcolor).place(x=590,y=50)
    ages = Spinbox(s2,from_=18,to=65,increment=1)
    ages.place(x=630,y=50)
    genders=Label(s2,text="Gender : ",bg=bgcolor).place(x=55,y=105)
    var=IntVar()
    male=Radiobutton(s2,text="Male",bg=bgcolor,variable=var,value=1)
    male.place(x=130,y=105)
    female=Radiobutton(s2,text="Female",bg=bgcolor,variable=var,value=2)
    female.place(x=210,y=105)
    contacts=Label(s2,text="*Contact : ",bg=bgcolor).place(x=55,y=150)
    contacts=Entry(s2)
    contacts.place(x=115,y=150)
    emails=Label(s2,text="*Email Id : ",bg=bgcolor).place(x=55,y=195)
    emails=Entry(s2)
    emails.place(x=115,y=195)
    passwd=Label(s2,text="*Create password : ",bg=bgcolor).place(x=55,y=240)
    passwd=Entry(s2,show="*")
    passwd.place(x=159,y=240)
    cpasswd=Label(s2,text="*Confirm password : ",bg=bgcolor).place(x=55,y=290)
    cpasswd=Entry(s2,show="*")
    cpasswd.place(x=168,y=290)
    adds=Label(s2,text="Address : ",bg=bgcolor).place(x=55,y=340)
    adds=Entry(s2)
    adds.place(x=110,y=340)
    citys=Label(s2,text="*City : ",bg=bgcolor).place(x=55,y=395)
    citys=Listbox(s2,bg="white",height=5)
    citys.insert(1,'Mumbai')
    citys.insert(2,'Delhi')
    citys.insert(3,'Bangalore')
    citys.insert(4,'Hyderabad')
    citys.insert(5,'Chennai')
    citys.place(x=95,y=395)
    resume1=Label(s2,text="Upload Resume : ",bg=bgcolor).place(x=350,y=395)
    def chose():
        global filename 
        filename = filedialog.askopenfilename(title ='Upload Cv') 
        # print(filename)
        resume.configure(text=filename)
        
    resume=Button(s2,text="Choose",command=chose)
    resume.place(x=450,y=395)
    def signup():
        fn=username.get() #user's name stored in 'fn'
        ln=sname.get() #user's surname stored in 'ln'
        age=ages.get() #user's age stored in 'age'
        gender=var.get() #user's gender stored in 'gender'
        contact=contacts.get() #user's contact stored in 'contact'
        email=emails.get() #user's email stored in 'email'
        add=adds.get() #user's address stored in 'add'
        city=citys.get(ACTIVE) #user's city stored in 'city'
        #password
        if(passwd.get() and cpasswd.get() and email and contact and city and fn and ln and age):
            if(passwd.get()!=cpasswd.get()):
                l=Label(s2,text="Error!!! Please retype the password",bg=bgcolor,fg="red").place(x=280,y=240)
            else:
                password=passwd.get()
                #user's password is stored in 'password'
            
                #code to enter data in database#
                c = util.Utility()
                if(c.createUser(fn,ln,age,gender,contact,email,add,city,password,filename)):
                    pass
                #
                #
                #
                #
                #code ends#
                global name
                global userId
                global cvPath
                name = fn
                row = c.authenticate(name,password)
                if(row):
                    userId = row[0]
                    cvPath = row[10]
                    s2.destroy()
                    home()
        else:
            l=Label(s2,text="Please enter all required fields",bg=bgcolor,fg="red").place(x=280,y=500)
    def reset():
        pass
    Submit=Button(s2,text="Submit",bg="black",fg="white",command=signup,width=12).place(x=70,y=500)
    Reset=Button(s2,text="Reset",bg="black",fg="white",command=reset,width=12).place(x=180,y=500)
    s2.mainloop()
def forgot():
    email=simpledialog.askstring("Forgot Password","Please enter your registered email id")
    #email is stored in 'email'
    #code to fetch the corresponding password from the database
    c= util.Utility()
    password = c.forgotPassword(email)
    #give the password in variable 'password'
    #
    #code ends
    messagebox.showinfo(email+"'s Password","Password is "+password)
def login():
    global name
    global userId
    global cvPath
    name=username.get()
    password=passwd.get()
    #code to check if name and password matches
    c = util.Utility()
    row = c.authenticate(name,password)
    if(row):
        userId = row[0]
        cvPath = row[10]
        s.destroy()
        home()
    

global jobId    
welcome=Label(s,text="Please log in !!! ",font='bold 18',bg=bgcolor).place(x=340,y=20)
username=Label(s,text="Username",bg=bgcolor,font=20).place(x=200,y=100)
username=Entry(s,width=50)
username.place(x=200,y=130)
passwd=Label(s,text="Password",bg=bgcolor,font=20).place(x=200,y=170)
passwd=Entry(s,show="*",width=50)
passwd.place(x=200,y=200)
login=Button(s,text="Log in",bg="black",fg="white",width=25,command=login).place(x=200,y=240)
forgot=Button(s,text="Forgot password?",bg=bgcolor,command=forgot,relief=FLAT,font =
               ('calibri', 10, 'bold', 'underline'),fg="blue",activebackground=bgcolor,activeforeground="blue").place(x=400,y=240)
new=Label(s,text="New User?",bg=bgcolor,font=12).place(x=250,y=320)
new=Button(s,text="Sign Up",command=newuser,width=15,bg="black",fg="white").place(x=350,y=320)
s.mainloop()
