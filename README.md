# AutoLabs

The AutoLabs is a Python script that automates the registration process on the Eleven Labs platform. It creates temporary email addresses, generates random passwords, and registers user accounts, verify account. The script provides the option to use a random proxy from a proxy site for added anonymity.

## Features

- Automated registration on the Eleven Labs platform
- Generates random passwords for user accounts
- Uses temporary email addresses for registration confirmation
- Supports the use of a random proxy from a proxy site (optional)

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- tqdm

## Usage

1. Install the required dependencies: pip install selenium beautifulsoup4 requests tqdm

2. Download the script `elevenlabs.py`.

3. Run the script with the following command: python elevenlabs.py [--proxy]

- Use the `--proxy` option to enable the use of a random proxy from a proxy site.

4. Follow the prompts and wait for the script to complete the registration process.

## Configuration

- Make sure to set the correct path to the Chrome driver (`driver_path` variable) in the script.

## License

This project is licensed under the [MIT License](LICENSE).
