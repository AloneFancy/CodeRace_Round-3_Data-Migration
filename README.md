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

Output: **output/data.json** with mapped contents

### **Task 2**

Task 2 run sequently with Task 1 by the same command line.

Input: **data.json** extracted from ReqIF file.

Output:  **output/ECU_Req.rst** after user's configurations.

### **Task 3**

**Upload** or **Update** (replace if existed) RST file to Github with authorization in auth.py.\
"Auth.py" is a python file that you have to generate yourself with the following structures:\
Auth.py\
&nbsp;&nbsp;   |__REPO_PATH: Path to your *Repository* starting with your *username*\
&nbsp;&nbsp;   |__token: Your Github token with enough permissions (delete, write, read)

Example:

```py
REPO_PATH  = 'path/to/my/github/repo'
token ='your_token_need_to_be_hidden'
```

We don't need **REPO_PATH** anymore because it is defined by **nlthanhcse/Bosch_CodeRace_Bibongde**

```python
repo = github_instance.get_repo('nlthanhcse/Bosch_CodeRace_Bibongde')
```

You can run the following command line to upload the current file in **output** folder or you can uncomment last line in **final.py** to run it sequently with Task 1 and Task 2.

```shell
python gitupload.py
```

## **Source files**

 **convert.py**, **final.py**, **requirements.txt**, **git_upload.py**, **globals.py**

## **Configuration files**

Includes **keys.conf**

### **keys.conf**

With defaults keys' values, users can modify it by defining a new section and other keys' values as you wish. Remember to load section's name in command line to apply new configurations.

### **values.conf**

Under **RST** section, users are allowed to config Json values to display in RST file. 

### **Features**

Task 1

- [ ] Array mapping
- [x] Attribute name and the same value
- [ ] Attribute name and customize value

Task 2

- [x] Heading, Information, Directive
- [x] Attribute value text
- [x] Sub-directive
- [x] Html (convert html to RST text)

Task 3

- [x] Push to GitHub
- [x] Overwrite
