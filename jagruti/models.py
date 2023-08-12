from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)


class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    dob  = models.CharField(max_length=50,default="")
    jobdescription = models.CharField(max_length=50,default="")
    jobcategory = models.CharField(max_length=50,default="")
    highestedu = models.CharField(max_length=50,default="")
    shift  = models.CharField(max_length=50,default="")
    job_type = models.CharField(max_length=50,default="")
    experience = models.CharField(max_length=50,default="")
    min_salary  = models.CharField(max_length=50,default="")
    max_salary = models.CharField(max_length=50,default="")
    website = models.CharField(max_length=50,default="")
    profile_pic = models.ImageField(upload_to="jagruti/img/candidate")

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname  = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    website = models.CharField(max_length=50,default="")
    description = models.CharField(max_length=500,default="")
    logo_pic = models.ImageField(upload_to="jagruti/img/company")


class JobDeatils(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE,default="")
    jobname = models.CharField(max_length=250)
    companyname = models.CharField(max_length=250)
    comapanyaddress = models.CharField(max_length=250)
    jobdescription = models.TextField(max_length=250)
    qualification = models.CharField(max_length=250)
    responsibilities = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    companywebsite = models.CharField(max_length=250)
    coampanyemail = models.CharField(max_length=250)
    companycontact = models.CharField(max_length=250)
    salarypackage = models.CharField(max_length=250)
    experience = models.CharField(max_length=250)

class Applylist(models.Model):
    candidate = models.ForeignKey(Candidate,on_delete=models.CASCADE)
    job = models.ForeignKey(JobDeatils,on_delete=models.CASCADE)
    education = models.CharField(max_length=200)
    experience = models.CharField(max_length=200,default="")
    website = models.CharField(max_length=200)
    min_salary = models.CharField(max_length=200)
    max_salary = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
