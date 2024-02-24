import utils
from textual.widgets import Markdown
from textual.app import ComposeResult


class Topic1:
    name = "1. Удаленной доступ"

    def compose(self):
        return [
            Markdown(
                """
## Введение
Представьте ситуацию: вы работаете системным администратором в небольшой организации. Вам предстоит настроить сервер под управлением РедОС 7.3. Ваша задача - выполнить ряд заданий, которые помогут вам освоить основные навыки работы с системой.
В боковой панели представлен список тем, задания по которым вам предстоит выполнить. В первую очередь, нам необходимо позаботиться о безопасности сервера.
## Задание 1.1 
Для начала смените порт SSH на 3243. Это поможет уменьшить количество попыток взлома сервера.
"""
            ),
            utils.task_check_widget("1-1"),
            Markdown(
                """
## Задание 1.2
Сгенерируйте ключи SSH для вашего пользователя. Это позволит вам безопасно подключаться к серверу без ввода пароля.
"""
            ),
            utils.task_check_widget("1-2"),
            Markdown(
                """
## Задание 1.3
Отключите доступ к серверу по паролю. Это не позволит злоумышленникам подобрать пароль и войти на сервер. 
"""
            ),
            utils.task_check_widget("1-3"),
            Markdown(
                """       
## Заключение
Вы настроили доступ к серверу. Теперь перейдем к настройке файрволла."""
            ),
        ]
