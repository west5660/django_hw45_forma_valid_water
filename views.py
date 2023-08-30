from django.shortcuts import render
from django.shortcuts import redirect


# Create your views here.
def index(req):
    return render(req,'index.html')
from .formsss import *
def def1(req):
    print(1)
    if req.method=='POST':
        print(2)
        anketa=UserformComment(req.POST)
        if anketa.is_valid():
            print(3)
            k1=anketa.cleaned_data.get('name')
            k2=anketa.cleaned_data['email']
            k3=anketa.cleaned_data['com']
            print(k1,k2,k3)
        else:
            print('erorr')

    else:
        anketa=UserformComment()
    data={'form':anketa}
    return render(req,'forform.html', context=data)

def def2(req):
    print(1)
    if req.POST:
        print(2)
        anketa = UserformErrors(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['num']
            k3 = anketa.cleaned_data['agree']
            return redirect('home')
        else:
            print('ne ok')
            print(anketa.errors)
    else:
        anketa=UserformErrors()
    data={'form':anketa}
    return render(req,'forform.html', context=data)

def def3(req):
    print(1)
    if req.POST:
        print(2)
        anketa = UserformValidator(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['code']
            k3 = anketa.cleaned_data['tel']
            return redirect('home')
        else:
            print('ne ok1')
            print(anketa.errors)
    else:
        anketa = UserformValidator()
    data = {'form': anketa}
    return render(req, 'forform.html', context=data)

def def4(req):
    print(1)
    if req.POST:
        print(2)
        anketa = UserformWater(req.POST)
        if anketa.is_valid():
            print('ok')
            k1 = anketa.cleaned_data.get('name')
            k2 = anketa.cleaned_data['sname']
            k3 = anketa.cleaned_data['email']
            k4 = anketa.cleaned_data['tel']
            k5 = anketa.cleaned_data['adres']
            k6 = anketa.cleaned_data['dost']
            k7 = anketa.cleaned_data['litr']

            # return redirect('home')
            data = {'k1': k1, 'k2': k2, 'k3': k3, 'k4': k4, 'k5': k5, 'k6': k6, 'k7': k7}
            return render(req, 'finalpage2.html', context=data)
        else:
            print('ne ok1')
            print(anketa.errors)
    else:
        anketa = UserformWater()
    data = {'form': anketa}
    return render(req, 'finalpage.html', context=data)
    pass