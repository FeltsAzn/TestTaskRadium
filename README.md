# TestTaskRadium

## Before running
Python version 3.10+

Install dependencies from requirements.txt file 
```bash
(venv)ubun: ~$ pip -r requirements.txt
```

## Start script

To start script run ***run.py*** file

```bash
(venv)ubun: ~$ python3 run.py
```
After starting choose download mode for script:
```bash
Download mode:
- Download archive(1)
- Download recursive(2)
- Quite(q)
Choice: 
```

1. Download archive - will download repository like archive, extract it and calculate hash
sums
2. Download recursive - will download repository recursive, before 
downloading searching repository, script will to find file download links and on this moment will downloading in another process


## Downloaded data

You can find downloaded repository in ***repository*** directory:
```
|-nitpick
    |-all.toml
    .....
    
|-repository
    |-project-configuration (downloaded repo)
    |- hash_sum.json
|-src
|-tests
....
```

In ***hash_sum.json*** you can find hash sum for each file

## Tests settings

Interpreter settings:
- Script path: ~TestTaskRadium/tests
- Work path: ~TestTaskRadium/tests

Run tests in IDE (recomemend)
