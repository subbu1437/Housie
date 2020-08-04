from django.shortcuts import render


def ShowChatHome(request):
    return render(request,"chat_home.html")

def ShowChatPage(request,person_name):
    return render(request,"chat_screen.html",{'person_name':person_name})
    #return HttpResponse("Chat page "+room_name+""+person_name)