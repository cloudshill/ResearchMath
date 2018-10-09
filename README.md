[comment]: <> (├── HEAD)
[comment]: <> (│ ├── pre-push.sample)
[comment]: <> (│ └── pack)
[comment]: <> (└── refs)
# File Structure
The file structure of the project is separated as the structure below:
```
ResearchMath
├── code
├── docs
├── tools
├── results
└── README.md

```
Where the main folders are set as:
- `build/`
- `code/`
- `docs/`
- `results/`
- `tools/`

## `code/`
This is where all of the codes are stored. They are separated different subprojects. They are thought to be linked to the other folders (i.e. `results/`, `docs/`)

For Python scripts, in order to check and see if their respective folders exist and to create a directory if it doesn't exist:

```python
import os                                   # Import os library
path = os.getcwd()                          # Get the current path (e.g. EyeTracking/code/AA)
parent_path = os.path.dirname(path)         # Get the parent path (e.g. EyeTracking/code)
folder_name = os.path.basename(path)        # Get the folder name (e.g. AA)
access_rights = 0o755                       # Access rights to 755 (i.e. -rwxr-xr-x | default is 777)
results_dir = '../../results/'+folder_name  # Set a destination (e.g. '../../results/AA')

if not os.path.isdir(results_dir):          # If the directory doesn't exist
    os.mkdir(results_dir,access_rights)     #   Create the directory
```

## `docs/`
This is where the documentation files for some of the subprojects will be

##`results/`
This is where all of the results are stored. The folders in this directory are equivalent to the subfolders in `code/`, which is where the source code is located, and all of their results are stored in their respective folders in `results/`

## `tools/`
This is where the toolboxes will be located, such as `NicksToolbox.py`. In order to import Python files from this folder, one may include

```python
import sys; sys.path.insert(0,'../../tools/')
import NicksToolbox as NS
```

# Subprojects
