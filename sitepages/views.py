from django.shortcuts import render


def page_view(request):
    path = request.path
    if path == "/":
        page = "Home"
    elif path == "/about/":
        page = "About"
    elif path == "/services/":
        page = "Services"
    else:
        page = "Contact"

    return render(request, "page.html", {"page": page})
