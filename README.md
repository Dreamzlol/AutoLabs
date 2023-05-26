# AutoLabs

This is a Python script to automate the creation of accounts on the ElevenLabs website.

### Features

*   Generates a temporary email address using the TempMail API.
*   Uses a randomly generated password for the new account.
*   Optionally uses a proxy server for the connection, which is selected randomly from a list of available proxies.
*   Navigates to the ElevenLabs sign-up page, fills in the necessary details, and submits the form.
*   Waits for a confirmation email to be sent to the temporary email address, then clicks on the confirmation link.
*   Saves the email address, password, and confirmation link to a text file.

### Requirements

This script requires Python 3.7+ and the following Python packages, which are listed in the `requirements.txt` file:

```makefile
argparse==1.4.0
requests==2.26.0
beautifulsoup4==4.10.0
selenium==3.141.0
TempMail==1.2.3
time==1.0
re==2.2.1
random==1.0.1
string==1.0.0
tqdm==4.62.2
```

To install these packages, use pip:

`pip install -r requirements.txt`

### Usage

1.  Clone the repository.
2.  Install the required Python packages.
3.  Update the path to the Chrome driver in the script (`driver_path` variable).
4.  Run the script with or without the `--proxy` argument to use a proxy server.

```css
python AutoLabs.py --proxy
```

### Note

This script uses the Chrome driver for Selenium. You need to have the Chrome driver installed on your system and the path to the driver must be specified in the script. You can download the Chrome driver from the [Chrome driver download page](https://chromedriver.chromium.org/downloads). Be sure to download the version that corresponds to your installed version of Chrome.

The `driver_path` variable in the script should be updated with the path to your Chrome driver. For example:

```python
driver_path = "/path/to/your/chromedriver"
```

### Disclaimer

This script is for educational purposes only. Use it responsibly.