# Skillshare video downloader in python

This script is exactly the same as @kallqvistI but with fixes and updates.

### Support your content creators, do NOT use this for piracy!

You will need a skillshare premium account to access premium content.
This script will not handle login for you.

1. Log-in to skillshare in your browser and open up the developer console.
(cmd-shift-c for chrome on mac)

2. Use a cookie manager browser extension and get your PHPSESSID cookie from the skillshare website.

3. Copy-paste PHPSESSID cookie into example script.

#### Example:
```
from downloader import Downloader

cookie = "PHPSESSID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/en/classes/Art-Fundamentals-in-One-Hour/189505397')

# or by class ID:
# dl.download_course_by_class_id(189505397)
```
