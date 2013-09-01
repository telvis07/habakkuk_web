from django.test import TestCase
from api.models import KmeansCluster
from datetime import date, datetime
from django.test.client import Client
import json

class QueryTest(TestCase):
    def setUp(self):
        cluster = KmeansCluster()
        cluster.date = date.today()
        cluster.data = json.dumps(cluster_data())
        cluster.save()
        # TODO: init or mock elasticsearch

    def tearDown(self):
        KmeansCluster.objects.all().delete()
        
    def test_no_date(self):
        client = Client()
        response = client.get("/api/query/")
        self.assertEquals(200, response.status_code)
        try:
            res = json.loads(response.content)
            self.assertFalse(res.get('trace'),res.get('trace'))
        except:
            self.fail("Failed to parse reponse from /api/query/")

        self.assertEquals(cluster_data(),res['clusters'])

    def test_with_date(self):
        client = Client()
        response = client.get("/api/query/%s"%datetime.today().strftime("%Y%m%d"))
        self.assertEquals(200, response.status_code)
        try:
            res = json.loads(response.content)
            self.assertFalse(res.get('trace'),res.get('trace'))
        except:
            self.fail("Failed to parse reponse from /api/query/")

        self.assertEquals(cluster_data(),res['clusters'])

def cluster_data():
    return  \
        {
          "name": "root", 
          "children": [
            {
              "size": 2, 
              "name": "john 3:16", 
              "bibleverses":[{"verse":'john 3:16', "weight":1.0},
                             {"verse":'galatians 1:1', "weight":0.001}],
              "children": [
                {
                  "name": "user1 ", 
                  "children": []
                }, 
                {
                  "name": "user2", 
                  "children": []
                }, 
              ]
            },
            {
              "size": 2, 
              "name": "genesis 2:24", 
              "bibleverses":[{"verse":'genesis 2:24', "weight":1.0},
                             {"verse":'habakkuk 1:1', "weight":0.001}],
              "children": [
                {
                  "name": "user3 ", 
                  "children": []
                }, 
                {
                  "name": "user4", 
                  "children": []
                }, 
              ]      
            },
          ]
        }
