---
title: 31天JavaScript学习-第11天
reprint: false
date: 2022-03-04 16:04:08
updated: 2022-03-04 16:04:08
conver:
categories: 前端
tags:
  - JavaScript
---

# BOM和客户端检测

<!--more-->

## BOM

**BOM（Browser Object Model，浏览器对象模型）**，BOM可以操作浏览器部分功能的API。

**常见的BOM对象**

- **Window：**代表整个浏览器的窗口，同时 window 也是网页中的全局对象。
- **Navigator：**代表当前浏览器的信息，通过该对象可以识别不同的浏览器。
- **Location**：代表当前浏览器的地址栏信息，通过 Location 可以获取地址栏信息，或者操作浏览器跳转页面。
- **History：**代表浏览器的历史记录，通过该对象可以操作浏览器的历史记录。由于隐私原因，该对象不能获取到具体的历史记录，只能操作浏览器向前或向后翻页，而且该操作只在当次访问时有效。
- **Screen：**代表用户的屏幕信息，通过该对象可以获取用户的显示器的相关信息。

**注：**这些 BOM 对象都是作为 window 对象的属性保存的，可以通过window对象来使用，也可以直接使用。比如说，我可以使用 `window.location.href`，也可以直接使用 `location.href`，二者是等价的。

### window对象

在浏览器中，window对象有两种角色，它既是JS访问浏览器窗口的一个接口，又是ES规定的Global对象。

如果页面中包含框架`<frame>`，则每个框架都有自己的window对象，并保存在frames集合中。每个window对象都有一个name属性，其中包含框架名称。

**window对象常用的方法**

| 方法            | 描述                |
| --------------- | ------------------- |
| window.moveTo   | 移动窗口到x, y      |
| window.resizeTo | 调整窗口到w, h      |
| window.open     | 导航到一个特定的url |
| alert()         | 弹出警告            |
| confirm()       | 弹出带确认的警告    |
| prompt()        | 弹出输入提示框      |

### navigator对象

window.navigator 的一些属性可以获取客户端的一些信息。

- userAgent：系统，浏览器)
- platform：浏览器支持的系统，win/mac/linux

### location对象

`window.location`可以简写成location。location相当于浏览器地址栏，可以将url解析成独立的片段。

**location对象的属性**

- **href**：跳转
- hash 返回url中#后面的内容，包含#
- host 主机名，包括端口
- hostname 主机名
- pathname url中的路径部分
- protocol 协议 一般是http、https
- search 查询字符串

**location对象的方法**

- location.assign()：改变浏览器地址栏的地址，并记录到历史中

设置location.href 就会调用assign()。一般使用location.href 进行页面之间的跳转。

- location.replace()：替换浏览器地址栏的地址，不会记录到历史中
- location.reload()：重新加载

## 客户端检测

