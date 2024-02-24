import utils
from textual.widgets import Markdown


class Topic3:
    name = "Тема 3: База данных"

    def compose(self):
        return [
            Markdown(
                """
## Введение
Вам необходимо поднять сетевые службы как Nextcloud и Gitea, но перед этим необходимо настроить базу данных. Ваша задача установить PostgreSQL и создать базых данных для Nextcloud и Gitea.
## Задание 3.1
Установите PostgreSQL 15 с помощью пакетного менеджера dnf.
"""
            ),
            utils.task_check_widget("3-1"),
            Markdown(
                """
## Задание 3.2
Инициализируйте базу данных."""
            ),
            utils.task_check_widget("3-2"),
            Markdown(
                """
## Задание 3.3
Включите и запустите службу PostgreSQL.
"""
            ),
            utils.task_check_widget("3-3"),
            Markdown(
                """
## Задание 3.4
Создайте пользователя БД nextcloud"""
            ),
            utils.task_check_widget("3-4"),
            Markdown(
                """
## Задание 3.5
Создайте базу данных nextcloud, которой владеет пользователь nextcloud"""
            ),
            utils.task_check_widget("3-5"),
            Markdown(
                """
## Задание 3.6
Создайте пользователя БД gitea"""
            ),
            utils.task_check_widget("3-6"),
            Markdown(
                """
## Задание 3.7
Создайте базу данных gitea, которой владеет пользователь gitea"""
            ),
            utils.task_check_widget("3-7"),
            Markdown(
                """
## Задание 3.8
В файле /var/lib/pgsql/15/data/pg_hba.conf измените метод аунтефикации с scram-sha-256 на md5 для локальных IPv4 и IPv6 соеденений и перезапустите службу БД"""
            ),
            utils.task_check_widget("3-8"),
            Markdown(
                """ 
## Заключение
Вы настроили базу данных. Теперь перейдем к установке Nextcloud.
"""
            ),
        ]
