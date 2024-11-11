from utils.widgets.multiple_choice import MultipleChoiceQuestion


QUESTION_TABLE: dict[str, MultipleChoiceQuestion] = {
    "theory-alternation": MultipleChoiceQuestion(
        question="Consider the alternation operation. "
                 "Suppose that our alphabet consists of all lowercase characters of the alphabet and "
                 "the empty string, ε. "
                 "Moreover, suppose we have the regular expression `a ∪ b ∪ c`. "
                 "Which of the following is a string which this expression accepts?",
        answers=["ab", "aaaaabbbccc", "c", "ε"],
        correctness_mapping={
            0: False,
            1: False,
            2: True,
            3: False
        },
        explanations={
            0: "The alternation operation indicates a choice between symbols, "
               "and it does not allow for more than one selection.",
            1: "The options for alternation may only be selected once "
               "when a Kleene star is not used on the expression. "
               "Moreover, alternation does not allow for more than one selection.",
            2: "Alternation only permits the selection of a single option among those presented, "
               "which only the string \"c\" fulfills.",
            3: "The empty string is not an option presented by alternation; "
               "an option provided must be selected."
        }
    ),
    "theory-concatenation": MultipleChoiceQuestion(
        question="Consider the concatenation operation. "
                 "Suppose that our alphabet consists of all lowercase characters of the alphabet and "
                 "the empty string, ε. "
                 "Moreover, suppose we have the regular expression `abc`. "
                 "Which of the following is a string which this expression accepts?",
        answers=["ε", "abc", "cba", "a"],
        correctness_mapping={
            0: False,
            1: True,
            2: False,
            3: False
        },
        explanations={
            0: "The concatenation operation joins symbols together in a specific order. "
               "It does not permit the empty string as an option.",
            1: "Concatenation joins the symbols \"a\", \"b\", and \"c\" together in that order, "
               "as that is the order of these symbols in the regular expression.",
            2: "Concatenation is an ordered operation; "
               "different orderings of \"a\", \"b\", and \"c\" represent different strings.",
            3: "In concatenation, two or more symbols are joined together and "
               "conditioned on one another in a specified order. "
               "This answer only has one symbol, disobeying the principles of the operation."
        }
    ),
    "theory-quantification": MultipleChoiceQuestion(
        question="Consider the quantification operation. "
                 "Suppose that our alphabet consists of all lowercase characters of the alphabet and "
                 "the empty string, ε. "
                 "Moreover, suppose we have the regular expression `a*`. "
                 "Which of the following is a NOT string which this expression accepts?",
        answers=["ε", "a", "aaaaaaa", "aaaab"],
        correctness_mapping={
            0: False,
            1: False,
            2: False,
            3: True
        },
        explanations={
            0: "The quantification operation permits zero or more repetitions of the symbol or expression it modifies. "
               "As a result, `a*` includes the empty string.",
            1: "Quantification can permit one instance of the symbol it modifies; "
               "it does not have to repeat multiple times.",
            2: "Quantification can generate as many instances as it desires for the string it modifies. "
               "As a result, no matter how many `a`s are added to the end of this string, "
               "the expression will accept the string.",
            3: "Quantification cannot generate new symbols; it only allows for the symbol it modifies to be repeated."
        }
    ),
    "theory-negative-numbers": MultipleChoiceQuestion(
        question="Suppose that our alphabet consists of all digits, the character \"-\", "
                 "the character \"_\" (here, representing a space), "
                 "and the empty string, ε. "
                 "Which of the following could we prefix to our original regular expression to allow negative numbers?",
        answers=["ε", "(-|ε)", "-", "-*", "(-|_)"],
        correctness_mapping={
            0: False,
            1: True,
            2: False,
            3: False,
            4: False
        },
        explanations={
            0: "While appending nothing would preserve all positive numbers, "
               "it would not support any negative numbers.",
            1: "To represent positive numbers, we need to include the empty string; "
               "to represent negative numbers, we need to use the \"-\" symbol",
            2: "This expression only supports negative numbers, "
               "as the negative sign would be required via concatenation.",
            3: "This expression can support positive or negative numbers, "
               "but it could also add additional dashes. In other words, it is too permissive.",
            4: "This expression can support negative numbers, "
               "but positive numbers would always be prefixed with a space. "
               "The space is distinct from the empty string."
        }
    ),
    "theory-decimals": MultipleChoiceQuestion(
        question="Suppose that our alphabet consists of all digits, the character \".\", and the empty string, ε. "
                 "Moreover, in the expressions below, let \"...\" indicate the alternation of digits 2 to 8 "
                 "in the same format as the digits printed explicitly."
                 "Which of the following could we suffix to our original regular expression to permit "
                 "the set of all decimals greater than or equal to 1.0? "
                 "You may assume that all numbers will have a decimal point and at least one subsequent digit.",
        answers=[
            ".(0 ∪ 1 ∪ ... ∪ 9)",
            "(.0 ∪ .1 ∪ ... ∪ .9)*",
            ".(0 ∪ 1 ∪ ... ∪ 9)*",
            ".(0 ∪ 1 ∪ ... ∪ 9)(0 ∪ 1 ∪ ... ∪ 9)*",
            "(.0 ∪ .1 ∪ ... ∪ .9)(0 ∪ 1 ∪ ... ∪ 9)*"
        ],
        correctness_mapping={
            0: False,
            1: False,
            2: False,
            3: True,
            4: True
        },
        explanations={
            0: "In this case, we would only permit decimals in the tenths place; "
               "thus, this expression is too restrictive.",
            1: "This expression would generate decimal points with each digit. A decimal only has a single point.",
            2: "Using the Kleene star, this expression could generate zero digits, which is not a valid decimal.",
            3: "This expression begins with a point, generates an initial required digit, "
               "and then follows it with as many optional digits as desired.",
            4: "This expression generates the first digit with a decimal point, "
               "and it then follows it up with optional additional digits."
        }
    ),
    "password-special-character": MultipleChoiceQuestion(
        question="Suppose that you want to assure that a password contains a special character "
                 "between the following symbols: \"~\", \"!\", \"@\", and \"#\". "
                 "Which of the following regular expressions would capture these characters--"
                 "and only these characters?",
        answers=[
            "~|!|@|#",
            ".",
            r"\p",
            "|~!@#|",
        ],
        correctness_mapping={
            0: True,
            1: False,
            2: False,
            3: False,
        },
        explanations={
            0: "Bar notation places a bar between each of its options.",
            1: "The period alone, as a special character in regular expression notation, "
               "would capture all of these characters. "
               "However, it would also catch any other character; it is too permissive.",
            2: r'"\p" is not a permissible shortcut notation.',
            3: "The use of bar notation here mimics bracket notation; "
               "bars do not format their alternatives in the same way.",
        }
    ),
    "password-single-digit": MultipleChoiceQuestion(
        question="Suppose that you want to assure that a password contains a single digit."
                 "Which of the following regular expressions would NOT capture these characters--"
                 "and only these characters?",
        answers=[
            r"\d",
            "[0123456789]",
            "[0-9]",
            r"[0|1|2|3|4|5|6|7|8|9]",
        ],
        correctness_mapping={
            0: False,
            1: False,
            2: False,
            3: True,
        },
        explanations={
            0: r'The "\d" shortcut refers to the set of all digits, so it does capture all digits.',
            1: "All numbers are presented in bracket notation, so they are all valid options.",
            2: "Since digits are ordered, using \"-\" is valid within bracket notation "
               "to represent the span of characters between \"0\" and \"9\".",
            3: "Bar notation does not work within bracket notation. "
               "As it stands, this expression is too permissive: it also captures \"|\".",
        }
    ),
    "password-three-two-one": MultipleChoiceQuestion(
        question="Suppose that you want your password to consist of three alphabetic characters of any case, "
                 "two numbers, an underscore, and one special character among \"~\", \"!\", \"@\", in that order."
                 "Which of the following regular expressions correctly expresses this?",
        answers=[
            r"[a-zA-Z][a-zA-Z][a-zA-Z]\d\d_[~!@]",
            r"[a-zA-Z]\d_[~!@]",
            r"[a-zA-Z] \d _ [~!@]",
            r"[a-zA-Z][a-zA-Z][a-zA-Z] \d\d _ [~!@]",
        ],
        correctness_mapping={
            0: True,
            1: False,
            2: False,
            3: False,
        },
        explanations={
            0: r"Concatenation combines an individual choice from each alternation or symbol, "
               r"so \"[a-zA-Z]\" needs to be represented thrice, \"\d\" twice, \"_\" once, and \"[~!@\" once",
            1: "Concatenation does not allow for more than one choice per alternation; "
               "alternations can only be selected the number of times that they're presented.",
            2: "Concatenation does not require spaces between each alternation. "
               "Moreover, alternations can only be selected the number of times that they're presented.",
            3: "Concatenation does not require spaces between each alternation."
        }
    ),
    "survey-options": MultipleChoiceQuestion(
        question="Suppose that you want to match items in a survey that were placed on a Likert scale. "
                 "In particular, the survey's options were "
                 "\"Strongly Disagree\", \"Disagree\", \"Neutral\", \"Agree\", and \"Strongly Agree\". "
                 "Which of the following regular expressions would capture these five options?",
        answers=[
            r"[Strongly Disagree]|[Disagree]|[Neutral]|[Agree]|[Strongly Agree]",
            r"Strongly Disagree|Disagree|Neutral|Agree|Strongly Agree",
            r"Strongly [Agree|Disagree]|Neutral",
            r"Strongly|Disagree|Neutral|Agree",
        ],
        correctness_mapping={
            0: False,
            1: True,
            2: False,
            3: False,
        },
        explanations={
            0: "Each choice in this bar alternation is a set alternation, "
               "meaning that only one symbol will be picked from each. "
               "This not only includes many options that are not desired, "
               "but it also does not include any of the Likert scale items.",
            1: "Concatenated strings in a regular expression can in turn be the alternatives of bar alternation.",
            2: "The bracket alternation does not allow for any nesting alternation. "
               "The bar is considered a symbol which can be chosen between all those in square brackets. "
               "Moreover, it is not possible to choose solely \"Agree\" or \"Disagree\", "
               "since concatenating \"Strongly\" is required.",
            3: "Bar alternation only selects one alternative, even among concatenated alternatives. "
               "As a result, \"Strongly Agree\" and \"Strongly Disagree\" are impossible to produce."
        }
    ),
    "practical-negative-numbers": MultipleChoiceQuestion(
        question=r'In the introduction to this section on regular expressions, '
                 r'we stated that we could capture all positive integers with the expression `[1-9]\d*`. '
                 r'Which of the following expressions also captures all negative integers? '
                 r'Note that negative integers are prefixed with one "-", whereas positive integers have no prefix.',
        answers=[
            r"-[1-9]\d*",
            r"-+[1-9]\d*",
            r"-*[1-9]\d*",
            r"-?[1-9]\d*"
        ],
        correctness_mapping={
            0: False,
            1: False,
            2: False,
            3: True,
        },
        explanations={
            0: "In this expression, all numbers will be prefixed with a negative sign. "
               "Thus, it won't be possible to match positive numbers anymore.",
            1: "The \"+\" character states that one or more alternatives of its modifying alternation will be used. "
               "This means that all numbers will be prefixed with a negative sign, "
               "making positive numbers impossible to match. "
               "Moreover, multiple negative signs do not straightforwardly indicate "
               "either the positive or negative sets of integers.",
            2: "The \"*\" character states that zero or more alternatives of its modifying alternation will be used. "
               "This means that, while both positive and negative numbers are possible, "
               "numbers with multiple negative signs will also be. This behavior is too permissive.",
            3: "The \"?\" character either allows for the \"-\" exactly once or not at all, "
               "fitting the needs for modeling positive and negative integers."
        }
    ),
    "practical-decimals": MultipleChoiceQuestion(
        question=r'In the introduction to this section on regular expressions, '
                 r'we stated that we could capture all positive integers with the expression `[1-9]\d*`. '
                 r'Which of the following expressions tweaks that expression to capture '
                 r'all decimal values greater than or equal to one?',
        answers=[
            r"[1-9]\d*[.][0-9]*",
            r"[1-9]\d*[.][0-9]?",
            r"[1-9]\d*[.][0-9]+",
            r"[1-9]\d*[.][0-9]{2,}",
        ],
        correctness_mapping={
            0: False,
            1: False,
            2: True,
            3: False,
        },
        explanations={
            0: "The \"*\" character can produce zero digits, leaving the expression without a value after the decimal. "
               "This is not a valid decimal, meaning that the expression is too permissive.",
            1: "The \"?\" character can produce either one or zero digits. "
               "Not only is a decimal without digits invalid, but many decimals contain more than one digit.",
            2: "Decimals are expressed with at least one value after the decimal point. "
               "The \"+\" character requires one digit and allows for as many as desired, "
               "which suits the requirements of representing any decimal.",
            3: "The curly bracket quantification could be used for representing all decimals, "
               "but starting with a minimum of 2 is too high: a decimal can have exactly one digit. "
               "This expression leaves that case out; thus, it is too restrictive."
        }
    ),
    "hexadecimals": MultipleChoiceQuestion(
        question=r"Hexadecimal, or base-16, strings can also represent bytes. "
                 r"Each hex digit (drawn from digits 0-9 and letters A-F) corresponds to four bits, "
                 r"which in turn corresponds to half a byte (also known as a nibble). "
                 r"Let's suppose that we want to match strings of hex digits that correspond to valid bit strings. "
                 r"Which of the following regular expressions accomplishes that?",
        answers=[
            r"[0-9A-F]{2,2}",
            r"([0-9A-F]{2,2})+",
            r"([0-9A-F]*){2,2}",
            r"([0-9A-F]+){2,2}",
        ],
        correctness_mapping={
            0: False,
            1: True,
            2: False,
            3: False,
        },
        explanations={
            0: "While this would only produce valid hex digits that represent bytes, "
               "it would only produce two-digit hexadecimals. "
               "Since there are bytes that are longer than eight bits (two hex digits), this is too restrictive.",
            1: "Each pair of hex digits represents a byte. "
               "Thus, we need to accumulate pairs of hex digits--and only pairs--to retain valid hexadecimal bytes.",
            2: "The grouping and quantification is combined incorrectly here. "
               "This expression could match zero hex digits (which is not valid) as well as any number of hex digits--"
               "exactly twice. In other words, any hex digit string of two or more hex digits would be matched. "
               "This is too permissive.",
            3: "The grouping and quantification is combined incorrectly here. "
               "This expression could match any string of at least two hex digits; "
               "essentially, it would cut a hex string into two pieces to match it. "
               "This is too permissive."
        }
    ),
    "dates": MultipleChoiceQuestion(
        question=r"Suppose that you want to match and gather information on dates. "
                 r"You write the following regular expression: `(<month>\d{2,2})/(<day>\d{2,2})/(<year>\d{4,4})`. "
                 r"One of the dates is \"12/31/1999\". "
                 r"What indexed and named groups would the regular expression output?",
        answers=[
            "None; the regular expression would not match this output.",
            "Group 0: \"12\"; Group 1: \"31\"; Group 2: \"1999\";\n"
            "Group \"month\": \"12\", Group \"day\": \"31\"; Group \"year\": \"1999\"",
            "Group 0: \"12/31/1999\"; Group 1: \"12\"; Group 2: \"31\"; Group 3: \"1999\";\n"
            "Group \"month\": \"12\", Group \"day\": \"31\"; Group \"year\": \"1999\"",
            "Group 0: \"12311999\"; Group 1: \"12\"; Group 2: \"31\"; Group 3: \"1999\";\n"
            "Group \"month\": \"12\", Group \"day\": \"31\"; Group \"year\": \"1999\"",
        ],
        correctness_mapping={
            0: False,
            1: False,
            2: True,
            3: False,
        },
        explanations={
            0: "The regular expression would match the string.",
            1: "The indexed groups are incorrect. Group 0 is the full string which is matched, "
               "and user-defined subgroups follow that group.",
            2: "The indexed groups begin with the full string that was matched; "
               "then, the user-defined subgroups--which are also named here--follow.",
            3: "Group 0 among the indexed groups is not correct. Group 0 is the fully-matched string, "
               "which includes the slashes that are not in subgroups."
        }
    ),
}
