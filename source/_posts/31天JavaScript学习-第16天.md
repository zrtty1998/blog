---
title: 31天JavaScript学习-第16天
reprint: false
date: 2022-03-10 15:44:43
updated: 2022-03-10 15:44:43
conver:
categories: 前端
tags:
  - JavaScript
---

# Ajax（一）

<!--more-->

Ajax：Asynchronous JavaScript And XML（异步JavaScript和XML）。Ajax的核心是JS对象：XMLHttpRequest

即可以使用XHR对象取得新数据，然后再通过DOM将新数据插入到页面中。

## Ajax原理

一个完整的http请求需要的是：

- 请求的网址、请求的方法get/post
- 提交请求的内容数据、请求主体
- 接收响应回来的内容

对应的，发送Ajax请求的步骤：

1. 创建异步对象，即XMLHttpRequest对象
2. 使用open方法设置请求参数。`open(method, url, async)`
3. 发送请求：`send()`
4. 注册事件：注册`onreadystatechange`事件，状态改变时就会调用
5. 服务端响应，获取返回的数据

话不多说，手写一个Ajax：

```js
// 创建XMLHttpRequest对象
let xmlhttp = new XMLHttpRequest();

// 设置请求的参数。请求的方法、请求的url
// 调用open方法并不会真正发送请求，而只是启动一个请求以备发送
// 第三个参数true（异步）false（同步），默认true
xmlhttp.open('get', 'ajax.php', false);

// 发送请求
// send方法接收一个参数，即要作为请求主体发送的数据。如果不需要通过请求主体发送数据
// 则必须传入null。调用send()之后，请求就会被分派到服务器
xmlhttp.send(null);

// 注册事件
xmlhttp.onreadystatechange = function (){
  // 为了保证数据完整返回，一般判断两个值
  if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
    // 服务端响应
    console.log('数据返回成功' + JSON.stringify(xmlhttp.responseText));
  }
};
```

在收到响应后，响应的数据会自动填充XHR对象的属性：

- **responseText：**作为响应主体被返回的文本
- **responseXML：**如果响应的内容类型是"text/xml"或"application/xml"，这个属性中将保存包含响应数据的XML DOM文档。
- **status：**响应的HTTP状态
- **statusText：**HTTP状态的说明

**readyState属性**

多数情况下，我们还是要发送异步请求。此时可以检测XHR对象的readyState属性，该属性表示请求和响应过程中的当前活动阶段。这个属性的值如下：

- **0：**未初始化，尚未调用open()方法
- **1：**启动，已经调用open()方法，但尚未调用send()方法
- **2：**发送，已经调用send()方法，但尚未接收到响应
- **3：**接收，已经接收到部分响应数据
- **4：**完成，已经接收到全部的响应数据，已经可以在客户端使用了

每次readyState属性值发生变动，都会触发一次readystatechange事件。

## HTTP头部信息

每个HTTP请求和响应都会带有相应的头部信息：

| Head            | Explain                                         |
| --------------- | ----------------------------------------------- |
| Accept          | 浏览器能够处理的内容类型                        |
| Accept-Charset  | 浏览器能够显示的字符集                          |
| Accept-Encoding | 浏览器能处理的压缩编码                          |
| Accept-Language | 浏览器当前设置的语言                            |
| Connection      | 浏览器与服务器之间连接的类型                    |
| Cookie          | 当前页面设置的任何Cookie                        |
| Host            | 发出请求的页面所在域                            |
| Referer         | 发出请求的页面的URI（HTTP规范把referrer拼错了） |
| User-Agent      | 浏览器的用户代理字符串                          |

使用`setRequestHeader()`方法可以设置自定义的请求头部信息。接收两个参数：头部字段的名称和头部字段的值。在open()方法之后且调用send()方法之前使用。

## get请求

get请求将查询字符串参数追加到URL末尾，以便将信息发送给服务器。对于XHR对象，位于传入open()方法的URL末尾的查询字符串必须经过正确的编码。查询字符串中每个参数的名称和值都必须使用encodeURIComponent()进行编码，而且所有名-值对都必须由&分割：

```js
function addURLParam(url, name, value) {
  url += (url.indexOf("?") == -1 ? "?" : "&");
  url += encodeURIComponent(name) + "=" + encodeURIComponent(value);
  return url;
}

let url = 'example.php';
url = addURLParam(url, "name", "Nick");
xmlhttp.open("get", url, false);
```

## post请求

post请求通常用于向服务器发送应该被保存的数据。POST请求应该把数据作为请求的主体提交。

## 封装Ajax请求

```js
function myAjax(url, success, fail) {
  // 1、创建XMLHttpRequest对象
  let xmlhttp;
  if (window.XMLHttpRequest) {
    xmlhttp = new XMLHttpRequest();
  } else {
    xmlhttp = new ActiveXObject('Microsoft.XMLHTTP');
  }
  // 2、发送请求
  xmlhttp.open('GET', url, true);
  xmlhttp.send();
  // 3、服务器响应
  xmlhttp.onreadystatechange = function() {
    if (xmlhttp.readyState === 4 && xmlhttp.status ===200) {
      let obj = JSON.parse(xmlhttp.responseText);
      console.log('数据返回成功' + obj);
      success && success(xmlhttp.responseText);
    } else {
      fail && fail(new Error('接口请求失败'));
    }
  };
}

myAjax('a.json', (res) => {
  console.log(res);
});
```

实际开发中，经常会涉及接口请求之间的依赖：即需要上一个接口请求返回的数据，来发送本次请求。这种层层嵌套的代码，会导致**回调地狱**的问题，不利于后续的维护。ES6使用Promise来解决该问题。

## JQuery中的Ajax

```js
$.ajax({
  url: 'https://xxx.com/getUserInfo.php',
  data: 'name=fox&age=18',
  type: 'GET',
  success: function (argument) {
    console.log('success');
  },
  beforeSend: function (argument) { },
  error: function (argument) {
    console.log('error');
  }
});
```

