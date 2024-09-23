# Jupyter Worksheet Library
This library helps support creating IPYNB worksheet exercises. Current version includes:
1. Hints - via HTML text, and hidden/shown via a button.
2. Quizzes - via [John M. Shea's `jupyterquiz` library](https://github.com/jmshea/jupyterquiz).


### Installation:
Pip install should install all required dependencies, which include `pandas, IPython, jupyterquiz==2.7.0a4`.
```
pip install git+https://github.com/pmdscully/jupyter_worksheet_lib.git
```


### Filenames and Source Data (draft-status):
In the current draft version, all files are stored in the same directory your IPYNB file. In a future version, this will use a single file format and be stored elsewhere, such as a URL (following a similar implementation as `jupyterquiz`)
- Your IPYNB file.
- Hints source data: - Excel spreadsheet (XLSX) under two columns (`Ref` and `Hint`). 
    - `worksheet_w1.xlsx`
    - `worksheet_w2.xlsx`
- Quiz source data: - in JSON format under the [`jupyterquiz`](https://github.com/jmshea/jupyterquiz) format.
    - `worksheet_w1_q1.json`
 
### Usage:
See the `example_notebook.ipynb` as an example IPYNB worksheet.

#### Usage: Hints
```
!pip install git+https://github.com/pmdscully/jupyter_worksheet_lib.git
from lib_worksheet import Worksheet
worksheet = Worksheet('w1')
worksheet.hint.offer('q1')
```
![image](https://github.com/user-attachments/assets/a5f1a574-d0f6-4a69-bf47-9a222578e35e)

![image](https://github.com/user-attachments/assets/2d8c845f-cbca-4f73-9077-414fc4392964)

![image](https://github.com/user-attachments/assets/a5f1a574-d0f6-4a69-bf47-9a222578e35e)

#### Usage: Quiz
```
worksheet.quiz('q1')
```
![image](https://github.com/user-attachments/assets/b1a7b780-c58a-4467-8521-a74e93e85111)

