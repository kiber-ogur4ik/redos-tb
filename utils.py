import os, importlib.util, inspect
from textual.widgets import Button, Label
from textual.containers import Horizontal, Center
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
        
    