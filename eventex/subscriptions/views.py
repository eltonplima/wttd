from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


def subscribe(request):
    template = 'subscriptions/subscription_form.html'

    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            obj = Subscription(**form.cleaned_data)
            obj.save()

            url = reverse('subscribe', args=(obj.id,))

            return HttpResponseRedirect(url)
        else:
            return render(request,
                          template,
                          {'form': form})
    else:
        return render(request,
                      template,
                      {'form': SubscriptionForm()})