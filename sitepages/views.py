from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render

from .forms import ContactForm, SERVICE_CHOICES


def page_view(request):
    path = request.path
    if path == "/services/":
        return render(request, "services.html")

    if path == "/contact/":
        if request.method == "POST":
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                email = form.cleaned_data["email"]
                phone = form.cleaned_data["phone"]
                services = form.cleaned_data["services"]
                message_text = form.cleaned_data["message"]

                selected_services = (
                    ", ".join(dict(SERVICE_CHOICES)[code] for code in services)
                    if services
                    else "No service selected"
                )

                subject = f"New Carbon Nitrogen Group inquiry from {name}"
                body = (
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone or 'Not provided'}\n"
                    f"Selected service(s): {selected_services}\n\n"
                    f"Message:\n{message_text or 'No message provided.'}\n"
                )
                recipient_list = [
                    "missmakau9@gmail.com",
                ]

                email_message = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=recipient_list,
                    reply_to=[email],
                )
                email_message.send(fail_silently=False)

                messages.success(
                    request,
                    "Thanks for reaching out. Your request has been sent to the team."
                )
                return redirect("/contact/")
        else:
            form = ContactForm()

        return render(request, "sitepages/contact.html", {"form": form})

    if path == "/about/":
        page = "About"
        return render(request, "page.html", {"page": page})

    if path == "/delivery-approach/":
        return render(request, "delivery-approach.html")

    page = "Page"
    return render(request, "page.html", {"page": page})
