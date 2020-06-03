from django.shortcuts import render, redirect
from Citizen_complaint_processing.models import admin, user_info, complaints
from django.contrib import messages


def indexPage(request):
    return render(request,'index.html')


def register(request):
    return render(request,'registration.html')


def adminlogin(request):
    return render(request,'admin_login_page.html')


def userlogin(request):
    return render(request,'user_login_page.html')


def user_verification(request):
    if request.method=="POST":
        username=request.POST['email']
        psswrd=request.POST['password']
        record=user_info.objects.filter(email_id=username)
        if record:
            user_record = user_info.objects.get(email_id=username)
            fetched_password = user_record.password
            if fetched_password == psswrd:
                request.session['username'] = username
                return redirect('/complaintregistration')
            else:
                error_message = "Password didn't match! Re-enter password"
                return render(request,'user_login_page.html', {'error_message': error_message})
        else:
            error_message = "User doesn't exist. Click here to register"
            return render(request, 'user_login_page.html', {'newuser_error_message': error_message})
    else:
        return redirect('/index')


def show_user_account(request):
    # Checking if the user is logged in
    if request.session.has_key('username'):
        uname = request.session['username']
        user_record=user_info.objects.get(email_id=uname)
        #name=user_record.fname
        return render(request,'user_profile.html',{'userinfo':user_record})
    else:
        error_message = "User not logged in!! Login here"
        return render(request, 'user_login_page.html', {'error_message': error_message})


def view_status(request):
    if request.session.has_key('username'):
        user_email=request.session['username']
        user_record=user_info.objects.get(email_id=user_email)
        user_id=user_record.id
        user_complaints=complaints.objects.filter(user_id=user_id)
        return render(request,'complaint_status.html',{'complaints':user_complaints})
    else:
        error_message="User not logged in!! Login here"
        return render(request,'user_login_page.html',{'error_message':error_message})

def show_comp_reg_page(request):
    # First check if the user is logged in
    if request.session.has_key('username'):
        return render(request,'complaint_reg.html')
    else:
        error_message="User not logged in!! Login here"
        return render(request,'user_login_page.html',{'error_message':error_message})


def verify_admin_login(request):
    if request.method=="POST":
        name = request.POST['admin']
        pswd = request.POST['password']
        admin_details=admin.objects.get(id=1)
        username=admin_details.username
        password=admin_details.password
        if name == username and pswd == password:
            request.session['admin']=username
            return redirect('/adminviewcomplaints')
        else:
            error_message="Invalid Credentials"
            return render(request, 'admin_login_page.html',{'error_message':error_message})
    else:
        return redirect('/index')

def register_user(request):
    if request.method=="POST":
        fname=request.POST['f_name']
        sname=request.POST['s_name']
        email_address=request.POST['email_add']
        pswrd=request.POST['password']
        addr=request.POST['address']
        city=request.POST['input_city']
        state=request.POST['input_state']
        pin=request.POST['pincode']
        gender=request.POST['gender']
        age=request.POST['user_age']
        contact=request.POST['phone_no']
        answers=user_info.objects.filter(email_id=email_address)
        if answers:
            error_message="Email ID already exists. Please provide unique email address"
            return render(request,'registration.html',{'error_message':error_message})
        else:
            newuser=user_info(fname=fname,sname=sname,email_id=email_address,password=pswrd,address=addr,city=city,state=state,pin=pin,gender=gender,age=age,phone=contact)
            newuser.save()
            success_message="User successfully registered! Click here to log in"
            return render(request,'registration.html',{'success_message':success_message})
    else:
        return redirect('/index')

def register_complaint(request):
    if request.method=="POST":
        dept=request.POST['department']
        cat=request.POST['category']
        locn=request.POST['address']
        state=request.POST['inpstate']
        dist=request.POST['district']
        city=request.POST['inp_city']
        date=request.POST['doc']
        descrptn=request.POST['description']
        uname=request.session['username']
        urecord=user_info.objects.get(email_id=uname)
        #uid=urecord.id
        #user_id=uid
        newcomplaint=complaints(department=dept,category=cat,location=locn,state=state,district=dist,city=city,date_of_occurence=date,complaint_desc=descrptn,user_id=urecord)
        newcomplaint.save()
        success_message="Complaint submitted successfully"
        #messages.success(request,"Submitted successfully!!")
        return render(request,'complaint_reg.html',{'sucess_message':success_message})
    else:
        return redirect('/index')


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('/user')

def change_address(request):
    if request.method=="POST":
        username=request.session['username']
        userinfo=user_info.objects.get(email_id=username)
        new_address=request.POST['address']
        userinfo.address=new_address
        userinfo.save()
        return redirect('/userprofile')
    else:
        return redirect('/index')


def change_city(request):
    if request.method=="POST":
        username=request.session['username']
        userinfo=user_info.objects.get(email_id=username)
        new_city=request.POST['inp_city']
        userinfo.city=new_city
        userinfo.save()
        return redirect('/userprofile')
    else:
        return redirect('/index')


def change_state(request):
    if request.method=="POST":
        username=request.session['username']
        userinfo=user_info.objects.get(email_id=username)
        new_state=request.POST['inp_state']
        userinfo.state=new_state
        userinfo.save()
        return redirect('/userprofile')
    else:
        return redirect('/index')



def change_pin(request):
    if request.method=="POST":
        username=request.session['username']
        userinfo=user_info.objects.get(email_id=username)
        new_pin=request.POST['pincode']
        userinfo.pin=new_pin
        userinfo.save()
        return redirect('/userprofile')
    else:
        return redirect('/index')


def change_phone(request):
    if request.method=="POST":
        username=request.session['username']
        userinfo=user_info.objects.get(email_id=username)
        new_phone=request.POST['phoneno']
        userinfo.phone=new_phone
        userinfo.save()
        return redirect('/userprofile')
    else:
        return redirect('/index')


def show_change_password_page(request):
    if request.method=="POST":
        if request.session.has_key('username'):
            return render(request,'change_password_page.html')
        else:
            error_message="User not logged in!! Login here"
            return render(request,'user_login_page.html',{'error_message':error_message})
    else:
        return redirect('/index')


def change_password(request):
    if request.method=="POST":
        if request.session.has_key('username'):
            usrname=request.session['username']
            userrecord=user_info.objects.get(email_id=usrname)
            fetchedpwd=userrecord.password
            oldpwd=request.POST['oldpassword']
            if fetchedpwd==oldpwd:
                newpwd=request.POST['newpassword']
                retypedpwd=request.POST['confirmpassword']
                if newpwd==retypedpwd:
                    userrecord.password=newpwd
                    userrecord.save()
                    return redirect('/userprofile')
                else:
                    error_message="Type password correctly"
                    return render(request,'change_password_page.html',{'error_message':error_message})
            else:
                error_message="Old Password doesn't match"
                return render(request,'change_password_page.html',{'error_message':error_message})
        else:
            error_message="User not logged in!! Login here"
            return render(request,'user_login_page.html',{'error_message':error_message})
    else:
        return redirect('/index')

def delete_user(request):
    if request.method=="POST":
        if request.session.has_key('username'):
            username=request.session['username']
            urecord=user_info.objects.get(email_id=username)
            urecord.delete()
            try:
                del request.session['username']
            except:
                pass
            return redirect('/index')
        else:
            error_message="User not logged in!! Login here"
            return render(request,'user_login_page.html',{'error_message':error_message})


def admin_view_complaints(request):
    if request.session.has_key('admin'):
        all_complaints=complaints.objects.all()
        return render(request,'admin_view_complaints.html',{'every_complaint':all_complaints})
    else:
        error_message="Admin not logged in"
        return render(request,'admin_login_page.html',{'error_message':error_message})


def admin_view_citizen_details(request):
    if request.session.has_key('admin'):
        all_citizens=user_info.objects.all()
        return render(request,'admin_view_citizen_details.html',{'allcitizens':all_citizens})
    else:
        error_message="Admin not logged in"
        return render(request,'admin_login_page.html',{'error_message':error_message})


def process_complaints(request):
    if request.session.has_key('admin'):
        return render(request,'process_complaint.html')
    else:
        errmessage="Admin not logged in"
        return render(request,'admin_login_page.html',{'error_message':errmessage})


def admin_logout_request(request):
    try:
        del request.session['admin']
    except:
        pass
    return redirect('/adminlogin')


def process_complaints_final(request):
    if request.method=="POST":
        if request.session.has_key('admin'):
            if request.POST['comp_id'] and request.POST['user_id']:
                compid=request.POST['comp_id']
                uid=request.POST['user_id']
                complaint_row=complaints.objects.filter(id=compid, user_id=uid)
                if complaint_row:
                    for item in complaint_row:
                        item.status=True
                        item.save()
                    return render(request,'process_complaint.html',{'success_message':"The complaint has been sent for processing"})
                else:
                    return render(request,'process_complaint.html',{'error_message':"Record doesn't exist!! Please enter valid details"})
            else:
                return render(request,'process_complaint.html',{'error_message':"Please enter valid details"})
        else:
            return render(request,'admin_login_page.html',{'error_message':"Admin not logged in"})
    else:
        return redirect('/index')


def show_complaint_deletion_page(request):
    if request.session.has_key('username'):
        return render(request,'complaintdeletion_page.html')
    else:
        return render(request,'user_login_page.html',{'error_message':"User not logged in!! Login here"})


def complaint_deletion(request):
    if request.method=="POST":
        if request.session.has_key('username'):
            username=request.session['username']
            comp_id=request.POST['comp_id']
            comp_record=complaints.objects.filter(id=comp_id)
            if comp_record:
                comp_record.delete()
                return render(request,'complaintdeletion_page.html',{'success_message':"Complaint deleted successfully!!"})
            else:
                return render(request,'complaintdeletion_page.html',{'error_message':"COMPLAINT DOES NOT EXIST!!"})
        else:
            return render(request,'user_login_page.html',{'error_message':"User not logged in. Login HERE"})
    else:
        return redirect('/index')