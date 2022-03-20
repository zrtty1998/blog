---
title: pip与conda换源
reprint: false
date: 2022-02-14 11:10:52
updated: 2022-02-14 11:10:52
conver:
categories: 环境搭建
tags:
  - pip
  - conda
---

# conda与pip换源汇总

<!--more-->

## conda

### linux

修改`~/.condarc`

```
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
ssl_verify: true
```



### windows

windows用户需先执行`conda config --set show_channel_urls yes`，生成`.condarc`文件，再进行修改

## pip

阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/

### linux

**临时换源：**

pip后加-i，指定pip源

**永久换源：**

修改`~/.pip/pip.conf`

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### windows

在user目录新建pip目录，路径为`C:\User\xx\pip\pip.ini`

```
[global]
timeout = 6000
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
```

