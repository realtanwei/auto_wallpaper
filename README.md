## Summary

* 获取https://cn.bing.com/首页背景
* 下载图片
* 设置背景

## Install Dependencies

* pip3 & python3 is required
* pip3 install -r requirements.txt

## Ubuntu 定时任务:

* chmox u+x auto_wallpaper.py
* crontab -e
* 添加cron表达式(eg: 0 9 * * * /usr/bin/python3 ${script_dir}/auto_wallpaper.py)
* sudo service cron restart
