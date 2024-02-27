import utils
from textual.widgets import Markdown


class Topic5:
    name = "Тема 5: Gitea"

    def compose(self):
        return [
            Markdown(
                """
## Введение
Gitea - это программное обеспечение с открытым исходным кодом для создания собственного сервера Git. Ваша задача - установить Gitea.


## Задание 5.1
Загрузите исполняемый файл Gitea с [официального сайта](https://dl.gitea.com/gitea/) и поместите его в /usr/local/bin/gitea, дав ему права на выполнение.
"""
            ),
            utils.task_check_widget(self, "5-1"),
            Markdown(
                """
## Задание 5.2
Создайте пользователя git.
"""
            ),
            utils.task_check_widget(self, "5-2"),
            Markdown(
                """
## Задание 5.3
Создайте следующие директории:
- /var/lib/gitea/\{custom, data, log\} с правами 750 и владельцем git:git
- /etc/gitea с правами 770 и владельцем git:git
""",
            ),
            utils.task_check_widget(self, "5-3"),
            Markdown(
                """
## Задание 5.4
Переведите SELinux в режим permissive.
                """
            ),
            Markdown(
                """
## Задание 5.5
Создайте службу Systemd для Gitea и запустите её.
""",
            ),
            utils.task_check_widget(self, "5-5"),
            Markdown(
                """
## Задание 5.6
Создайте конфигурационный файл Nginx gitea.conf и настройте в нём обратный прокси gitea на linux.local/gitea и перезапустите его.
""",
            ),
            utils.task_check_widget(self, "5-6"),
            Markdown(
                """
## Задание 5.7
Пройдите первоначальную настройку Gitea, используя в качестве параметров базы данных параметры, которые вы использовали при настройке PostgreSQL.
""",
            ),
            utils.task_check_widget(self, "5-7"),
            Markdown(
                """
## Заключение
Вы успешно установили и настроили Gitea. Давайте подведем итоги.""",
            ),
        ]
