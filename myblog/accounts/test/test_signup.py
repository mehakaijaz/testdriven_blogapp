from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from ..forms import UserRegistrationForm
from django.contrib.auth import get_user_model
# Create your tests here.
class AccountCreationTest(TestCase):

    def setUp(self):
        self.form_class=UserRegistrationForm

    def test_signup_page_exists(self):
        response=self.client.get(reverse('signup_page'))
        self.assertEqual(response.status_code,HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response,'Create your account.')

    def test_signup_form_works_correct(self):
        

        #self.assertTrue(issubclass(UserRegistrationForm,UserCreationForm))
        self.assertTrue(issubclass(self.form_class,UserCreationForm))#upar wli line ko ese bhi likh skte h
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data={
            'email':'mehak@gmail.com',
            'username':'testuser',
            'password1':'azmi1234',
            'password2':'azmi1234'
        }
        
        form=self.form_class(sample_data)

        self.assertTrue(form.is_valid())

    def test_signup_form_creates_user_in_db(self):
        user={
            'email':'mehak@gmail.com',
            'username':'testuser1',
            'password1':'azmi1234',
            'password2':'azmi1234'
        }

        form=self.form_class(user)
        User=get_user_model()

        if form.is_valid():
            form.save()

        self.assertEqual(User.objects.count(),1)    