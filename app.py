from textual.app import App, ComposeResult
from textual.widgets import OptionList, Button
from textual.containers import VerticalScroll
import utils

topic_list = utils.topic_list()


class Tbapp(App):

    completed_tasks = []
    CSS_PATH = "app.tcss"

    def compose(self) -> ComposeResult:
        task_names = [task.name for i, task in enumerate(topic_list)]
        yield OptionList(*task_names, id="sidebar")
        yield VerticalScroll(id="main-content", *topic_list[0].compose(self))

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        self.query_one("#main-content").remove_children()
        self.query_one("#main-content").mount_all(
            topic_list[event.option_index].compose(self)
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        task_number = event.button.id.replace("verify-", "")
        utils.check_task(self, task_number)


if __name__ == "__main__":
    app = Tbapp()
    app.run()
