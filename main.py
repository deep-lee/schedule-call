import requests
import schedule
import time
import json
import os

def job():
    urls = os.environ.get('URLS')
    if urls is None:
        urls = "https://www.baidu.com"

    # 遍历配置文件中的URL
    for url in urls.split(','):
        try:
            # 发送GET请求
            response = requests.get(url)
            print(f'Response from {url}: {response.status_code}')
        except requests.exceptions.RequestException as e:
            # 如果请求失败，打印错误信息
            print(f'Error requesting {url}: {e}')

def main():
    # 定时任务
    interval_in_seconds = os.environ.get('INTERVAL_IN_SECONDS')

    if interval_in_seconds is None:
        interval_in_seconds = 60
    schedule.every(interval_in_seconds).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
