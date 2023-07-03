import requests
import schedule
import time
import json
import os

def job():
    urls = os.environ.get('URLS').split(',')

    # 遍历配置文件中的URL
    for url in urls:
        try:
            # 发送GET请求
            response = requests.get(url)
            print(f'Response from {url}: {response.status_code}')
        except requests.exceptions.RequestException as e:
            # 如果请求失败，打印错误信息
            print(f'Error requesting {url}: {e}')

def main():
    # 定时任务
    schedule.every(10).seconds.do(job)  # 每300秒执行一次，你可以根据需要调整

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
