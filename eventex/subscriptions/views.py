from django.http.response import HttpResponse
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm


def subscribe(request):
    template = 'subscriptions/subscription_form.html'
    return render(request,
                  template,
        {'form': SubscriptionForm()})