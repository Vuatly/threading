from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from emailsender.forms import SendEmailForm
from emailsender.models import Email


class EmailFormView(CreateView):
    model = Email
    form_class = SendEmailForm
    template_name = 'send_emails.html'
    success_url = reverse_lazy('emailsender:send-mail')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super(EmailFormView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/admin')



class AwaitngMailsView(ListView):
    model = Email
    template_name = 'mails-list.html'
    context_object_name = 'mails'
    paginate_by = 20

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AwaitngMailsView, self).get_context_data()
        context['sended'] = Email.objects.filter(seconds=0)
        context['awaitng'] = Email.objects.filter(seconds__gt=0)
        return context
