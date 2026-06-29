from django.shortcuts import render


def page_view(request):
    path = request.path
    if path == "/":
        page = "Home"
    elif path == "/about/":
        page = "About"
    elif path == "/services/":
        page = "Services"
    elif path == "/contact/":
        page = "Contact"
    else:
        page = "Page"

    return render(request, "page.html", {"page": page})
