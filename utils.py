import os, importlib.util, inspect, subprocess, requests
from textual.widgets import Button, Label
from textual.containers import Horizontal, Center


def topic_list():
    task_modules = []
    tasks_folder = "tasks"
    for file in sorted(os.listdir(tasks_folder)):
        if file.endswith(".py"):
            module_name = file[:-3]
            spec = importlib.util.spec_from_file_location(
                module_name, os.path.join(tasks_folder, file)
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            task_modules.append(module)

    task_list = []
    for module in task_modules:
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and name.startswith("Topic"):
                task_list.append(obj)
    return task_list


def task_check_widget(self, task_number):
    if task_number not in self.remaining_tasks:
        self.remaining_tasks.append(task_number)    
    return Horizontal(
        Button(" Проверить", id=f"verify-{task_number}"),
        Center(Label("Не выполнено", id=f"result-{task_number}")),
        classes="task-check",
    )


def task_check_widget_update(self, task_number, success):
    if success:
        self.query_one(f"#result-{task_number}").update("Выполнено")
        button = self.query_one(f"#verify-{task_number}")
        button.variant = "success"
        button.disabled = True
        self.remaining_tasks.pop(task_number)
        
    else:
        self.query_one(f"#result-{task_number}").update("При проверке возникла ошибка")
        button = self.query_one(f"#verify-{task_number}")
        button.variant = "error"
        self.query_one("#main-content").focus()
    

# такие костыли нужны потому что правило iptables может быть записано в разной форме и сравнение строк не всегда сработает
def check_iptables(params):
    rules = subprocess.check_output("pkexec sudo iptables -S", shell=True, text=True)
    for rule in rules.split("\n"):
        if all(params in rule for params in params.split(" ")):
            return True
    return False


def check_task(self, task_number):
    if task_number == "1-1":
        output = subprocess.check_output(
            "pkexec cat /etc/ssh/sshd_config", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "Port 3243" in output)
    elif task_number == "1-2":
        with open(f"/home/{os.environ['USER']}/.ssh/id_rsa", "r") as f:
            task_check_widget_update(
                self, task_number, "-----BEGIN OPENSSH PRIVATE KEY-----" in f.readline()
            )
    elif task_number == "1-3":
        # запросить доступ к руту через polkit и найти в файле /etc/ssh/sshd_config строку PasswordAuthentication no
        try:
            sshd_config = subprocess.check_output(
                "pkexec cat /etc/ssh/sshd_config", shell=True, text=True
            )
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
        task_check_widget_update(
            self, task_number, check_iptables(iptables_params[task_number])
        )
    elif task_number == "3-1":
        output = subprocess.run("rpm -q postgresql14-server", shell=True)
        task_check_widget_update(self, task_number, output.returncode == 0)
    elif task_number == "3-2":
        output = subprocess.run("pkexec ls /var/lib/pgsql/14/data", shell=True)
        task_check_widget_update(self, task_number, output.returncode == 0)
    elif task_number == "3-3":
        output = subprocess.check_output(
            "systemctl status postgresql-14", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "active (running)" in output)
    elif task_number == "3-4":
        output = subprocess.check_output(
            "pkexec --user postgres psql -c \\\du", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "nextcloud" in output)
    elif task_number == "3-5":
        output = subprocess.check_output(
            "pkexec --user postgres psql -c \\\l", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "nextcloud" in output)
    elif task_number == "3-6":
        output = subprocess.check_output(
            "pkexec --user postgres psql -c \\\du", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "gitea" in output)
    elif task_number == "3-7":
        output = subprocess.check_output(
            "pkexec --user postgres psql -c \\\l", shell=True, text=True
        )
        task_check_widget_update(self, task_number, "gitea" in output)
    elif task_number == "3-8":
        output = subprocess.check_output(
            "pkexec cat /var/lib/pgsql/14/data/pg_hba.conf", shell=True, text=True
        )
        result = False
        for line in output.split("\n"):
            if (
                "host" in line
                and "all" in line
                and "127.0.0.1/32" in line
                and "md5" in line
            ):
                result = True
        task_check_widget_update(self, task_number, result)
    elif task_number == "3-9":
        output = subprocess.check_output(
            "pkexec cat /var/lib/pgsql/14/data/postgresql.conf", shell=True, text=True
        )
        task_check_widget_update(
            self,
            task_number,
            ("listen_addresses = '*'" in output and "port = 5432" in output),
        )
    elif task_number in ["4-1", "4-2", "4-3", "4-4", "4-5"]:
        selinux_params = {
            "4-1": "httpd_can_network_connect",
            "4-2": "httpd_graceful_shutdown",
            "4-3": "httpd_can_network_connect_db",
            "4-4": "domain_can_mmap_files",
            "4-5": "daemons_dump_core",
        }
        output = subprocess.check_output(
            f"pkexec sudo getsebool {selinux_params[task_number]}",
            shell=True,
            text=True,
        )
        task_check_widget_update(self, task_number, output.strip().endswith("on"))
    elif task_number == "5-1":
        output = subprocess.run(
            "rpm -q nextcloud nextcloud-postgresql nextcloud-nginx",
            shell=True,
            text=True,
        )
        task_check_widget_update(self, task_number, output.returncode == 0)
    elif task_number == "5-2":
        output = subprocess.check_output(
            "pkexec cat /etc/nginx/nginx.conf", shell=True, text=True
        )
        task_check_widget_update(
            self,
            task_number,
            (
                "sendfile on" in output
                and "proxy_connect_timeout 600s" in output
                and "proxy_send_timeout 600s" in output
                and "proxy_read_timeout 600s" in output
                and "fastcgi_read_timeout 600s" in output
                and "fastcgi_send_timeout 600s" in output
            ),
        )
    elif task_number == "5-3":
        output = subprocess.check_output(
            "pkexec cat /etc/php.ini", shell=True, text=True
        )
        task_check_widget_update(
            self,
            task_number,
            (
                "memory_limit = 512M" in output
                and "max_input_vars = 1000" in output
                and "max_execution_time = 3600" in output
                and "upload_tmp_dir = /tmp" in output
            ),
        )
    elif task_number == "5-4":
        task_check_widget(
            self, task_number, os.path.exists("/usr/share/nextcloud/config/CAN_INSTALL")
        )
    elif task_number == "5-5":
        task_check_widget(
            self,
            task_number,
            requests.get("http://linux.local/nextcloud/index.php/login").status_code
            == 200,
        )
    elif task_number == "6-1":
        try:
            os.access("/usr/local/bin/gitea", os.X_OK)
        except:
            result = False
        else:
            result = True
        task_check_widget_update(self, task_number, result)
    elif task_number == "6-2":
        output = subprocess.run("id git", shell=True)
        task_check_widget_update(self, task_number, output.returncode == 0)
    elif task_number == "6-3":
        task_check_widget(
            self,
            task_number,
            os.path.exists("/var/lib/gitea/custom")
            and os.path.exists("/var/lib/gitea/data")
            and os.path.exists("/var/lib/gitea/log")
            and os.path.exists("/etc/gitea"),
        )
    elif task_number == "6-4":
        output = subprocess.run("systemctl status gitea", shell=True, text=True)
        task_check_widget_update(self, task_number, "active (running)" in output)
    elif task_number == "6-5":
        output = subprocess.check_output("nginx -t", shell=True, text=True)
        task_check_widget_update(self, task_number, "successful" in output and os.path.exists("/etc/nginx/conf.d/gitea.conf"))
    elif task_number == "6-6":
        task_check_widget(
            self,
            task_number,
            requests.get("http://linux.local/gitea").status_code == 200,
        )
    
        