# Planet cron for Lake Atitlan

[![Python: 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/Atitlan-GT/model-data-etl/blob/master/LICENSE)
[![IMapApps: Development](https://img.shields.io/badge/IMapApps-Development-green)](https://imapapps.com)

[Currently in Development]

Finds and adds the most current Planet data for Lake Atitlan to our system.

## Installation Requirements

### Required

- Atitlan-GT webmap-apps installed
- Python 3.x

## Setup

- Open updateplanet.py and enter your information in the two variables:
  -- ajax_url (points to the ajax file in webmap-apps)
  -- planet_key (your Planet key)

## Execute the application

You should be able to run with python updateplanet.py command.  
We recommend setting up a cron which updates as regularly as you
need it to. We have an example in cron.txt

## License and Distribution

Copyright © 2021 UAH.

Model Data ETL for Lake Atitlan is distributed by UAH under the terms of the MIT License. See
[LICENSE](https://github.com/Atitlan-GT/model-data-etl/blob/master/LICENSE) in this
directory for more information.
