import utils
from textual.widgets import Markdown


class Topic4:
    name = "Тема 4: SELinux"

    def compose(self):
        return [
            Markdown(
                """
## Введение 
Для правильной работы веб-сервера необходимо настроить SELinux. Ваша задача - правильно настроить переключатели SELinux.
## Задание 4.1
Включите переключатель httpd_can_network_connect.
"""
            ),
            utils.task_check_widget("4-1"),
            Markdown(
                """
## Задание 4.2
Включите переключатель httpd_graceful_shutdown.
"""
            ),
            utils.task_check_widget("4-2"),
            Markdown(
                """
## Задание 4.3
Включите переключатель httpd_can_network_connect_db.
"""
            ),
            utils.task_check_widget("4-3"),
            Markdown(
                """
## Задание 4.4
Включите переключатель domain_can_mmap_files.
"""
            ),
            utils.task_check_widget("4-4"),
            Markdown(
                """
## Задание 4.5
Включите переключатель daemons_dump_core.
"""
            ),
            utils.task_check_widget("4-5"),
        ]
