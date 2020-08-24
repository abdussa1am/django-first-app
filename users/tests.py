from django.test import Client, TestCase
# Create your tests here.

class Aert(TestCase):

    def setUp(self):
       c = Client()
       response = c.get("/pessangers/")
       self.assertEqual(response.status_code , 200)
