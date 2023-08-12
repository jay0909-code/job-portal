from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.indexpage,name="index"),
    path("signup/",views.signuppage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OtpPage,name="otppage"),
    path("otpverify/",views.OtpVefrify,name="otpverify"),
    path("loginpage/",views.loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="loginuser"),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("updateprofile/<int:pk>",views.updateprofile,name="updateprofile"),
    path("candidatejobpostlist/",views.Candidatejobpostlist,name="candidatejobpostlist"),
    path("applypage/<int:pk>",views.ApplyPage,name="applypage"),
    path("applyjob/<int:pk>",views.ApplyJob,name="applyjob"),


    ############################################# Company Page ###########################################################################

    path("companyindex/",views.companyindex,name="companyindex"), 
    path("companyprofilepage/<int:pk>",views.companyprofilepage,name="companyprofilepage"),
    path("updatecompanyrpofile/<int:pk>",views.updatecompanyprofile,name="updatecompanyprofile"),
    path("jobpostpage/",views.jobpostpage,name="jobpostpage"),
    path("jobpost/<int:pk>",views.jobdetailssubmit,name="jobpost"),
    path("jobpostlist/",views.jobpostlist,name="jobpostlist"),
    path("companylogout/",views.CompanyLogout,name="companylogout"),
    path("applyjoblist/",views.JobApplyList,name="applyjoblist"),



    ####################################### Admin ###############################################

    path("adminloginpage/",views.AdminPage,name="adminloginpage"),
    path("adminindexpage/",views.AdminIndexPage,name="adminindexpage"),
    path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminCandidateUser,name="userlist"),
    path("admincompanylist/",views.AdminCompanyUser,name="companylist"),

]