from django.shortcuts import render
from django.views import View
from .forms import RegForm
from .models import RegModel
from django.http import HttpResponse
# Create your views here.
class RegInput(View):
    def get(self,request):
        con_dic={"regform":RegForm()}
        return render(request,'reginput.html',con_dic)
class Reg(View):
    def post(self,request):
        rf=RegForm(request.POST)
        if rf.is_valid():
            r=RegModel(firstname=rf.cleaned_data["firstname"],
                       lastname=rf.cleaned_data["lastname"],
                       username=rf.cleaned_data["username"],
                       password=rf.cleaned_data["password"],
                       cpassword=rf.cleaned_data["cpassword"],
                       emailid=rf.cleaned_data["emailid"],
                       mobileno=rf.cleaned_data["mobileno"])
            r.save()
            return HttpResponse("registation successfull")
