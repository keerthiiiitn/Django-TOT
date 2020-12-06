from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hi, This is home page")

def abouts(r):
	return HttpResponse("<h2 style='background-color:green;color:white;padding:3px;margin-left:230px;margin-right;230px'>This is about page</h2>")

def dynamicurl(y, name):
	return HttpResponse("<h2>Hi, Welcome to {}</h2>".format(name))

def msg(request):
	return render(request,'djtot/message.html',{})

def detailsofme(request):
	data = {'Name':'Keerthi','Rollno':221}
	return render(request,'djtot/details.html',{'data':data})

def tables(request):
	data = {'n':2}
	return render(request,'djtot/table.html',{'data':data})

def table(request,n):
	j = ''
	for i in range(1,11):
		j += '{} x {:02} = {:02}'.format(n, i, n*i)+"<br/>"
	# print(j)
	return HttpResponse(j)

def twodynamicparameters(request,name,age):
	# data = {'name':name,'age':age}
	return render(request,'djtot/twoparameters.html',{'n':name,'a':age})

def signuppage(request):
	return render(request,'djtot/signuppage.html',{})

def sample(request):
	return render(request,'djtot/inlineex.html',{})

def loginpage(request):
	return render(request,'djtot/internaltask.html',{})

def registrationpage(request):
	return render(request,'djtot/externaltask.html',{})

def jasex(request):
	return render(request,'djtot/js.html')

def jstask(request):
	return render(request,'djtot/jstask.html')