from django.urls import path
from emailsender.views import EmailFormView, AwaitngMailsView

app_name = 'emailsender'

urlpatterns = [
    path('', EmailFormView.as_view(), name='send-mail'),
    path('mails-list', AwaitngMailsView.as_view(), name='mails-list'),
]
