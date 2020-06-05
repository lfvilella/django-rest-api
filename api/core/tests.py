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
        self.new_data = {
            'title': "GitHub",
            'link': "https://github.com",
            'description': "Some description here",
            'tags': ["git", "tag1"],
        }

    def test_CREATE_GET_PUT_PATCH_DELETE(self):
        # CREATE
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

        # GET - tool by ID
        request = self.client.get(self.url+'1/')
        self.assertEqual(request.status_code, 200)

        # PUT
        response = self.client.put(self.url+'1/', self.new_data, format='json')
        # Line below, I update the variable to get the right Tool
        tool_from_db = models.Tool.objects.all().first()

        self.new_data['id'] = tool_from_db.id
        self.assertEqual(self.new_data, response.data)

        self.assertEqual(self.new_data['id'], tool_from_db.id)
        self.assertEqual(self.new_data['title'], tool_from_db.title)
        self.assertEqual(self.new_data['link'], tool_from_db.link)
        self.assertEqual(self.new_data['description'],
                         tool_from_db.description)
        self.assertEqual(self.new_data['tags'], tool_from_db.tags)

        # PATCH
        new_title = "New Title With Patch Verb"
        response = self.client.patch(self.url+'1/',
                                     {'title': new_title},
                                     format='json')
        tool_from_db = models.Tool.objects.all().first()
        self.assertEqual(new_title, tool_from_db.title)

        # DELETE
        response = self.client.delete(self.url+'1/')
        self.assertEqual(response.status_code, 204)

    def test_create_with_wrong_and_none_title(self):
        self.data['title'] = 123321
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)
        
        self.data['title'] = ""
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)
    
    def test_create_with_wrong_and_none_link(self):
        self.data['link'] = "wrongURL"
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)

        self.data['link'] = ""
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)
    
    def test_create_with_wrong_and_none_description(self):
        self.data['description'] = 123321
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)

        self.data['description'] = ""
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)

    def test_create_with_wrong_and_none_tags(self):
        self.data['tags'] = {'tag1': 'value1'}
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)

        self.data['tags'] = ""
        self.client.post(self.url, self.data, format='json')
        self.assertRaises(TypeError)

    def test_filters(self):
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, 201)

        # TITLE
        request = self.client.get(self.url+'?title=Notion')
        self.assertEqual(request.status_code, 200)
        self.assertEqual('Notion', request.data[0]['title'])

        bad_request = self.client.get(self.url+'?title=NoOne')
        self.assertEqual(bad_request.status_code, 404)
        
        # LINK
        request = self.client.get(self.url+'?link=https://notion.so')
        self.assertEqual(request.status_code, 200)
        self.assertEqual('https://notion.so', request.data[0]['link'])

        bad_request = self.client.get(self.url+'?link=https://bossabox.com')
        self.assertEqual(bad_request.status_code, 404)

        # TAGS
        request = self.client.get(self.url+'?tags=calendar')
        self.assertEqual(request.status_code, 200)
        self.assertTrue('calendar' in request.data[0]['tags'])

        bad_request = self.client.get(self.url+'?tags=NoTAGS')
        self.assertEqual(bad_request.status_code, 404)

        # Get wrong tags return 404
        request = self.client.get(self.url+'?tags=calendar&tags=git')
        self.assertEqual(request.status_code, 404)

    def test_invalid_url(self):
        request = self.client.get('/tool/')
        self.assertEqual(request.status_code, 404)
    
    def test_invalid_id(self):
        request = self.client.get(self.url+'idInvalid/')
        self.assertEqual(request.status_code, 404)
    