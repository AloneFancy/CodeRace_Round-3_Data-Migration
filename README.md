# CODE_RACE_R2T3

BOSCH_CODERACE 2023 ROUND 2_DATA MIGRATION Topic 3

## Requirements

```python
python -m pip install -r requirements.txt
```

## Usage

### Task 1

Input: **Requirements.reqif** in the same folder with **final.py**

Command line:

```
python final.py [PROFILE]
```
**Note**: The program only receives one argument as the PROFILE that users need to set it in file **.conf**. The **DEFAULT** profile will be used if no arguments provided.

Output: **data.json**

### Task 2
Input:

Output:  **ECU_REQ.rst**

### Task 3

**Upload** or **Update** (replace if existed) RST file to Github with authorization in auth.py
"Auth.py"'s structure that you should generate yourself:\
Auth.py\
&nbsp;&nbsp;   |__username\
&nbsp;&nbsp;   |__password\
&nbsp;&nbsp;   |__token

```python
python gitupload.py
```

Source files: **convert.py**, **final.py**, **requirements.txt**
