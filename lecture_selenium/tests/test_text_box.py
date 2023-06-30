import pytest
from selenium.common import NoSuchElementException

from lecture_selenium.pages.page_text_box import PageTextBox


user_data = {'fullname': 'Vasya Pupkin',
             'email': 'pupkin@1.com',
             'bad_email': 'hsdkhf00',
             'curr_addr': 'My current address',
             'perm_addr': 'My perm address'}


class TestTextBox:

    def test_full_name(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname'))
        page.submit()
        name = page.get_full_name()
        assert name == user_data['fullname']

    def test_email_positive(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_email(user_data.get('email'))
        page.submit()
        email = page.get_email()
        assert email == user_data['email']

    def test_email_negative(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_email(user_data.get('bad_email'))
        page.submit()
        # assert page.get_email_field_attribute("class") == "mr-sm-2 field-error form-control"
        assert "field-error" in page.get_email_field_attribute("class")
        with pytest.raises(NoSuchElementException) as q:
            assert page.get_email() != True

    def test_curr_addr(self, chrome):
        page=PageTextBox(chrome)
        page.open().set_curr_addr(user_data.get('curr_addr'))
        page.submit()
        addr = page.get_curr_addr()
        assert addr == user_data['curr_addr']

    def test_perm_addr(self, chrome):
        page=PageTextBox(chrome)
        page.open().set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        addr2 = page.get_perm_addr()
        assert addr2 == user_data['perm_addr']

    def test_full_form_positive(self, chrome):
        page=PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname')).set_email(user_data.get('email'))\
            .set_curr_addr(user_data.get('curr_addr')).set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        fullname=page.get_full_name()
        mail=page.get_email()
        addr1=page.get_curr_addr()
        addr2=page.get_perm_addr()
        assert fullname == user_data['fullname']
        assert mail == user_data['email']
        assert addr1 == user_data['curr_addr']
        assert addr2 == user_data['perm_addr']

    def test_full_form_negative(self, chrome):
        page=PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname')).set_email(user_data.get('bad_email'))\
            .set_curr_addr(user_data.get('curr_addr')).set_perm_addr(user_data.get('perm_addr'))
        page.submit()
        assert "field-error" in page.get_email_field_attribute("class")
        with pytest.raises(NoSuchElementException) as q:
            fullname=page.get_full_name()
            mail=page.get_email()
            addr1=page.get_curr_addr()
            addr2=page.get_perm_addr()
            assert fullname != user_data['fullname']
            assert mail != user_data['bad_email']
            assert addr1 != user_data['curr_addr']
            assert addr2 != user_data['perm_addr']


