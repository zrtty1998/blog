---
title: 31天JavaScript学习-第10天
reprint: false
date: 2022-03-03 16:13:09
updated: 2022-03-03 16:13:09
conver:
categories: 前端
tags:
  - JavaScript
---

# 函数表达式（二）——应用

<!--more-->

## 模仿块级作用域

JS中没有块级作用域的概念。使用匿名函数可以用来模仿块级作用域。

```js
(function(){
  // 块级作用域
})();
```

该代码定义并立即调用了一个匿名函数，将函数声明包含在一对圆括号中，表示它实际上是一个函数表达式。而紧随其后的另一对圆括号会立即调用这个函数。

## 私有变量

JS中没有私有成员的概念，所有对象属性都是公有的。但在任何函数中定义的变量，都可以认为是私有变量。如果在这个函数内部创建一个闭包，那么闭包通过自己的作用域链可以访问这些对象。就可以创建用于访问私有变量的公有方法。

把有权访问私有变量和私有函数的公有方法成为特权方法。有两种在对象上创建特权方法的方式。

**方式一：构造函数中定义特权方法**

```js
function Person(name) {
  this.getName = function() {
    return name;
  };

  this.setName = function(value) {
    name = value;
  };
}

var person = new Person('Jack');
console.log(person.getName()); // Jack
person.setName('Greg');
console.log(person.getName()); // Greg
```

这种定义特权方法有一个缺点，就是只能使用构造函数模式。而构造函数模式的缺点是针对每个实例都会创建同样一组新方法。

**方式二：静态私有变量**

通过在私有作用域中定义私有变量或函数，同样可以创建特权方法。

```js
(function () {
  // 私有变量和私有函数
  var name = '';

  Person = function (value) {
    name = value;
  };

  Person.prototype.getName = function () {
    return name;
  };
  Person.prototype.setName = function (value) {
    name = value;
  };
})();

var person = new Person('Jack');
console.log(person.getName());
person.setName('Greg');
console.log(person.getName());
```

