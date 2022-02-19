---
title: 31天Javascript学习-第1天
reprint: false
date: 2022-02-19 19:54:00
updated: 2022-02-19 19:54:00
conver:
categories: 前端
tags:
  - Javascript
---

**day01-JS的基本语法和数据类型**

<!--more-->

# Javascript的特点

## 解释性语言

**解释型语言**的意思是：程序执行之前，不需要事先被翻译为机器码；而是在运行时，边翻译边执行（翻译一行，执行一行）。

## 单线程

Javascript作为浏览器脚本语言，主要用途是与用户互动、操作DOM等，这决定了它只能是单线程。

单线程就意味着，所有任务需要排队，前一个任务结束，才会执行后一个任务。如果前一个任务耗时很长，后一个任务就不得不一直等着。但js 引擎执行异步代码而不用等待，是因有为有 消息队列和事件循环。

NodeJS是单线程异步非阻塞模式，只有js执行是单线程，I/O交给libuv，是其他线程。[nodejs真的是单线程吗？ - 小小鸟儿！ - 博客园 (cnblogs.com)](https://www.cnblogs.com/wxmdevelop/p/10234556.html)

# Javascript的基本语法

## HTML对JS的三种引用方式

**方式1：行内式**

```html
<input type="button" value="点我点我" onclick="alert('hello world')" />
```

**方式2：内嵌式**

使用<script>元素，只需指定type属性

```html
<script type="text/javascript">
            // 在这里写 js 代码
            alert('hello world');
            console.log('hello world');
</script>
```

**方式3：外链式**

使用<script>元素，需指定src属性

```html
<script src="utils.js"></script>
```

JS代码写在<body>中，准确来说是在页面标签元素后，body结束标签前。

## 区分大小写

## 标识符

标识符指变量、函数、属性的名字，或者函数的参数。

- 标识符第一个字符必须是一个字母、下划线或$
- 其他字符可以是字母、下划线、$或数字

按照惯例，ECMAScript标识符采用驼峰大小写格式，第一个字母小写，剩下每个单词的首字母大写。

## 严格模式

在js代码顶部添加`"use strict";`

# 变量

JS的变量是松散类型的，不需要指定变量类型。如`var message;`使用var声明的变量作用域为该语句所在的函数内，存在变量提升现象。

ES6新增关键字let。使用let声明的变量作用域为该语句所在的代码块内，不存在变量提升。且let不允许在相同的作用域内，重复声明同一个变量。

# 数据类型

共有5种简单数据类型：Undefined、Null、Boolean、Number、String

1种复杂数据类型Object，Object本质由一组无序的键值对组成的。

## typeof操作符

使用typeof操作符可返回变量的数据类型

注意：typeof是一个操作符而不是函数，因此可以使用圆括号也可以不使用

## 简单（基本）数据类型

### Undefined

Undefined类型只有一个值，即特殊的undefined。

对未初始化的变量执行typeof会返回undefined，而对未声明的变量执行typeof同样返回undefined

```js
var message;
alert(typeof message); // 'undefined'
alert(typeof age); // 'undefined'
```

因此，保持变量显式的初始化是一个良好的编码习惯。

### Null

Null类型只有一个值，即特殊的null。null值表示一个空对象指针，正因此使用typeof检测null值时会返回'object'类型。

如果定义的变量在将来用于保存对象，最好将该变量初始化为null。实际上，undefined值是派生自null值的，因此`null == undefined`返回值是true。

### Boolean

Boolean类型有两个值，true和false。各种数据类型与Boolean类型的转换如下

| 数据类型  | 转换为true的值               | 转换为false的值 |
| --------- | ---------------------------- | --------------- |
| Boolean   | true                         | false           |
| String    | 任何非空字符串               | ""（空字符串）  |
| Number    | 任何非零数字值（包括无穷大） | 0和Nan          |
| Object    | 任何对象                     | null            |
| Undefined | n/a(N/A)                     | undefined       |

### Number

Number类型用来表示整数和浮点数值。

#### 整数

除十进制外，整数还可以以八进制和十六进制的字面值来表示

```
var octalNum1 = 070; // 八进制56
var octalNum2 = 079; // 无效的八进制，解析为79
var hexNum1 = 0xA; // 十六进制的10
var hexNum2 = 0x2f; // 十六进制的31
```

#### 浮点数

JS浮点数值的最高精度是17位小数。

JS会将某些浮点数值转换为整数值，如1.0，1.。

对于极大极小值，可以用e表示法，如

```js
var floatNum = 3.124e7;
```

#### Nan

Nan（Not a Number）是一个特殊的数值。

- 任何涉及Nan的操作都会返回Nan
- Nan和任何值都不相等

#### 数值转换

Number()、parseInt()、parseFloat()

### String

## Object

