from model.registation_page import RegistationPage


def test_form():
    registation_page = RegistationPage()

    registation_page.open()
    registation_page.fill_first_name('Nikita')
    registation_page.fill_second_name('Alekseev')
    registation_page.fill_email('test@test.ru')
    registation_page.choose_gender()
    registation_page.fill_phone_number('79999999999')
    registation_page.fill_birthday()
    registation_page.fill_subjects('Computer Science')
    registation_page.choose_hobbies()
    registation_page.upload_picture('image.jpg')
    registation_page.fill_current_address('Russia, Reutov')
    registation_page.choose_state_and_city('Haryana', 'Panipat')
    registation_page.press_button_submit()
    registation_page.assert_student_data('Student Name Nikita Alekseev', 'Student Email test@test.ru', 'Gender Male',
                                         'Mobile 7999999999',
                                         'Date of Birth 18 July,1991', 'Subjects Computer Science',
                                         'Hobbies Sports, Music',
                                         'Picture image.jpg', 'Address Russia, Reutov',
                                         'State and City Haryana Panipat')
    registation_page.final_print()
