from django.urls import reverse
from rest_framework.test import APITestCase
from . import models


class TestToolAPI(APITestCase):
    def setUp(self):
        self.url = '/tools/'
        self.data = {
            'title': "Notion",
            'link': "https://notion.so",
            'description': (
                "All in one tool to organize teams and ideas. "
                "Write, plan, collaborate, and get organized."
            ),
            'tags': [
                "organization",
                "planning",
                "collaboration",
                "writing",
                "calendar",
            ],
        }
        
    def test_create(self):
        self.assertEqual(models.Tool.objects.count(), 0)
        response = self.client.post(self.url, self.data, format='json')

        self.assertEqual(response.status_code, 201)

        self.assertEqual(models.Tool.objects.count(), 1)
        tool_from_db = models.Tool.objects.all().first()

        # reponse should return the request data + id
        self.data['id'] = tool_from_db.id
        self.assertEqual(self.data, response.data)

        self.assertEqual(self.data['id'], tool_from_db.id)
        self.assertEqual(self.data['title'], tool_from_db.title)
        self.assertEqual(self.data['link'], tool_from_db.link)
        self.assertEqual(self.data['description'], tool_from_db.description)
        self.assertEqual(self.data['tags'], tool_from_db.tags)

    def test_wrong_link(self):
        self.data['link'] = "wrongURL"
        response = self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)
    
    def test_none_tags(self):
        self.data['tags'] = ""
        response = self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)
    
    def test_update(self):
        # Creating Again
        self.assertEqual(models.Tool.objects.count(), 0)
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(models.Tool.objects.count(), 1)
        
        breakpoint()
        # Changing with PUT verb
        new_data = {
            'title' : "GitHub",
            'link' : "https://github.com",
            'description' : "Some description here",
            'tags' : ["git", "tag1"],
        }
        request = self.client.put(self.url+'1/', new_data)

        tool_from_db = models.Tool.objects.all().first()

        new_data['id'] = tool_from_db.id
        self.assertEqual(new_data, request.data)

        self.assertEqual(new_data['id'], tool_from_db.id)
        self.assertEqual(new_data['title'], tool_from_db.title)
        self.assertEqual(new_data['link'], tool_from_db.link)
        self.assertEqual(new_data['description'], tool_from_db.description)
        self.assertEqual(new_data['tags'], tool_from_db.tags)
