from textual.app import App, ComposeResult
from textual.widgets import Header, Static, OptionList, Markdown, Button
from textual.containers import ScrollableContainer
from textual.widgets.option_list import Option

import utils
import subprocess
topic_list = utils.topic_list()
class Tbapp(App):
    
    completed_tasks = []
    CSS_PATH = "app.tcss"
    def compose(self) -> ComposeResult:
        # создать массив из названий заданий
        task_names = [task.name for i, task in enumerate(topic_list)]
        yield OptionList(*task_names, id="sidebar")
        with ScrollableContainer(id="main-content"):
            yield Markdown("Выберите задание")
            
    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        #clear contents of container
        self.query_one("#main-content").remove_children()
        self.query_one("#main-content").mount_all(topic_list[event.option_index].compose(self))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        task_number = event.button.id.replace("verify-", "")
        match task_number:
            case "1-1":
            # Запускать тесты
                pass
                    

if __name__ == "__main__":
    app = Tbapp()
    app.run()
