---
title: 31天JavaScript学习-第17天.md
reprint: false
date: 2022-03-13 20:39:56
updated: 2022-03-13 20:39:56
conver:
categories: 前端
tags:
  - JavaScript
---

# Ajax（二）

<!--more-->

## JSON

JSON(JavaScrtipt Object Notation)：是ES的子集。

**JS中json字符串和js对象的互相转化**

```js
let jsObj = JSON.parse(ajax.responseText); // 将JSON字符串转化未js对象

let Obj = {
	name: 'zrtty',
	age: 20
};
let jsonStr = JSON.stringify(Obj);
```

## XMLHttpRequest2级

规范化的XMLHttpRequest。

### FormData

现代Web应用中表单数据的序列化是一项频繁使用的功能。为此定义了FormData类型。

```js
let data = new FormData();
data.append('name', 'zrtty'); // 分别接收两个参数：键和值
```

创建的FormData的实例，可以将它直接传给XHR的send()方法，不必明确地在XHR对象上设置请求头部。XHR对象能够识别传入的数据类型是FormData的实例，并配置适当的头部信息。

### 超时设定

XHR对象timeout属性，表示请求在等待响应多少毫秒后停止。

```js
xhr.open('get', 'timeout.php', true);
xhr.timeout = 1000;
xhr.ontimeout = function() {
	alert('request timeout');
};
xhr.send(null);
```

### overrideMimeType()方法

用于重写XHR响应的MIME类型。

## 跨域源资源共享

默认情况下，XHR对象只能访问与包含它的页面位于同一个域中的资源。同源指的是：**域名、协议、端口**完全相同。

CORS（Cross-Origin Resource Sharing，跨域源资源共享）定义了在必须访问跨源资源时，浏览器与服务器应该如何沟通。其背后思想就是使用自定义的HTTP头部让浏览器和服务器进行沟通，从而决定请求或响应是否成功。

### IE中的CORS

IE8中映入了XDR（XDomainRequest）类型。这个对象与XHR相似，单能实现安全可靠的跨域通信。

XDR对象的使用方法和XHR对象非常相似。也是创建一个实例，调用open()方法，再调用send()方法。但XDR对象的open()方法只接收两个参数：请求的类型和URL。所有的XDR请求都是异步执行的，请求返回后，会触发load事件，响应的数据也会保存在responseText属性中。

### 其他浏览器的CORS

其他浏览器无需编写额外代码即可触发这个行为，只要使用标准的XHR对象并在open()方法中传入绝对URL即可。

### 跨浏览器的CORS

不同浏览器对CORS的支持程度并不都一样。所有浏览器都支持简单的请求。检测XHR是否支持CORS的最简单方式，就是检查是否存在withCredentials属性，再结合检测XDomainRequest对象是否存在，就可以兼顾所有浏览器了。

## 其他跨域技术

### 图像Ping

### JSONP

JSONP市JSON with padding（填充式JSON或参数式JSON）的简写，是应用JSON的一种新方法。

JSONP是被包含在函数调用中的JSON，如

```js
callback({ 'name': 'zrtty'} );
```

JSONP由两部分组成：回调函数和数据。其本质是利用了`<script src=''></script>`标签具有可跨域的特性，由服务端返回一个预先定义好的JS函数的调用，并且将服务器数据以该函数参数的形式传递过来。此方法需要前后端配合完成。

html标签的src属性是支持跨域的，jsonp就是利用这个特性实现的跨域，但用到是script标签。

jsonp只能通过GET方式进行请求。

```js
  <script>
    function handleResponse(response) {
      console.log(response.ip);
    }
  </script>
  <script src="http://freegeoip.net/json/?callback=handleResponse"></script>
```

这个URL是在请求一个JSONP地理定位服务。这里指定的回调函数的名字叫handleResponse()。

**JQuery的JSONP**

```js
$('#btn').click(function () {
  $.ajax({
    url: 'http://freegeoip.net/json/?callback=handleResponse',
    dataType: 'jsonp',
    type: 'get',
    // jsonp: 'callback_name' // 传递给服务器的回调函数的毛宁子（默认callback)
    // jsonCallBack: 'responseHandler' // 自定义的函数名。默认为jQuery自动生成的随机函数名
    success: function (response) {
      console.log(response.ip);
    },
    error: function (err) {
      console.log(err);
    }
  });
});
```

