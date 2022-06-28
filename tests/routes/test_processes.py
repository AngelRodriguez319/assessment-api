from rest_framework import status
from rest_framework.test import APITestCase
from seed.tests.util_test import fill_test_database


class TestProcesses(APITestCase):

    def setUp(self):
        fill_test_database()

    def test_execute(self):
        input_1 = {"N": 7, "K": 2, "user_id": 1}
        response_1 = self.client.get('/api/processes/execute/', input_1)
        output_1 = 105
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_1.data, output_1)

        input_2 = {"N": 10, "K": 3, "user_id": 1}
        response_2 = self.client.get('/api/processes/execute/', input_2)
        output_2 = 280
        self.assertEqual(response_2.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_2.data, output_2)

        input_3 = {"N": 50, "K": 1, "user_id": 1}
        response_3 = self.client.get('/api/processes/execute/', input_3)
        output_3 = 3041
        self.assertEqual(response_3.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_3.data, output_3)

        input_4 = {"N": 21, "K": 4, "user_id": 1}
        response_4 = self.client.get('/api/processes/execute/', input_4)
        output_4 = 2088
        self.assertEqual(response_4.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_4.data, output_4)

        input_5 = {"N": 17, "K": 4, "user_id": 1}
        response_5 = self.client.get('/api/processes/execute/', input_5)
        output_5 = 9945
        self.assertEqual(response_5.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_5.data, output_5)

        input_6 = {"N": 41, "K": 5, "user_id": 1}
        response_6 = self.client.get('/api/processes/execute/', input_6)
        output_6 = 2638
        self.assertEqual(response_6.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_6.data, output_6)

        input_7 = {"N": 41, "K": 5, "user_id": "Admin"}
        response_7 = self.client.get('/api/processes/execute/', input_7)
        self.assertEqual(response_7.status_code, status.HTTP_400_BAD_REQUEST)
