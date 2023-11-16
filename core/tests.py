from django.urls import reverse
from django.test import TestCase
from core.forms import ContactForm


class ContactViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')

    def test_form_display(self):
        response = self.client.get(reverse('contact'))
        self.assertIsInstance(response.context['form'], ContactForm)
        self.assertContains(response, 'form')

    def test_valid_form_submission(self):
        form_data = {'name': 'Test User', 'email': 'test@example.com', 'content': 'Hello'}
        response = self.client.post(reverse('contact'), form_data)
        self.assertEqual(response.status_code, 302)

    def test_invalid_form_submission(self):
        form_data = {'name': '', 'email': 'invalid-email', 'content': ''}
        response = self.client.post(reverse('contact'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].is_bound)
        self.assertTrue(response.context['form'].is_valid() == False)
