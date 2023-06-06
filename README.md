# **CODE_RACE_R3T3**

BOSCH_CODERACE 2023 ROUND 3_DATA MIGRATION Topic 3

## Requirements

```python
python -m pip install -r requirements.txt
```

## **Usage**

### **Task 1**

Input: **Requirements.reqif** and **keys.conf** in the same folder with **final.py**

Command line:

```shell
python final.py  [PROFILE name in **keys.conf**]
```

**Note**: The program only receives one argument as the PROFILE that users need to set it in file **.conf**. The **DEFAULT** profile will be used if no arguments provided.

Output: **data.json** with mapped contents

### **Task 2**

Task 2 run sequently with Task 1 by the same command line.

Input: **data.json** extracted from RST file.

Output:  **ECU_REQ.rst** after user's configurations.

### **Task 3**

**Upload** or **Update** (replace if existed) RST file to Github with authorization in auth.py.\
"Auth.py"'s structure that you have to generate yourself:\
Auth.py\
&nbsp;&nbsp;   |__REPO_PATH: Path to your *Repository* starting with your *username*\
&nbsp;&nbsp;   |__token: Your Github token with enough permissions

```shell
python gitupload.py
```

Source files: **convert.py**, **final.py**, **requirements.txt**, **git_upload.py**, **globals.py**

### **Feature**

Task 1: 40
 - [ ]Array mapping: 10
 - [x]Attribute name and the same value: 10
 - [ ]Attribute name and customize value: 10
 - [ ]Easy to configure file: 5
 - [ ]Clean code: 5\
Task 2: 40
 - [ ]Heading, Information, Directive: 5
 - [ ]Attribute value text: 10
 - [ ]Sub-directive: 10
 - [ ]Html (convert html to RST text): 10
 - [ ]Clean code: 5\
Task 3: 20
 - [ ]Push to GitHub: 10
 - [ ]Overwrite: 5
 - [ ]Clean code: 5
