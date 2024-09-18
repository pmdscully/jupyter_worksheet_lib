# Jupyter Worksheet Library
This library helps support creating IPYNB worksheet exercises. 

#### Current version includes:
1. Hints - via HTML text, and hidden/shown via a button.
2. Quizzes - via [John M. Shea's `jupyterquiz` library](https://github.com/jmshea/jupyterquiz).

#### Creating source data:
- **Hints** are entered into an Excel spreadsheet (XLSX) under two columns (`Ref` and `Hint`). 
- **Quizzes** are entered in JSON format under the [jupyterquiz](https://github.com/jmshea/jupyterquiz) format.

#### Locations and Filenames (draft-status):
In the current draft version, all files are stored in the same directory your IPYNB file.
- Your IPYNB file.
- Hints source data:
    - `worksheet_w1.xlsx`
    - `worksheet_w2.xlsx`
- Quiz source data:
    - `worksheet_w1_q1.json`
 
#### Installation:
Pip install should all dependencies, which include `pandas IPython jupyterquiz==2.7.0a4`.
```
pip install git+https://github.com/pmdscully/jupyter_worksheet_lib.git
```

#### Usage:
```
from lib_worksheet import Worksheet
worksheet = Worksheet('w1')
worksheet.hint.offer('q1')
worksheet.quiz('q1')
```
