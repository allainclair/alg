## Upwork Scanner

## Instructions to run the app

I used MaCOS Catalina 10.15.7, Python 3.9, and
[Pipenv](https://pypi.org/project/pipenv/) to manage virtual environments and
packages. First, we need to set up a "Safari driver" used in [Selenium](https://selenium-python.readthedocs.io/) to interact
to interact with the browser.

Link for a video demo of the app: [https://youtu.be/mBTEi7t2RW8](https://youtu.be/mBTEi7t2RW8)

### 1. Safari driver for Selenium

* We can follow
  [https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
  in the section *Running the Example in Safari* to enable the Safari driver.
  
* You probably do not need to download anything if you are at a MacOS. Just follow:

  * Ensure that the Develop menu is available. It can be turned on by opening
    Safari preferences (Safari > Preferences in the menu bar), going to the
    Advanced tab, and ensuring that the Show Develop menu in the menu bar checkbox is checked.
    
  * Enable Remote Automation in the Develop menu. This is toggled via
    Develop > Allow Remote Automation in the menu bar.

  * Authorize safari driver to launch the webdriver service, which hosts the
    local webserver. To permit this, run /usr/bin/safaridriver once manually
    and complete the authentication prompt.

  * You will probably need to allow the driver in *System Preferences* >
    *Security & Privacy* > *General* and check *Allow apps downloaded from App
    Store and identified developers*. Without these steps, the application won't work.
  
### 2. Pipenv

[Pipenv](https://pypi.org/project/pipenv/) is necessary to run the app.

* `pip install pipenv` installs the Pipenv.
* A binary `pipenv` will be available.

### 3. Run tests and application

* After installing Pipenv, you must use a terminal to go into `argyle/` directory.
  
* Inside the `argyle/` directory you can run `./conf-run.sh` which will run:

  ```
  pipenv install --dev  # Install dependencies from Pipfile
  pipenv run pytest tests/  # Run some unit tests from tests/ 
  pipenv run python sync_main.py  # Run the main scanner application
  ```
  
  You also can run each command in the terminal.

* If you want to rerun the main app: `pipenv run python sync_main.py`

### 4. Output

There are two output files pointed in `const.py`:
```
JSON_BASIC_PROFILE_FILE_PATH = 'profile_basic.json'
JSON_FULL_PROFILE_FILE_PATH = 'profile_full.json'
```
We also do some logs to the `stdio`. The JSON -> object using `pydantic` was 
just logged in the `stdio`.

`geckodriver.log` is auto-created by Selenium.

## Troubleshooting

If Safari does not launch and we get time out exception. Try to forced quit the safari
instances in the *Activity Monitor*.

Sometimes upwork send captchas to be filled. We have to bypass them manually.
I didn't experience this with Safari Browser.

## Failed tries

### First try using Python Requests to log in to Upwork

When trying to use only Python Requests Library to log in to upwork, it didn't
perform well. I tried to analyze the [Chrome Dev Tool](https://developers.google.com/web/tools/chrome-devtools)
network, and I saw that Upwork seems to have some tools to prevent automation, like
iovation ([https://www.iovation.com/](https://www.iovation.com/)). A hash code is
sent to the server whenever we try to submit the login form.

Even using Selenium, the Chrome driver didn't work. Firefox worked sometimes.
I had to use the Safari driver to be more stable. But we have some performance
problems with Safari. We can not have more than one driver running.
If we had more, we could speed up gathering information by running multiple
drivers on different pages.

### Python AsyncIO with Safari

We could create more drivers (instances) for Safari to speed up our scanning,
but according to some web researches, Safari does not support it yet. This way,
we only have a driver each time. I tried to use Firefox and Chrome drivers,
but I had issues with captchas and some Upwork site errors due to the automation.

We could cut the UI from Safari as well, but the same issue I researched,
we can not do this with Safari.

## Future improvements

* We can research AsyncIO selenium
  [https://pypi.org/project/aioselenium/](https://pypi.org/project/aioselenium/) to
  try to improve performance. This way, we can use Python AsyncIO.

* Dig more in Selenium, its drivers (Firefox and Chrome), and Python Async/IO to improve performance.

* I tried to schedule the application to run every X times using
  [cron](https://en.wikipedia.org/wiki/Cron). But we have problems with Safari
  when doing this. Safari needs the UI to run, and it seems that cron has
  issues with running Safari's UI.

* "Potentially, hundreds or thousands of scanning routines can happen concurrently":
  Due to the single Safari driver, I decided not to create many threads
  (tasks/coroutines like asyncio).

We could try [https://scrapy.org/](https://scrapy.org/) framework.

