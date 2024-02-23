import subprocess, utils
from textual.widgets import Markdown, Button, Static
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual import log
class Topic1:
    name = "Тема 1"
    def compose(self) -> ComposeResult:
        return [Markdown("""
## Задание 1.1 Lorem ipsum
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec odio nec nunc tincidunt tincidunt.
"""), utils.task_check_widget("1-1")]
