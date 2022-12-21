from downloader import Downloader

# use cookie manager and find PHPSESSID and replace xxxx only
cookie = "PHPSESSID=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

dl = Downloader(cookie=cookie)

# download by class URL:
dl.download_course_by_url('https://www.skillshare.com/en/classes/Art-Fundamentals-in-One-Hour/189505397')

# or by class ID:
# dl.download_course_by_class_id(189505397)
