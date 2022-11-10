from django.core.management import BaseCommand

from mainapp.models import News


class Command(BaseCommand):

    # посточное заполнение БД - для каждой записи подключаемся

    # def handle(self, *args, **options):
    #     for i in range(10):
    #         News.object.create(
    #             title=f'title#{i}',
    #             preamble=f'preamble#{i}',
    #             body='some body'
    #         )

    # пакетное заполнение БД - создаем в оперативе и отправляем пакетом, экономим ресурсы подключения к БД

    def handle(self, *args, **options):
        news_list = []
        for i in range(10):
            news_list.append(News(
                title=f'title#{i}',
                preamble=f'preamble#{i}',
                body='some body'
            ))

        News.object.bulk_create(news_list)