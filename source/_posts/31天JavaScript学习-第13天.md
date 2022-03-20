---
title: 31天JavaScript学习-第13天
reprint: false
date: 2022-03-06 16:48:28
updated: 2022-03-06 16:48:28
conver:
categories: 前端
tags:
  - JavaScript
---

# 事件

<!--more-->

JS与HTML之间的交互是通过**事件**实现的。

**事件的三要素：事件源、事件、事件驱动程序**。

## 事件流

事件流是描述从页面中接收事件的顺序。IE的事件流是**事件流冒泡**，Netscape的事件流是**事件捕获流**。

### 事件流冒泡

事件开始时由最具体的元素接收，然后逐级向上传播到较为不具体的节点（文档）。

```html
<!DOCTYPE html>
<head>
  <title>Document</title>
</head>
<body>
  <div id="myDiv">Click Me</div>
</body>
</html>
```

如果你点击了页面中的`<div>`元素。那么这个click事件会按照如下的顺序传播：

1. `<div>`
2. `<body>`
3. `<html>`
4. document

所有的现代浏览器都支持事件冒泡，Firfox、Chrome等会将事件一直冒泡到window对象。

### 事件捕获流

事件捕获流的顺序与事件冒泡流相反，不太具体的节点应该更早接收到事件。其用意时在事件达到预定目标之前捕获它。

### DOM事件流

**DOM2级事件**规定的事件流包括三个阶段：事件捕获阶段、处于目标阶段和事件冒泡阶段。

以前面的点击div元素为例。

1. 在事件捕获阶段，事件从document到`<html>`再到`<body>`就停止了。
2. 下一个阶段时”处于目标阶段”，事件在`<div>`上发生，并在事件处理中被看成冒泡阶段的一部分。
3. 冒泡阶段发生，事件又传播回文档。

## 事件处理程序

事件是用户或浏览器自身执行的某种动作。而响应某个事件的函数就叫做事件处理程序。

### HTML事件处理程序

```html
<input type='button' value='Click Me' onclick='alert('Clicked')' />
```

```html
<input type='button' value='Click Me' onclick='showMessage()' />
<script>
    function showMessage(){
      alert("hello world")
    }
 </script>
```

### DOM0级事件处理程序

```js
var btn = document.getElementById("myBtn");
btn.onclick = function() {
	alert("Clicked");
};
```

使用DOM0级方法指定的事件处理程序被认为是元素的方法。因此，这时候的事件处理程序是在元素内部的作用域中运行的。

缺点：不能同时对一个DOM绑定多个相同事件。

### DOM2级事件处理程序

- addEventListener()
- removeEventListener()

所有的DOM节点都包含这两个方法，并都接收三个参数：

- 要处理的事件名
- 作为事件处理程序的函数
- 一个布尔值：true，在捕获阶段调用事件处理程序；false，在冒泡阶段调用事件处理程序。

```js
var btn = document.getElementById("myBtn");
btn.addEventListener("click", function(){
    alert("this.id");
}, false);
btn.addEventListener("click", function(){
    alert("Hello world");
}, false);
```

DOM2级事件处理程序可以添加多个事件处理程序。

通过`addEventListener()`添加的事件处理程序只能通过`removeEventListener()`来移除；移除时传入的参数与添加处理程序时使用的参数相同。这也意味着由于上面例子中传入的是匿名函数，因此无法在移除时添加相同的参数。正确例子如下：

```js
var btn = document.getElementById("myBtn");
var handler = function(){
    alert("this.id");
};
btn.addEventListener("click", handler, false);
btn.removeEventListener("click", handler, false);
```

大多数情况下，都是将事件处理程序添加到事件流的冒泡阶段。

## 事件对象

当触发DOM上的某个事件时，会产生一个事件对象event。浏览器每次都会将这个事件event作为实参传进之前的响应函数。

```js
var btn = document.getElementById("myBtn");
btn.onclick = function(event) {
	alert(event.type);
};
btn.addEventListener("click", function(event){
    alert("event.type");
}, false);
```

## 事件类型

### UI事件

**load事件**

当页面完全加载完后（包括所有图像、JS文件、CSS文件等外部资源），就会触发window的load事件。

有两种定义onload事件处理程序的方式。

```js
EventUtil.addHandler(window, "load", function(event){
	alert("loaded");
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Document</title>
</head>
<body onload="alert('loaded')">
    
</body>
</html>
```

一般来说，在window上面发生的任何事件都可以在`<body>`元素中通过相应的特性来指定，因为在HTML中无法访问window元素。

在图像上也可以触发onload事件。

**unload事件**

当文档被完全卸载后触发，只要用户从一个页面切换到另一个页面，就会发生unload事件。

**resize事件**

当浏览器窗口被调整到一个新的高度或宽度时，就会触发resize事件。可以通过JS或`<body>`元素中的onresize特性来指定事件处理程序。

**scroll事件**

当浏览器窗口滚动时触发。

### 焦点事件

焦点事件会在页面元素获得或失去焦点时触发。有以下6个焦点事件：

- blur：在元素失去焦点时触发。这个事件不会冒泡。
- focus：在元素获得焦点时触发。这个事件不会冒泡。
- DOMFocusIn：在元素获得焦点时触发。只有Opera支持该事件。DOM3已弃用。
- DOMFocusOut：在元素失去焦点时触发。只有Opera支持该事件。DOM3已弃用。
- focusing：在元素失去焦点时触发。这个事件会冒泡。
- focusout：在元素获得焦点时触发。这个事件会冒泡。

## 事件委托

事件委托，就是把一个元素相应事件的函数委托到另一个元素。

例如有一个无序列表ul，列表之中有大量的`<a>`标签，当鼠标移到`<a>`标签上的时候，需要触发相应的处理事件。通常的写法是为每个`<a>`标签都绑定类似onMouseOver的事件监听。

```js
    window.onload = function(){
        var parentNode = document.getElementById("parent-list");
        var aNodes = parentNode.getElementByTagName("a");
        for(var i=0, l = aNodes.length; i < l; i++){

            aNodes[i].onclick = function() {
                console.log('我是超链接 a 的单击相应函数');
            }
        }
    }
```

但是这种做法过于消耗性能。**我们希望，只绑定一次事件，即可应用到多个元素上**，即使元素是后来添加的。

因此，比较好的方法就是把这个点击事件绑定到他的父层，也就是 `ul` 上，然后在执行事件函数的时候再去匹配判断目标元素。如下：

```html
<ul id="parent-list">
    <li><a href="javascript:;" class="my_link">超链接一</a></li>
    <li><a href="javascript:;" class="my_link">超链接二</a></li>
    <li><a href="javascript:;" class="my_link">超链接三</a></li>
</ul>

<script>
	window.onload = function(){
        // 获取父节点，并为它绑定click单击事件。 false 表示事件在冒泡阶段触发（默认）
        document.getElementById('parent-list').addEventListener('click', function(event){
            event = event || window.event;
            
             // e.target 表示：触发事件的对象
             //如果触发事件的对象是我们期望的元素，则执行否则不执行
            if (event.target && event.target.className == 'my_link') {
				console.log('我是ul的单击响应函数');
            }
        }, false);
    };
</script>
```

为父节点注册click事件，当子节点被点击时，click事件会向父节点冒泡。父节点捕获到事件后，通过判断`event.target`拿到被点击的子节点的相应信息，并做处理。
