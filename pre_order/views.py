from django.shortcuts import render
from .forms import SubscriberForm


def pre_order(request):

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # print(request.POST)
        # print(form.cleaned_data)
        # print(form.cleaned_data["name"])

        new_record = form.save()

    return render(request, 'pre_order/pre_order.html', locals())
