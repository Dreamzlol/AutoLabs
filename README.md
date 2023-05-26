AutoLabs

AutoLabs is a Python project that automates the registration process for ElevenLabs using Selenium. It provides the option to register with a random proxy from a proxy site or without using a proxy.
Features

    Automates the registration process for ElevenLabs
    Option to register with a random proxy or without using a proxy
    Generates a random password for each registration
    Uses TempMail to generate temporary email addresses for confirmation emails
    Retrieves the confirmation link from the confirmation email and visits it automatically
    Saves the registered email, password, and confirmation link to a file

Installation

    Clone the repository:

    bash

git clone https://github.com/Dreamzlol/AutoLabs.git

Navigate to the project directory:

bash

cd AutoLabs

Install the required dependencies:

    pip install -r requirements.txt

Usage

To register without using a proxy:

python elevenlabs.py

To register with a random proxy from the proxy site:

css

python elevenlabs.py --proxy

License

This project is licensed under the MIT License.
