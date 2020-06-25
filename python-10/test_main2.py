import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()
from django.test import TestCase


class TestChallenge10(TestCase):
    def test_0(self):
        response = self.client.post('/lambda/', {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
                                    content_type='application/json')
        assert isinstance(response.data, dict)
        self.assertEqual(response.status_code, 200)

    def test_01(self):
        response = self.client.post('/lambda/', {"question": [2, 3, 2, 4, 5, 12, 2, 3]},
                                    content_type='application/json')
        assert len(response.data['solution']) == 8
        self.assertEqual(response.status_code, 200)
    
    def test_02(self):
        response = self.client.post('/lambda/', {"question": [2, 2, 2, 1, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [2, 2, 2, 4 , 1]
        self.assertEqual(response.status_code, 200)
    
    def test_05(self):
        response = self.client.post('/lambda/', {"question": [2, 2, 2, 4, 1]},
                                    content_type='application/json')
        assert response.data['solution'] == [2, 2, 2, 4, 1]
        self.assertEqual(response.status_code, 200)

    def test_03(self):
        response = self.client.post('/lambda/', {"question": [6, 6, 6, 6, 6, 6, 2, 2, 2, 1, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [6, 6, 6, 6, 6, 6, 2, 2, 2, 4,1]
        self.assertEqual(response.status_code, 200)

    def test_04(self):
        response = self.client.post('/lambda/', {"question": []},
                                    content_type='application/json')
        assert response.data['solution'] == []
        self.assertEqual(response.status_code,200)

    def test_06(self):
        response = self.client.post('/lambda/', {"question": []},
                                    content_type='application/json')
        assert response.data['solution'] == []
        self.assertEqual(response.status_code,200)

    def test_07(self):
        response = self.client.post('/lambda/', {"question": [3, 3, 3, 3, 2, 2, 2, 12, 12, 5, 5, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [3, 3, 3, 3, 2, 2, 2, 12, 12, 5, 5, 4]
        self.assertEqual(response.status_code,200)
    
    def test_08(self):
        response = self.client.post('/lambda/', {"question": [3, 3, 3, 3, 2, 2, 2, 12, 12, 5, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [3, 3, 3, 3, 2, 2, 2, 12, 12, 5, 4]
        self.assertEqual(response.status_code,200)


    def test_09(self):
        response = self.client.post('/lambda/', {"question": [2, 2, 2, 3, 3, 12, 5, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [2, 2, 2, 3, 3, 12, 5, 4]
        self.assertEqual(response.status_code,200)
    

    def test_10(self):
        response = self.client.post('/lambda/', {"question": [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]},
                                    content_type='application/json')
        assert response.data['solution'] == [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]
        self.assertEqual(response.status_code,200)

    def test_10(self):
        response = self.client.post('/lambda/', {"question": [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]},
                                    content_type='application/json')
        assert response.data['solution'] == [3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5]
        self.assertEqual(response.status_code,200)

    def test_10(self):
        response = self.client.post('/lambda/', {"question": [2, 2, 2, 3, 3, 4, 5, 12]},
                                    content_type='application/json')
        assert response.data['solution'] == [2, 2, 2, 3, 3, 4, 5, 12]
        self.assertEqual(response.status_code,200)