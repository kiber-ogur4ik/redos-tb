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
Перевести SELinux в режим permissive.
"""
            ),
            utils.task_check_widget("4-1"),
            Markdown(
                """
## Задание 4.2
Включите следущие переключатели:
- httpd_can_network_connect
- httpd_graceful_shutdown
- httpd_can_network_connect_db
- domain_can_mmap_files
- daemons_dump_core
"""
            ),
            utils.task_check_widget("4-2"),
            Markdown(
                """
## Задание 4.3
Перевести SELinux в режим enforcing.
"""
            ),
            utils.task_check_widget("4-3"),
            Markdown(
                """
## Заключение
Вы настроили SELinux. Теперь перейдем к установке Nextcloud и веб-сервера.
"""
            ),
        ]
