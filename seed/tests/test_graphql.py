"""
__Seed builder__
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import json

from graphene_django.utils.testing import GraphQLTestCase

from seed.tests.util_test import fill_test_database

class TestGraphql(GraphQLTestCase):
    GRAPHQL_URL = "/graphql"

    def setUp(self):
        fill_test_database()
    
    def test_query_processes(self):
        response_01 = self.query(
            '''
            {
                processes(query: "id=1", orderBy: "id", limit: 1){
                    id
                    n
                    k
                    result
                    user {
                      id
                    }
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["processes"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                processes{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["processes"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                processPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    processes { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["processPagination"]["totalPages"], 1)
            self.assertEqual(res_03["processPagination"]["totalCount"], 1)
            self.assertEqual(res_03["processPagination"]["processes"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                processCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["processCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                processCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["processCount"]["count"], 1)

    def test_query_process(self):
        response = self.query(
            '''
            {
                process(id: 1){
                    id
                    n
                    k
                    result
                    user {
                      id
                    }
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["process"]["id"], 1)
    
    def test_save_process(self):
        response = self.query(
            '''
            mutation {
                saveProcess(
                    user:  1,
                    n: 128,
                    k: 128,
                    result: 128,
                ) {
                    process {
                        id
                        n
                        k
                        result
                        user {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveProcess"]["process"]["id"], 2)
    
    def test_set_process(self):
        response = self.query(
            '''
            mutation {
                setProcess(id:1
                    user:  1,
                    n: 128,
                    k: 128,
                    result: 128,

                ) {
                    process {
                        id
                        n
                        k
                        result
                        user {
                          id
                        }
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setProcess"]["process"]["id"], 1)
    
    def test_delete_process(self):
        response = self.query(
            '''
            mutation {
                deleteProcess(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteProcess"]["id"], 1)

    def test_query_users(self):
        response_01 = self.query(
            '''
            {
                users(query: "id=1", orderBy: "id", limit: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                }
            }
            ''')
        res_01 = json.loads(response_01.content)["data"]
        self.assertResponseNoErrors(response_01)
        with self.subTest():
            self.assertEqual(res_01["users"][0]["id"], 1)

        response_02 = self.query(
            '''
            {
                users{ id }
            }
            ''')
        res_02 = json.loads(response_02.content)["data"]
        self.assertResponseNoErrors(response_02)
        with self.subTest():
            self.assertEqual(res_02["users"][0]["id"], 1)

        response_03 = self.query(
            '''
            {
                userPagination(pageNum: 1, pageSize: 1){
                    pageNum
                    pageSize
                    totalPages
                    totalCount
                    users { id }
                }
            }
            ''')
        res_03 = json.loads(response_03.content)["data"]
        self.assertResponseNoErrors(response_03)
        with self.subTest():
            self.assertEqual(res_03["userPagination"]["totalPages"], 1)
            self.assertEqual(res_03["userPagination"]["totalCount"], 1)
            self.assertEqual(res_03["userPagination"]["users"][0]["id"], 1)

        response_04 = self.query(
            '''
            {
                userCount(query: "id=1"){ count }
            }
            ''')
        res_04 = json.loads(response_04.content)["data"]
        self.assertResponseNoErrors(response_04)
        with self.subTest():
            self.assertEqual(res_04["userCount"]["count"], 1)

        response_05 = self.query(
            '''
            {
                userCount { count }
            }
            ''')
        res_05 = json.loads(response_05.content)["data"]
        self.assertResponseNoErrors(response_05)
        with self.subTest():
            self.assertEqual(res_05["userCount"]["count"], 1)

    def test_query_user(self):
        response = self.query(
            '''
            {
                user(id: 1){
                    id
                    username
                    firstName
                    lastName
                    email
                    isActive
                }
            }
            ''')
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["user"]["id"], 1)
    
    def test_save_user(self):
        response = self.query(
            '''
            mutation {
                saveUser(
                    username: "email@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,
                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["saveUser"]["user"]["id"], 2)
    
    def test_set_user(self):
        response = self.query(
            '''
            mutation {
                setUser(id:1
                    username: "email_1@test.com",
                    firstName: "FirstName",
                    lastName: "LastName",
                    email: "email_1@test.com",
                    password: "pbkdf2_sha256$150000$jMOqkdOUpor5$kU/QofjBsopM+CdCnU2+pROhtnxd5CZc7NhUiXNTMc0=",
                    isActive: true,

                ) {
                    user {
                        id
                        username
                        firstName
                        lastName
                        email
                        isActive
                    }
                }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["setUser"]["user"]["id"], 1)
    
    def test_delete_user(self):
        response = self.query(
            '''
            mutation {
                deleteUser(id:1) { id }
            }
            '''
        )
        res = json.loads(response.content)["data"]
        self.assertResponseNoErrors(response)
        self.assertEqual(res["deleteUser"]["id"], 1)