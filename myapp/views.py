from builtins import set
from select import select
from smtpd import usage

from django.shortcuts import render
from .models import User

# Create your views here.
from setuptools.command.register import register


class Index:

    def __init__(self):
        self.is_login = True

    def login_register(self, request):
        login = False
        register = False
        list_user = self.check_login()
        if request.method == 'POST':
            user = request.POST.get('Name')
            passw = request.POST.get('Password')

            for i in list_user:
                if user == i.user and passw == i.passw:
                    login = True

            register = True if request.POST.get('register') else False
            self.registerDB(user, passw)
        return render(
            request=request,
            template_name='index.html',
            context={
                'is_login': login,
                'is_register': register
            }
        )


    @classmethod
    def registerDB(cls, u, p):
        user = User(user=u, passw=p)
        user.save()

    @classmethod
    def check_login(cls):
        user = User.objects.all()
        return list(user)