from selene.support.shared import browser
from selene import have
import os


class RegistationPage():

    def open(self):
        browser.config.window_width = 1024
        browser.config.window_height = 768
        browser.config.base_url = 'https://demoqa.com'
        browser.open('/automation-practice-form')

    def register(self, student):
        browser.element('#firstName').type(student.first_name)
        browser.element('#lastName').type(student.second_name)
        browser.element('#userEmail').type(student.email)
        browser.element('input[value=' + student.gender + ']').double_click()
        browser.element('#userNumber').type(student.phone_number)
        browser.element('#dateOfBirthInput').press()
        browser.element('.react-datepicker__month-select').click()
        browser.element('option[value="6"]').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('option[value="1991"]').click()
        browser.element('div[aria-label="Choose Thursday, July 18th, 1991"]').click()
        browser.element('#subjectsInput').type(student.subjects).press_enter()
        browser.element('label[for="hobbies-checkbox-1"]').click()
        browser.element('label[for="hobbies-checkbox-3"]').click()
        browser.element('#currentAddress').type(student.address)
        browser.element('#state').click()
        browser.element('#react-select-3-input').set_value(student.state).press_tab()
        browser.element('#city').click()
        browser.element('#react-select-4-input').set_value(student.city).press_tab()
        browser.element('#submit').press_enter()
        return browser.element('#uploadPicture').send_keys(os.getcwd() + f"\\{student.picture}")

    def assert_student_data(self, student):
        browser.all('tbody tr').should(
            have.exact_texts('Student Name ' + student.name, 'Student Email ' + student.email,
                             'Gender ' + student.gender,
                             'Mobile ' + student.phone_number, 'Date of Birth ' + student.birthday,
                             'Subjects ' + student.subjects,
                             'Hobbies ' + student.hobbies, 'Picture ' + student.picture,
                             'Address ' + student.address, 'State and City ' + student.state_and_city
                             ))

    def final_print(self):
        print('\nФорма полностью заполнена, отправлена и проверена. Тест пройден успешно.')
