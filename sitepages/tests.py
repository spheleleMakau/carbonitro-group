from django.test import SimpleTestCase

from .forms import ContactForm


class ContactFormTests(SimpleTestCase):
    def test_phone_number_must_be_international_format(self):
        form = ContactForm(
            data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "123",
                "services": [],
                "message": "Need help with a project.",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)

    def test_message_is_required_when_no_service_is_selected(self):
        form = ContactForm(
            data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "+27 72 350 5208",
                "services": [],
                "message": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_form_is_valid_with_international_phone_and_message(self):
        form = ContactForm(
            data={
                "name": "Jane Doe",
                "email": "jane@example.com",
                "phone": "+44 20 7946 0958",
                "services": [],
                "message": "Need help with a project.",
            }
        )

        self.assertTrue(form.is_valid())
