import json
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from mainapp.models import News


# class HelloWorldView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Hello world!")
#
# # def hello_world(request):
# #     return HttpResponse("Hello world!")
#
# def blog(request, **kwargs):
#     return HttpResponse(f'{kwargs}')


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'address': 'территория Петропавловская крепость, 3Ж',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'address': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'address': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data


class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'


class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # with open(settings.BASE_DIR / 'news.json', encoding="utf-8") as news_file:
        #     context_data['object_list'] = json.load(news_file)

        context_data['object_list'] = News.object.all()

        context_data['range'] = range(1, 6)

        return context_data

    def get(self, *args, **kwargs):
        query = self.request.GET.get('q', None)
        if query:
            return HttpResponseRedirect(f'https://google.ru/search?q={query}')

        return super().get(*args, **kwargs)
