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


    # def test_wrong_url_on_link_field(self):
    #     tool = models.Tool()
    #     tool.title = "TitleToWrongURL"
    #     tool.link = "wrongURL"
    #     tool.description = self.description
    #     tool.tags = self.tags
    #     tool.save()

    #     self.assertRaises(TypeError)
    
    # def test_none_array_on_tags_field(self):
    #     tool = models.Tool()
    #     tool.title = "TitleToWrongTags"
    #     tool.link = self.link
    #     tool.description = self.description
    #     tool.tags = []
    #     tool.save()

    #     self.assertRaises(TypeError)
