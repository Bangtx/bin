from importlib.resources import path

from django.shortcuts import render
from .models import User
from django.http import HttpResponse


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

    def admin(self, r):
        all_user = User.objects.all()
        return render(
            request=r,
            template_name='form.html',
            context={
                'all_user': all_user
            }
        )

    def edit_user(self, r, id):
        user = User.objects.get(id=id).user
        passw = User.objects.get(id=id).passw
        print(user, passw)
        if r.method == 'POST':
            user_input = r.POST.get('user')
            pass_input = r.POST.get('pass')
            u = User.objects.get(id=id)
            u.user = user_input
            u.passw = pass_input
            u.save()
            return HttpResponse('update ok')
        return render(request=r, template_name='edit.html',
                      context={
                          'user': user,
                          'passw': passw
                      })

    def delete_user(self, r, id):
        u = User.objects.get(id=id)
        if u:
            u.delete()
        all_user = User.objects.all()
        return render(
            request=r,
            template_name='form.html',
            context={
                'all_user': all_user
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