### python version 
Python 3.10.12

For linux:

### To create enviroment:
python3 -m venv .venv

### To activate env:
source env/bin/activate

### To install package:
pip install -r .\requirements.txt

### To create a new requirements list, run:
 pip freeze > requirements.txt

### To run the project:
gunicorn -w 4 -b 127.0.0.1:5000 main:app