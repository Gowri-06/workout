from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect 
from django.template import loader
from .models import Members
from django.urls import reverse

 
# Create your views here.
# def index(request):
#     template = loader.get_template('myfirst.html')
#     memberdata = Members.objects.all().values()
#     print(memberdata)
#     context = {"mymembers":memberdata}
#     return HttpResponse(template.render(context,request))


# def add(request):
#     template = loader.get_template('add.html')
#     return HttpResponse(template.render({},request))

# def addrecord(request):
#     a = request.POST["first"]
#     b = request.POST["last"]
#     x = Members(firstname=a, lastname=b)
#     x.save()
#     return HttpResponseRedirect(reverse('index'))

# def delete(request, id):
#   member = Members.objects.get(id=id)
#   member.delete()
#   return HttpResponseRedirect(reverse('index'))

# def update(request, id):
#   mymember = Members.objects.get(id=id)
#   template = loader.get_template('update.html')
#   context = {
#     'mymember': mymember,
#   }
#   return HttpResponse(template.render(context, request))

# def updaterecord(request, id):
#   first = request.POST['first']
#   last = request.POST['last']
#   member = Members.objects.get(id=id)
#   member.firstname = first
#   member.lastname = last
#   member.save()
#   return HttpResponseRedirect(reverse('index'))



class Car:
  name = 'tata'

  def __init__(self,model):
    self.model = model
  def setColor(self, color):
    self.yeah = color
  def getColor(self):
    return self.model
Mycar = Car("suv")
Mycartwo = Car("muv")
Mycar.setColor("pinkk")
print(Mycartwo.getColor())
print(Mycar.name)




