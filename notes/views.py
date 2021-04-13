from django.shortcuts import render
from .models import Notes
from django.http import HttpResponse
# Create your views here.
def home(request):
    notes=Notes.objects.all()
    print(notes)

    return render(request,'notes/index.html',{'notes':notes})

def article(request,id):
    note=Notes.objects.get(id=id)
    return render(request,'notes/article.html',{'note':note})

def upload(request):
    if request.method=="GET":
        return render(request,'notes/upload.html')
    else:
        title=request.POST.get('title')
        paragraph1=request.POST.get('paragraph1')
        paragraph2=request.POST.get('paragraph2')
        paragraph3=request.POST.get('paragraph3')
        paragraph4=request.POST.get('paragraph4')
        paragraph5=request.POST.get('paragraph5')
        paragraph6=request.POST.get('paragraph6')
        paragraph7=request.POST.get('paragraph7')
        paragraph8=request.POST.get('paragraph8')
        paragraph9=request.POST.get('paragraph9')
        paragraph10=request.POST.get('paragraph10')
        note=Notes.objects.create(title=title,paragraph1=paragraph1,paragraph2=paragraph2,paragraph3=paragraph3,paragraph4=paragraph4,paragraph5=paragraph5,paragraph6=paragraph6,paragraph7=paragraph7,paragraph8=paragraph8,paragraph9=paragraph9,paragraph10=paragraph10)
        note.save()
        return HttpResponse("<h1>Upload was successful</h1>")