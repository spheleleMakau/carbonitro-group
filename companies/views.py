from django.views.generic import TemplateView


class CompaniesListView(TemplateView):
    template_name = "companies/list.html"


class PotificDetailView(TemplateView):
    template_name = "companies/potific.html"
