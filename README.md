# chromedriver-autoinstaller-max

chromedriver-autoinstaller-max was forked from the original [python-chromedriver-autoinstaller](https://github.com/yeongbin-jo/python-chromedriver-autoinstaller) repository. 


## Installation

```bash
pip install chromedriver-autoinstaller-max
```

## Usage
Just type `import chromedriver_autoinstaller_max` in the module you want to use chromedriver.

## Example
```
from selenium import webdriver
import chromedriver_autoinstaller_max


chromedriver_autoinstaller_max.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
```

## Authors & Contributors

- CHIDA <[iam.yeongbin.jo@gmail.com](mailto:iam.yeongbin.jo@gmail.com)>
