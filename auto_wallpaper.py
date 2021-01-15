import requests
import datetime
import subprocess

## bing service endpoint
BASE_URL        =   "https://www.bing.com"
## wallpaper dir
WALLPAPER_DIR   =   "/home/yd/Pictures/wallpaper/"


def main():
    today = datetime.date.today()
    formatted_today = today.strftime("%Y%m%d")
    filename = formatted_today + ".jpg"
    filepath = WALLPAPER_DIR + filename
    download_image(filepath)
    runcmd(["gsettings set org.gnome.desktop.background picture-uri file:" + filepath])

def runcmd(command):
    ret = subprocess.run(command, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
    if ret.returncode == 0:
        print("success:",ret)
    else:
        print("error:",ret)

def download_image(filepath):
    url = get_wallpaper()
    r = requests.get(BASE_URL + url)
    with open(filepath, "wb") as image:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                image.write(chunk)

def get_wallpaper():
    try:
        r = requests.get(BASE_URL + "/HPImageArchive.aspx?format=js&idx=0&n=1")
        data = r.json()
        url = data['images'][0]['url']
        return url
    except BaseException as e:
        print(e)

if __name__ == "__main__":
    main()