from django.shortcuts import render,redirect
from .models import*
from random import randint
# Create your views here.
def indexpage(request):
    return render(request,"jagruti/index.html")

def signuppage(request):
    return render(request,"jagruti/signup.html")

def RegisterUser(request):
    if request.POST['role'] == 'Candidate':
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password  = request.POST['password']
        cpassword = request.POST['cpassword']


        user = UserMaster.objects.filter(email=email)
        
        if user:
            message = "User already register."
            return render(request,"jagruti/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)

            newuser = UserMaster.objects.create(role=role,email=email,password=password,otp=otp)
            newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname,)    
            return render(request,"jagruti/otpverify.html",{'email':email})
    else:
         if request.POST['role'] == 'Company':
             role = request.POST['role']
             fname = request.POST['firstname']
             lname = request.POST['lastname']
             email = request.POST['email']
             password = request.POST['password']
             cpassword = request.POST['cpassword']

             user = UserMaster.objects.filter(email=email)

             if user:
                 message = "User already exist."
                 return render(request,"jagruti/signup.html")
             else:
                 if password == cpassword:
                     otp = randint(100000,999999)
            
                 newuser = UserMaster.objects.create(role=role,email=email,password=password,otp=otp)
                 newcomp = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                 return render(request,"jagruti/otpverify.html",{'email':email})
             

def OtpPage(request):
    return render(request,"jagruti/otpverify.html")

def OtpVefrify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "Otp verify successfully."
            return render(request,"jagruti/login.html",{'msg':message})
        else:
            message = "Otp is incorrect ."
            return render(request,"jagruti/otpverify.html",{'msg':message})
    else:
        return render(request,"jagruti/signup.html")
    
def loginpage(request):
    return render(request,"jagruti/login.html")

def LoginUser(request):
    if request.POST['role'] == 'Candidate':
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)

        if user:
            if user.password == password and user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                return redirect('index')
            else:
                message = "Password is incorrect ."
                return render(request,"jagruti/login.html",{'msg':message})
        else:
            message = "User doesnot exist."
            return render(request,"jagruti/login.html",{'msg':message})
        
    else:
        if request.POST['role'] == 'Company':
            email = request.POST['email']
            password = request.POST['password']

            user = UserMaster.objects.get(email=email)

            if user.password == password and user.role == "Company":
                comp = Company.objects.get(user_id=user)
                request.session['id'] = user.id 
                request.session['role'] = user.role
                request.session['firstname'] = comp.firstname
                request.session['lastname'] = comp.lastname
                request.session['email'] = user.email
                request.session['password'] = user.password
                return redirect('companyindex')
            else:
                message = "Password is incorrect."
                return render(request,"jagruti/login.html",{'msg':message})
        else:
            message = "User doesnot exist."
            return render(request,"jagruti/login.html")



def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"jagruti/profile.html",{'user':user,'can':can})

def updateprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)

    if user.role == 'Candidate':
        can = Candidate.objects.get(user_id=user)
        can.state = request.POST['state']
        can.city = request.POST['city']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['category']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['description']
        can.min_salary = request.POST['minsalary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.save()
        url = f'/profilepage/{pk}'
        return redirect(url)
    

def ApplyPage(request,pk):
    user = request.session['id']  
    if user:
        cand = Candidate.objects.get(user_id = user)
        job = JobDeatils.objects.get(id=pk)
    return render(request,"jagruti/apply.html",{'user':user,'cand':cand,'job':job})

def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDeatils.objects.get(id=pk)
        edu = request.POST['education']
        exp = request.POST['experience']
        web = request.POST['website']
        gender = request.POST['gender']
        min_salary = request.POST['minsalary']
        max_salary = request.POST['maxsalary']
        newapply  =  Applylist.objects.create(candidate=can,job=job,education=edu,experience=exp,website=web
                                            ,min_salary=min_salary,max_salary=max_salary,gender=gender)
                                         
        message = "Job applied successfully."
        return render(request,"jagruti/apply.html",{'msg':message})

############################################################ Company Page #######################################################

def companyindex(request):
    return render(request,"jagruti/company/index.html")

def companyprofilepage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id=user)
    return render(request,"jagruti/company/profile.html",{'user':user,'comp':comp})
        
def updatecompanyprofile(request,pk):
    user = UserMaster.objects.get(pk=pk)

    if user.role == 'Company':
        comp = Company.objects.get(user_id=user)
        comp.company_name = request.POST['companyname']
        comp.state = request.POST['state']
        comp.city = request.POST['city']
        comp.contact = request.POST['contact']
        comp.website = request.POST['website']
        comp.description = request.POST['description']
        comp.save()
        url = f'/companyprofilepage/{pk}'
        return redirect(url)
    
def jobpostpage(request):
    return render(request,"jagruti/company/jobpost.html")

def jobdetailssubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        address = request.POST['companyaddress']
        jobdescription  = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsebility = request.POST['responsbility']
        location  = request.POST['location']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['contact']
        salary = request.POST['salary']
        experience = request.POST['experience']
        website = request.POST['website']
        

        newjob = JobDeatils.objects.create(company_id=comp,jobname=jobname,companyname=companyname,comapanyaddress=address,jobdescription=jobdescription,
        qualification=qualification,responsibilities=responsebility,location=location,companywebsite=website,coampanyemail=companyemail,
        companycontact=companycontact,salarypackage=salary,experience=experience)
         

        message = "Job post successfully."
        return render(request,"jagruti/company/jobpost.html",{'msg':message})
    
def jobpostlist(request):
    all_job = JobDeatils.objects.all()
    return render(request,"jagruti/company/jobpostlist.html",{'all_job':all_job})

def Candidatejobpostlist(request):
    all_job = JobDeatils.objects.all()
    return render(request,"jagruti/job-list.html",{'all_job':all_job})

def JobApplyList(request):
    all_jobapply = Applylist.objects.all()
    return render(request,"jagruti/company/applyjoblist.html",{'all_job':all_jobapply})

def CompanyLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')


############################### Admin #######################

def AdminPage(request):
    return render(request,"jagruti/admin/login.html")

def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"jagruti/admin/index.html")
    else:
        return redirect('adminloginpage')
def AdminLogin(request):
    username = request.POST['uname']
    password = request.POST['password']

    if username == "jay" and password == "jay":
        request.session['uname'] = username
        request.session['password'] = password
        return redirect('adminindexpage')
    else:
        message = "User doesn't match."
        return render(request,"jagruti/admin/login.html",{'msg':message})
    
def AdminCandidateUser(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"jagruti/admin/candidateuserlist.html",{'alluser':all_user})

def AdminCompanyUser(request):
    all_user = UserMaster.objects.filter(role="Company")
    return render(request,"jagruti/admin/companyuserlist.html",{'alluser':all_user})   