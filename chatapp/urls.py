from django.urls import path
from . import views


urlpatterns = [
	path("", views.AddSessionView.as_view(), name="create_session"),
	path("list/", views.ListSessionView.as_view(), name="list_session"),
	path("get_chat/", views.GetChatView, name="get_chat"),
	path("chat/<int:pk>/<str:user>", views.ChatView, name="chat"),
	path("recieve_message/<int:pk>/", views.RecieveMessage, name="recieve_message"),
	path("json/<int:pk>/", views.JSONsender, name="json_sender"),
]