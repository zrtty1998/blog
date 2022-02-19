---
title: linux关于压缩命令
reprint: false
date: 2022-02-19 15:24:49
updated: 2022-02-19 15:24:49
conver:
categories: linux
tags:
  - linux
---

Linux的压缩一直没有弄清楚，在这里系统整理一遍。

<!--more-->

# Linux中常用压缩格式

linux常见压缩包以tar.xx格式存在，其中tar是一种打包格式，而后面的gz、bz2等才是压缩方式。

## tar.gz

**压缩：**`tar -zcvf filename.tar.gz [目标文件]`

c:	**c**reate	创建新归档

**解压：**`tar -zxvf filename.tar.gz`

其中zxvf含义分别如下

z: 　　g**z**ip  　　　　　　　   压缩格式

x: 　　e**x**tract　　　　　　　　  解压

v:　　 **v**erbose　　　　　　　　详细信息

f: 　　**f**ile(file=archieve)　　　　文件

## tar.bz2

**压缩：**`tar -jcvf filename.tar.bz2 [目标文件]`

**解压：**`tar -jxvf filename.tar.bz2`

j: 　bzip2　　　　　　　　　 压缩格式

其它选项和tar.gz解压含义相同

## tar.xz

**压缩：**`tar -Jcvf filename.tar.bz2 [目标文件]`

**解压：**`tar -Jxvf filename.tar.xz`

注意J大写

## tar.Z

**压缩：**`tar -Zcvf filename.tar.bz2 [目标文件]`

**解压：**`tar -Zxvf filename.tar.xz`

注意Z大写

## 附

**事实上, 从1.15版本开始tar就可以自动识别压缩的格式,故不需人为区分压缩格式就能正确解压**

```
tar -xvf filename.tar.gz
tar -xvf filename.tar.bz2
tar -xvf filename.tar.xz
tar -xvf filename.tar.Z
```

## zip

zip包使用zip/unzip命令进行处理。

**压缩：**`zip [目标目录] [待压缩目录]`

**解压：**`unzip [待解压文件] -d [目标目录]`
