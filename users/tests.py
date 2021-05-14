from django.test import TestCase
from django.test import Client


class AdminTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_load_properly(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)
        print('application load properly')

    def test_user_admin(self):
        response = self.client.post('/api/users/register-admin/', {
            'username': "admin",
            'password': "admin",
            'first_name': "arman",
            'last_name': "sabagh"
        })
        self.assertEqual(response.status_code, 201)
        print('admin user create successfully')

        response = self.client.login(username='admin', password='admin')
        self.assertTrue(response)
        print('admin user login successfully')
