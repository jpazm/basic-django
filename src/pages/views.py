from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello spartan</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contacts page</h1>")