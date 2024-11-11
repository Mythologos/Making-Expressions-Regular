# Making Expressions Regular

**Author**: Stephen Bothwell (University of Notre Dame)
- _Supervision_: Julie Vecchio

**Maintainer**: Stephen Bothwell

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Mythologos/Making-Expressions-Regular/HEAD)

## Overview

This repository contains a Jupyter notebook meant to educate on the use of regular expressions in Python 3. 
It was developed around the time of Python 3.11 and 3.12, 
and it is aware of changes to `re` that have occurred across the development of Python 3.

## Organization

This repository contains its main contribution, the `making-expressions-regular.ipynb` Jupyter notebook, 
in the top-level directory. Within the `utils` directory, there is a set of custom modules used in the notebook.
These include a set of `widgets` which can verify regular expressions and show whether a given input matches that expression or not (`regex_verifier.py`), 
and it also defines multiple choice questions for the notebook (`multiple_choice.py`). The actual multiple choice questions used are stored in the `activities` subdirectory (see `question_table.py`).

## Prerequisites

The tutorial expects knowledge of basic programming constructions (iteration, conditions) and,
more specifically, Python syntax for those conditions. 

## Feedback

If you have any questions or feedback, please feel free to contact the author of this tutorial. 
His contact email will be available at [his website](https://mythologos.github.io/).
