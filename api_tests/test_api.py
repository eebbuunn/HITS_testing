from lib.repo import *


class TestHttpBaseChecks:
    def test_http_ok_start_page(self):
        assert get_form().status_code == 200

    def test_http_ok_on_result_page(self):
        assert post_form("1, 1, 2").status_code == 200

    def test_http_result_not_empty(self):
        assert post_form("1, 1, 2").text != ''

    def test_http_form_page_not_empty(self):
        assert get_form().text != ''

    def test_http_form_page_content_type(self):
        assert get_form().headers['Content-Type'] == 'text/html; charset=utf-8'

    def test_http_result_page_content_type(self):
        assert post_form('1, 2, 3').headers['Content-Type'] == 'text/plain; charset=utf-8'

    def test_http_404_on_notexist_page(self):
        assert get_page('asdasdasdas').status_code == 404

    def test_http_post_data_with_extra_fields(self):
        data = {
            'data': '1, 2, 3',
            'extra': 'something',
            1: 2
        }
        assert post_data('/result', data=data).status_code == 400

    def test_http_get_with_auth(self):
        headers = {"Authentication": "Bearer ahsduiiagduhauGDYUAGwdyuAGSdyuGAYUwgdLSYdAWDUHUIAWgdYKAGdu"}
        assert get_page('/', headers=headers).status_code == 200


class TestMaxCoins:
    def test_burst_baloons_4_nums(self):
        expected = '167'
        actual = post_form("3, 1, 5, 8").text
        print(actual)
        assert actual == expected

    def test_burst_baloons_1_num(self):
        expected = '3'
        actual = post_form("3").text
        print(actual)
        assert actual == expected

    def test_burst_baloons_2_num(self):
        expected = '10'
        actual = post_form("1, 5").text
        print(actual)
        assert actual == expected


class TestErrorResponses:
    def test_400_with_num_less_0(self):
        assert post_form("-1, 2").status_code == 400

    def test_400_with_num_more_100(self):
        assert post_form("1, 200").status_code == 400

    def test_400_nums_count_more_300(self):
        data = ", ".join(['1' for _ in range(301)])
        assert post_form(data).status_code == 400

    def test_400_nums_count_less_1(self):
        assert post_form(None).status_code == 400

    def test_number_is_char(self):
        assert post_form('a').status_code == 400

    def test_number_is_string(self):
        assert post_form('str').status_code == 400

    def test_number_is_unicode(self):
        assert post_form('℮').status_code == 400

    def test_number_is_ascii(self):
        assert post_form("!@#").status_code == 400

    def test_number_is_emoji(self):
        assert post_form('💀').status_code == 400

    def test_number_is_list(self):
        assert post_form([]).status_code == 400

    def test_form_without_key_data(self):
        data = {123: 345}
        assert post_data('/result', data=data).status_code == 400
