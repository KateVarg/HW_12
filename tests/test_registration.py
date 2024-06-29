from pages.registration_page import RegistrationPage
from data.user import User


def test_send_practice_form():
    page = RegistrationPage()
    user = User(
                'Иван',
                'Иванов',
                'ivanivanov@test.com',
                'Male',
                '8912345678',
                '15',
                'June',
                '1999',
                'English',
                'Reading',
                'images.jpeg',
                'Страна, город, улица, дом, этаж, квартира',
                'NCR',
                'Gurgaon'
                )
    page.open().register(user).check_registered_user(user)
