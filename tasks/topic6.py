from textual.widgets import Markdown

class Topic6:
    name = "Тема 6: Заключение"
    def compose(self):
        # я рассчитываю на то, что пользователь не будет лезть в заключение, если не выполнил все задания
        widgets = [Markdown("# Заключение")]
        if self.remaining_tasks == []:
            widgets.append(Markdown("Вы успешно выполнили все задания! Тестирование завершено."))
        else:
            widgets.append(Markdown(f"Вам осталось выполнить задания {', '.join(self.remaining_tasks).replace('-', '.')}"))
        return widgets