from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


template = 'subscriptions/subscription_form.html'

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def new(request):
    form = SubscriptionForm()
    data = {'form': form}

    return render(request,
                  template,
                  data)

def create(request):
    form = SubscriptionForm(request.POST)
    if not form.is_valid():
        data = {'form': form}
        return render(request,
                      template,
                      data)

    obj = form.save()
    url = reverse('detail', args=(obj.id,))

    return HttpResponseRedirect(url)

def detail(request, pk):
    template = 'subscriptions/subscription_detail.html'
    subscription = get_object_or_404(Subscription, pk=pk)
    data = {'subscription': subscription}

    return render(request,
                  template,
                  data)
