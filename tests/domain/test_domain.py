from seed.tests.util_test import fill_test_database
from rest_framework.test import APITestCase
from domain.create_process import create_process
from domain.seed_serie import seed_serie


class TestDomain(APITestCase):

    def setUp(self):
        fill_test_database()

    def test_create_process(self):
        output_1 = create_process(7, 2, 1)
        self.assertEqual(output_1, 105)

        output_2 = create_process(10, 3, 1)
        self.assertEqual(output_2, 280)

        output_3 = create_process(50, 1, 1)
        self.assertEqual(output_3, 3041)

        output_4 = create_process(21, 4, 1)
        self.assertEqual(output_4, 2088)

        output_5 = create_process(17, 4, 1)
        self.assertEqual(output_5, 9945)

        output_6 = create_process(41, 5, 1)
        self.assertEqual(output_6, 2638)

    def test_seed_serie(self):
        output_1 = seed_serie(7, 2)
        self.assertEqual(output_1, 105)

        output_2 = seed_serie(10, 3)
        self.assertEqual(output_2, 280)

        output_3 = seed_serie(21, 4)
        self.assertEqual(output_3, 208845)

        output_4 = seed_serie(17, 4)
        self.assertEqual(output_4, 9945)

        output_5 = seed_serie(41, 5)
        self.assertEqual(output_5, 26381811456)

        output_6 = seed_serie(-1, -1)
        self.assertEqual(output_6, None)

        output_7 = seed_serie(0, 5)
        self.assertEqual(output_7, None)