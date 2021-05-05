from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .models import Session
import json


# Create your views here.

class AddSessionView(CreateView):
    model = Session
    template_name = "startchat.html"
    fields = "__all__"
    success_url = reverse_lazy("create_session")


class ListSessionView(ListView):
    model = Session
    template_name = "list.html"
    fields = "__all__"
    success_url = reverse_lazy("list_session")


def GetChatView(request):
    if request.method == "POST":
        username = request.POST["username"]
        chats = Session.objects.filter(starting_user=username)
        print(chats)

        return render(request, "get_chats.html", {"chats": chats, })


def ChatView(request, pk, user):
    chat = Session.objects.filter(pk=pk)[0]
    if user == "sender":
        pass
    elif user == "reicever":
        chat.starting_user, chat.ending_user = chat.ending_user, chat.starting_user
    else:
        return HttpResponse("404 error. Page does not exist")
    return render(request, "chat.html", {"chat": chat})


def RecieveMessage(request, pk):
    chat = Session.objects.filter(pk=pk)[0]

    if request.method == "POST":
        coming_message_dic = json.loads(request.body)
        chat.messages[chat.count_message] = coming_message_dic
        chat.count_message += 1
        # gelen mesajı json a ekleme

        chat.save()

    return HttpResponseRedirect(reverse('chat', args=[str(pk), str(user)]))


def JSONsender(request, pk):
    chat = Session.objects.filter(pk=pk)[0]
    print(chat.messages, "json")
    print(chat.messages)
    # return HttpResponse(json.dumps(chat.messages), content_type="application/json")
    return JsonResponse(chat.messages, safe=False, json_dumps_params={'ensure_ascii': False})
    # param kısmı utf8 için
