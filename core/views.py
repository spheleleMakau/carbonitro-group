from django.views.generic import TemplateView


class GenericPageView(TemplateView):
    template_name = "generic_page.html"
