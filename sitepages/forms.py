from django import forms

SERVICE_CHOICES = [
    ("renewable_energy", "Renewable Energy"),
    ("geology_services", "Geology Services"),
    ("mining_services", "Mining Services"),
    ("engineering_services", "Engineering Services"),
    ("strategy_consulting", "Strategy Consulting"),
    ("digital_transformation", "Digital Transformation"),
    ("business_transformation", "Business Transformation"),
    ("change_management", "Change Management"),
]


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        label="Full name",
        widget=forms.TextInput(attrs={
            "placeholder": "Your full name",
            "class": "form-input",
        }),
    )
    email = forms.EmailField(
        label="Email address",
        widget=forms.EmailInput(attrs={
            "placeholder": "you@example.com",
            "class": "form-input",
        }),
    )
    phone = forms.CharField(
        max_length=40,
        required=False,
        label="Phone number",
        widget=forms.TextInput(attrs={
            "placeholder": "+27 72 350 5208",
            "class": "form-input",
        }),
    )
    services = forms.MultipleChoiceField(
        required=False,
        choices=SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="Services of interest",
    )
    message = forms.CharField(
        required=False,
        label="What do you need?",
        widget=forms.Textarea(attrs={
            "placeholder": "Describe what you need and how we can help.",
            "class": "form-textarea",
            "rows": 6,
        }),
    )

    def clean(self):
        cleaned_data = super().clean()
        services = cleaned_data.get("services")
        message = cleaned_data.get("message")

        if not services and not message:
            raise forms.ValidationError(
                "Please select at least one service or tell us what you need in the message."
            )

        return cleaned_data
