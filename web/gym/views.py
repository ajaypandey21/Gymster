from django.shortcuts import render, redirect
from gym import models
from django.contrib import messages

# Create your views here.
from gym.models import GymMem

from gym.models import Trainer


def index(request):
    return render(request, "index.html")


def classy(request):
    return render(request, "class.html")


def contact(request):
    return render(request, "contact.html")


def detail(request):
    return render(request, "detail.html")


def update(request):
    return render(request, "update.html")


def team(request):
    return render(request, "team.html")


def mdash(request):
    if 'muser' in request.session:
        current_user = request.session['muser']
        mem = GymMem.objects.get(username=current_user)
        param = {'curr_user': current_user}

        return render(request, 'mdash.html', {'curr_user': current_user, "ajay": mem})
    else:
        redirect('memlog')
    return render(request, "mdash.html")


def about(request):
    return render(request, "about.html")


def adminlog(request):
    if 'user' in request.session:
        return redirect('dash')

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.Admin.objects.filter(username=username, password=password)
        if user_obj:
            request.session['user'] = username
            return redirect('dash')

        login_error = "Wrong Username and Password"
        messages.info(request, "Invalid Username and Password ")

    return render(request, "adlog.html")


def memlog(request):
    if 'muser' in request.session:
        return redirect('mdash')

    elif request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = models.GymMem.objects.filter(username=username, password=password)
        if user_obj:
            request.session['muser'] = username
            return redirect('mdash')

        login_error = "Wrong Username and Password"
        messages.info(request, "Invalid Username and Password ")

    return render(request, "memlog.html", locals())


def mlogout(request):
    try:
        del request.session['muser']

    except:

        return redirect('memlog')

    return redirect('memlog')

def tlogout(request):
    try:
        del request.session['tuser']

    except:

        return redirect('tlog')

    return redirect('tlog')



def memreg(request):
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        program = request.POST.get("program")

        user_list = models.GymMem.objects.filter(username=username)

        if user_list:
            error_exist = "User already Exist,Please Enter different"
            return render(request, "memreg.html", {"error_reg": error_exist})

        else:
            user_data = models.GymMem.objects.create(username=username, first_name=first_name, email=email,
                                                     password=password, last_name=last_name, phone=phone,
                                                     program=program)
            user_data.save()
            return redirect("memlog")

    return render(request, "memreg.html")


def dashboard(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'curr_user': current_user}
        trainer = Trainer.objects.all()
        members = GymMem.objects.all()
        return render(request, 'dashboard.html', {"curr_user": current_user, "ajay": members, "ajay2": trainer})
    else:
        redirect('adminlog')
    return render(request, "adminlog.html")


def logout(request):
    try:
        del request.session['user']

    except:

        return redirect('adminlog')

    return redirect('adminlog')


def update(request, id):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")
        image = request.POST.get("image")

        employees = GymMem.objects.get(id=id)

        employees.phone = phone
        employees.first_name = first_name
        employees.last_name = last_name
        employees.email = email
        employees.password = password
        employees.image = image

        employees.save()
        return redirect("/mdash")
    return render(request, 'mdash.html', {"ajay": employees})

    # form = EmpForm(request.POST, instance=employees)
    # if form.is_valid():
    #     form.save()
    #     return redirect("/mdash")


def edit(request, id):
    employees = GymMem.objects.get(id=id)
    return render(request, 'edit.html', {'employees': employees})


def destroy(id):
    employees = GymMem.objects.get(id=id)
    employees.delete()
    return redirect('dash')


def tlog(request):
    if 'tuser' in request.session:
        return redirect('tdash')

    elif request.method == "POST":
        tid = request.POST.get("t_id")
        password = request.POST.get("password")
        train_obj = models.Trainer.objects.filter(t_id=tid, password=password)

        if train_obj:
            request.session['tuser'] = tid
            return redirect('tdash')

        login_error = "Wrong Username and Password"
        messages.info(request, "Invalid Username and Password ")
    return render(request, 'tlog.html',locals())


def tdash(request):
    if 'tuser' in request.session:
        current_user = request.session['tuser']
        mem = Trainer.objects.get(t_id=current_user)

        return render(request, 'tdash.html',{"curr_user":current_user,"ajay2":mem})


def treg(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'curr_user': current_user}
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            tid = request.POST.get("t_id")
            password = request.POST.get("password")

            user_list = models.Trainer.objects.filter(t_id = tid)

            if user_list:
                error_exist = "User already Exist,Please Enter different"
                return render(request, "treg.html", {"error_reg": error_exist})

            else:
                user_data = models.Trainer.objects.create(t_id=tid, first_name=first_name,
                                                         password=password, last_name=last_name,
                                                        )
                user_data.save()
                return redirect("dash")

        return render(request, 'treg.html', {"curr_user": current_user, })
    else:
        redirect('adminlog')

    return render(request, 'treg.html')


def memreg2(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'curr_user': current_user}
        if request.method == "POST":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            phone = request.POST.get("phone")
            program = request.POST.get("program")

            user_list = models.GymMem.objects.filter(username=username)

            if user_list:
                error_exist = "User already Exist,Please Enter different"
                return render(request, "memreg2.html", {"error_reg": error_exist})

            else:
                user_data = models.GymMem.objects.create(username=username, first_name=first_name, email=email,
                                                         password=password, last_name=last_name, phone=phone,
                                                         program=program)
                user_data.save()
                return redirect("dash")

        return render(request, 'memreg2.html', {"curr_user": current_user, })
    else:
        redirect('adminlog')
    return render(request, 'memreg2.html')


'''def register(request): ## Validation Django
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_list = models.GymMem.objects.filter(username=username)

        if user_list:
            error_exist = "User already Exist,Please Enter diferent"
            return render(request, "register.html", {"error_reg": error_exist})

        else:

            form = EmpForm(request.POST)
            val_error = "please enter data"
            if form.is_valid():
                user_data = models.GymMem.objects.create(username=username, first_name=first_name, email=email,
                                                         password=password, last_name=last_name)
                user_data.save()
                return redirect("login")
            else:
                return render(request, "register.html",{"error":val_error})

        # return redirect('login')

    return render(request, "register.html")'''

'''
def adminreg(request):
    if request.method == 'POST':

        name = request.POST.get("name")

        username = request.POST.get("username")

        password = request.POST.get("password")

        user_list = models.GymMem.objects.filter(username=username)

        if user_list:
            error_exist = "User already Exist,Please Enter different"
            return render(request, "AdminReg.html", {"error_reg": error_exist})

        else:
            user_data = models.Admin.objects.create(username=username, name=name,
                                                    password=password)
            user_data.save()
            return redirect("adminlog")

    return render(request, "AdminReg.html")'''
