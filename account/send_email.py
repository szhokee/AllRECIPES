from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'AllRECIPES',
        f'http://localhost:8000/account/activate/{code}/', #body
        'szhokee@gmail.com', #from
        [email]   # to
    )