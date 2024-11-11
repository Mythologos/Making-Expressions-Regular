from re import compile, error, fullmatch, Match, Pattern
from typing import Optional

from IPython.core.display_functions import DisplayHandle
from IPython.display import display
from ipywidgets import Checkbox, HBox, interactive_output, Output, Text, VBox, Widget


class RegexVerifier:
    def __init__(self):
        regex_textbox: Text = Text(description="Regex:", placeholder=r"\d*")
        string_textbox: Text = Text(description="String:", placeholder="42")
        group_checkbox: Checkbox = Checkbox(description="Numbered Groups")
        named_group_checkbox: Checkbox = Checkbox(description="Named Groups")

        textbox_vbox: VBox = VBox(children=[regex_textbox, string_textbox])
        checkbox_vbox: VBox = VBox(children=[group_checkbox, named_group_checkbox])
        interact_hbox: HBox = HBox(children=[textbox_vbox, checkbox_vbox])
        feedback: Output = Output()

        self.regex_verifier_mapping: dict[str, Widget] = {
            "regex": regex_textbox,
            "string": string_textbox,
            "show_groups": group_checkbox,
            "show_named_groups": named_group_checkbox
        }
        self.regex_verifier_interface: VBox = VBox(children=[interact_hbox, feedback])
        self.regex_verifier_output = interactive_output(self.apply_regex, self.regex_verifier_mapping)

    def display(self) -> DisplayHandle:
        return display(self.regex_verifier_interface, self.regex_verifier_output)

    @classmethod
    def apply_regex(cls, regex: str, string: str, show_groups: bool = False, show_named_groups: bool = False):
        try:
            pattern: Pattern = compile(regex)
        except error:
            print(f"Regular expression \"{regex}\" is not valid.")
        else:
            current_match: Optional[Match] = fullmatch(pattern, string)
            if current_match is not None:
                print(f"Regular expression \"{regex}\" matches \"{string}\".")
                if show_named_groups is True:
                    cls._print_named_groups(current_match)
                elif show_groups is True:
                    cls._print_groups(current_match)
            else:
                print(f"Regular expression \"{regex}\" does not match string \"{string}\".")

    @classmethod
    def _print_groups(cls, current_match: Match):
        # We put "start=1" here because .groups() only iterates over subgroups.
        for group_number, group in enumerate(current_match.groups(), start=1):
            print(f"\tGroup {group_number}: \"{group}\"")

    @classmethod
    def _print_named_groups(cls, current_match: Match):
        for group_name, group_value in current_match.groupdict().items():
            print(f"\tGroup \"{group_name}\": \"{group_value}\"")
