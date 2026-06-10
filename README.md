# Riftguessr

## Requirements

**Create a virtual environment**

```
python3 -m venv .venv
```

Note: you may need to install `python-venv` system-wide on default Python installations.

**Activate the virtual environment**

Linux and macOS
```
source .venv/bin/activate
```

Windows (PowerShell)
```
.venv/Scripts/Activate.ps1
```

**Install the dependencies**

```
pip install -r requirements.txt
```

Note: make sure to enable the virtual environment before installing the dependencies (otherwise you may install dependencies system-wide, which is not recommended).

## Usage

```
python3 riftguessr.py <level>
```

Difficulty can be set with `<level>` :
- beginner (3-5)
- intermediate (6-10)
- expert (11-15)