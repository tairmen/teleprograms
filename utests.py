import unittest
import resp
import req
from unittest.mock import patch


class TestResp(unittest.TestCase):
    def test_find_all(self):
        self.assertEqual(resp.find_all(
            {'12:00': 'Сериал "Викинги"'}, '13:00', '15:00'), {})
        self.assertEqual(resp.find_all(
            {'10:00': 'a'}, '00:00', '20:00'), {'10:00': 'a'})

    def test_get_ser(self):
        self.assertEqual(resp.get_ser({'12:00': 'Сериал A'}), {
                         '12:00': 'Сериал A'})
        self.assertEqual(resp.get_ser({'12:00': 'Фильм A'}), {})

    def test_get_xml(self):
        self.assertEqual(resp.get_xml('Понедельник', '12:00', '12:01'), [])
        self.assertEqual(resp.get_xml('Mon', '12:00', '15:00'), 'Error')

    def test_make_xml(self):
        self.assertEqual(resp.make_xml('error'), 'Error')


class TestReq(unittest.TestCase):
    def test_tvprog_request(self):
        with patch('req.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            mocked_get.return_value.ok = False

    def test_tv_prog(self):
        self.assertEqual(req.tv_prog('something'), 'Error')


if __name__ == '__main__':
    unittest.main()
