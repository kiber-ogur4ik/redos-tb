import utils
from textual.widgets import Markdown

class Topic5:
    name = "Тема 5: Nextcloud и Nginx"

    def compose(self):
        return [
            Markdown(
                """
## Введение
Nextcloud - это программное обеспечение с открытым исходным кодом для создания собственного облачного хранилища. Ваша задача - установить Nextcloud и настроить его, вместе с Nginx.

## Задание 5.1
Установите пакеты nextcloud nextcloud-postgresql nextcloud-nginx .
"""
            ),
            utils.task_check_widget(self,"5-1"),
            Markdown(
                """
## Задание 5.2
Настройте Nginx для работы с Nextcloud, сделая следующее:
- Установите таймауты proxy_connect, proxy_send, proxy_read, fastcgi_read, fastcgi_send в значение 600 секунд
- Перезапустите Nginx
"""
            ),
            utils.task_check_widget(self,"5-2"),
            Markdown(
                """
## Задание 5.3
Настройте PHP для работы с Nextcloud, сделав следующее:
- Установите лимит памяти в значение 512M
- Установите параметр max_input_vars в значение 1000
- Уставовите максимальное время выполнения в значение 3600
- Установите временную папку для загрузок в /tmp
"""
            ),
            utils.task_check_widget(self,"5-3"),
            Markdown(
                """
## Задание 5.4 
Запустите установку и настройку Nextcloud, создав файл CAN_INSTALL в /usr/share/nextcloud/config.
"""
            ),
            utils.task_check_widget(self,"5-4"),
            Markdown("""
## Задание 5.5
Пройдите первоначальную настройку Nextcloud, используя в качестве параметров базы данных параметры, которые вы использовали при настройке PostgreSQL.
                """
            ), utils.task_check_widget(self,"5-5"),
            Markdown("""
## Заключение
Вы успешно установили и настроили Nextcloud и Nginx. Давайте перейдём к следущей и заключительной теме.
            """
            )
        ]