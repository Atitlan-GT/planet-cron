# Planet cron for Lake Atitlan

[![Python: 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Atitlan-GT/model-data-etl/blob/master/LICENSE)
[![IMapApps: Development](https://img.shields.io/badge/IMapApps-Development-green)](https://imapapps.com)


Finds and adds the most current Planet data for Lake Atitlan to our system.

## Installation Requirements

### Required

- Atitlan-GT webmap-apps installed
- Python 3.x

### Recommended
Conda (To manage packages within the applications own environment).  If you choose to not use conda you will
have to manually install the package requirements listed in the environment.yml file.

### Environment
- Create the env

```commandline
conda env create -f environment.yml
```

Add a file named data.json in the base directory.  This file will hold a json object containing
the WEBMAP_APPS_URL for your application, and PLANET_KEY.  The format will be:

```json
{
  "WEBMAP_APPS_URL": "URL_TO_YOUR_DEPLOY_OF_WEBMAP_APPS/ajax.php",
  "PLANET_KEY": "YOUR_PLANET_KEY"
}
```


## Execute the application

You should be able to run with python updateplanet.py command.  
We recommend setting up a cron which updates as regularly as you
need it to. We have an example in cron.txt

### Authors

- [Billy Ashmall (IMapApps)](mailto:imapapps@gmail.com)

## License and Distribution

Copyright © 2021 UAH.

Model Data ETL for Lake Atitlan is distributed by UAH under the terms of the MIT License. See
[LICENSE](https://github.com/Atitlan-GT/model-data-etl/blob/master/LICENSE) in this
directory for more information.
