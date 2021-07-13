import unittest
from unittest import TestCase

from dao import *


class TestDao(TestCase):
    def test_conn(self):
        con = conn()
        self.assertIsNotNone(self, con)

    def test_crud(self):
        # save
        wid = db_save_poster('1', 'test', "https://baidu.com", '')
        self.assertIsNotNone(self, wid)
        # update
        db_update_poster(wid, '1', 'test',
                         "https://tse2-mm.cn.bing.net/th/id/OIP-C.JTej4UK2oUlKg0YSzf7pGwHaE9?pid=ImgDet&rs=1", '')
        # query
        p = query_user_poster(wid)
        self.assertIsNotNone(self, p)
        # query all
        posters = query_user_posters()
        self.assertIsNotNone(self, posters)
        # delete
        db_delete_poster(wid)

if __name__ == '__main__':
    unittest.main()
