from typing import Optional

from ipywidgets import Button, HBox, Output, RadioButtons, Widget, VBox


class MultipleChoiceQuestion(VBox):
    def __init__(self, question: str, answers: list[str], correctness_mapping: dict[int, Optional[bool]],
                 explanations: dict[int, str], **kwargs):
        self.question = question
        self.answers = answers
        self.correctness_mapping = correctness_mapping
        self.explanations = explanations

        # UI:
        self.question_description = Output()
        with self.question_description:
            print(self.question)

        self.option_buttons = RadioButtons(options=[key for key in self.answers], layout={"width": "max-content"}, )

        self.submit_button = Button(description="Check Answer")
        self.submit_button.on_click(self._check_selection)

        self.clear_button = Button(description="Clear Answer")
        self.clear_button.on_click(self._clear_selection)

        buttons: list[Button] = [self.submit_button, self.clear_button]
        button_box: HBox = HBox(buttons)

        self.feedback = Output()

        items: list[Widget] = [self.question_description, self.option_buttons, button_box, self.feedback]
        super().__init__(items, **kwargs)

    def _check_selection(self, button: Button):
        current_selection: Optional[str] = self.option_buttons.value
        if current_selection is not None:
            selection_index: int = self.answers.index(current_selection)
            self.feedback.clear_output()
            if self.correctness_mapping[selection_index] is True:
                with self.feedback:
                    print(f"That's correct! {self.explanations[selection_index]}")
            else:   # self.correctness_mapping[self.answers.index(current_selection)] is False:
                with self.feedback:
                    print(f"Sorry, that answer is incorrect. {self.explanations[selection_index]}")
        else:   # self.answers[current_selection] is None
            pass

    def _clear_selection(self, button: Button):
        self.feedback.clear_output()
        self.option_buttons.value = None

