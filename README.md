# H1 NS2 trace file interpreted
this program was created to simply the process of calculating various values from trace file that are generated from NS2 trace files.<br>trace file extension `.tr`

packages used - <li>Kivy (for ui)
<li> subprocessbr
<br>
the calculations are done by the awk scripts

to run this file create a virtual environment and install the requirements.txt file

```
virtualenv <environment name>
pip install -r requirements.txt
```
then activate the virtual environment
```
source <environment name>/bin/activate (this is for linux)
```
after installing the requirements.txt. just run the main.py file
```
python main.py
```
