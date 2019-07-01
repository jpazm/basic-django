from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    # return HttpResponse("<h1>Hello spartan</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_age": 29
    }
    return render(request, "about.html", my_context)