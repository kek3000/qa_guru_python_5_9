from model.registation_page import RegistationPage
from data.users import User


def test_form():
    registation_page = RegistationPage()

    nikita = User(first_name='Nikita', second_name='Alekseev', name='Nikita Alekseev', email='test@test.ru',
                  address='Russia, Reutov', phone_number='7987654321', picture='image.jpg', subjects='Computer Science',
                  city='Panipat', state='Haryana', state_and_city='Haryana Panipat', gender='Male',
                  birthday='18 July,1991', hobbies='Sports, Music')

    registation_page.open()
    registation_page.register(nikita)
    registation_page.assert_student_data(nikita)
    registation_page.final_print()
