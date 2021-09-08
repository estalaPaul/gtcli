# GTCLI

![GTCLI Logo](./logo.png)

Very basic command line interface for Google Tasks. Allows you to see, add, rename and delete your Tasks Lists; as well as see, add, update, complete and delete your Tasks.

## Table of contents

* [Installation](#installation)
* [Usage](#usage)
* [Disclaimer](#disclaimer)

## Installation

To install this script you first must install the Google Python Library for the Google Tasks API. For this we use pip and run the following command.

```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

Then you must set up the Google Authentication using OAuth 2.0. To do this, you can follow this [guide](https://developers.google.com/identity/protocols/OAuth2). 
After obtaining OAuth 2.0 credentials from the Google API Console, you must download the corresponding JSON file. That file must be renamed _credentials.json_ and placed in a secure directory. The same directory will be used to store the pickle file where your user access and refresh tokens are stored.

After obtaining that file and storing it in a safe directory, you must export a enviroment variable pointing to that directory, using the following command:

```
export GTCLI_RESOURCES_DIR="/path/to/safe/directory/"
```

Then lastly, we can clone this repository and run the gtcli.py file to get started. 

## Usage

Using the script is very simple. You just run the gtcli.py file with the object to modify (Task or Task List), a flag to indicate how you want to modify said object and if it is necessary, extra information needed for that operation. Here are a couple examples.

### Add a Task List

```
./gtcli.py tl -a [TITLE]
```

### Add a Task 

```
./gtcli.py t -a [TASKLIST] [TITLE] optional -n [NOTES]
```

For further documentation use --help. 

```
./gtcli.py --help
```

## Disclaimer

This is meant for personal use only and is alpha level code. It, in no way, is ready for production use. 
