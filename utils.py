import os, importlib.util, inspect
from textual.widgets import Button, Label
from textual.containers import Horizontal, Center
import subprocess

def topic_list():
    task_modules = []
    tasks_folder = "tasks"

    for file in os.listdir(tasks_folder):
        if file.endswith(".py"):
            module_name = file[:-3]
            spec = importlib.util.spec_from_file_location(module_name, os.path.join(tasks_folder, file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            task_modules.append(module)

    task_list = []
    for module in task_modules:
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and name.startswith("Topic"):
                task_list.append(obj)
    return task_list

def task_check_widget(task_number):
    return Horizontal(Button(" Проверить", id=f"verify-{task_number}"), 
                       Center(Label("Не выполнено", id=f"result-{task_number}")), classes="task-check")

                      
def task_check_widget_update(self, task_number, success):
    if success:
        self.query_one(f"#result-{task_number}").update("Выполнено")
        button = self.query_one(f"#verify-{task_number}")
        button.variant = "success"
        button.disabled = True
    else: 
        self.query_one(f"#result-{task_number}").update("При проверке возникла ошибка")
        button = self.query_one(f"#verify-{task_number}")
        button.variant = "error"
        self.query_one("#main-content").focus()

#такие костыли нужны потому что правило iptables может быть записано в разной форме и сравнение строк не всегда сработает
def check_iptables(params):
    import platform

    rules = subprocess.check_output("pkexec sudo iptables -S", shell=True, text=True)
    for rule in rules.split("\n"):
        if all(params in rule for params in params.split(" ")):
            return True
    return False


def check_task(self, task_number):
    #TODO: проверка заданий и учет выполненных в completed_tasks
    if task_number == "1-1":
        result = subprocess.check_output("pkexec cat /etc/ssh/sshd_config", shell=True, text=True)
        task_check_widget_update(self, task_number, "Port 3243" in result)
    elif task_number == "1-2":
        with open(f"/home/{os.environ['USER']}/.ssh/id_rsa", "r") as f:
            task_check_widget_update(self, task_number, "-----BEGIN OPENSSH PRIVATE KEY-----" in f.readline())
    elif task_number == "1-3":
        # запросить доступ к руту через polkit и найти в файле /etc/ssh/sshd_config строку PasswordAuthentication no
        try:
            sshd_config = subprocess.check_output("pkexec cat /etc/ssh/sshd_config", shell=True, text=True)
            completed = "PasswordAuthentication no" in sshd_config
        finally:
            task_check_widget_update(self, task_number, completed) 
    elif task_number in ["2-1", "2-2", "2-3", "2-4", "2-5"]:
        iptables_params = {
            "2-1": "-P INPUT DROP",
            "2-2": "-A INPUT -m conntrack --ctstate RELATED,ESTABLISHED -j ACCEPT",
            "2-3": "-A INPUT -p tcp --dport 3243 -j ACCEPT",
            "2-4": "-A INPUT -p tcp --dport 80 -j ACCEPT",
            "2-5": "-A INPUT -p tcp --dport 443 -j ACCEPT",
            
        }
        task_check_widget_update(self, task_number, check_iptables(iptables_params[task_number]))
