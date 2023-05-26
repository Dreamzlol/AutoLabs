# AutoLabs

This is a Python script for generating accounts on ElevenLabs. It uses Selenium for automated registration and TempMail for temporary email generation. Optionally, you can specify a proxy for registration.

## Features

- Automated registration on ElevenLabs
- Random password generation
- Optional proxy support
- Confirmation email verification
- Saving account details to a file

## Requirements

- Python 3.6 or higher
- Install the required packages using the following command:

```shell
pip install -r requirements.txt
```

## Usage

Clone the repository:

```shell

git clone https://github.com/Dreamzlol/AutoLabs.git
```
Navigate to the project directory:

```shell
cd AutoLabs
```
Install the required packages:

```shell
pip install -r requirements.txt
```
Run the script without a proxy:

```shell
python elevenlabs.py
```

Run the script with a random proxy:

```shell
python elevenlabs.py --proxy
```

This project is licensed under the MIT License. See the LICENSE file for details.
