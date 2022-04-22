---
title: 31天JavaScript学习-第22天
reprint: false
date: 2022-03-26 15:56:07
updated: 2022-03-26 15:56:07
conver:
categories: 前端
tags:
  - nodejs
---

# 模块化（一）：CommonJS

<!--more-->

## 模块化规范

- **服务器端规范：**CommonJS，Node.js使用的模块化规范
- **浏览器端规范：**
  - AMD规范，是RequireJS在推广过程中对模块化定义的规范化产出。
  - CMD规范，是SeaJS在推广过程中对模块化定义的规范化产出，出自淘宝。

## CommonJS基本语法

CommonJS规定：每个文件都可以当作一个模块，每个模块内部内部，module变量代表当前模块。这个变量是一个对象，它的exports属性（即module.exports）是对外的接口对象。加载某个模块，其实是加载该模块的module.exports对象。

在服务器端，模块的加载时运行时同步加载的；在浏览器端，模块需要提前编译打包。

### 模块的暴露与引入

Node.js中，每个模块都有一个exports接口对象，我们可以把公共的变量、方法挂载到这个接口对象中，其他模块通过引入该接口对象以实现引入。

**暴露模块方式一：exports**

exports对象用来导出当前模块的公共方法或属性。其他模块通过require函数调用时，得到的就是当前模块的exports对象。

> 注意关键字是`exports`，并非ES6中的`export/import`导出导入模块规范。

```js
const name = 'zrtty';
const foo = function (value) {
  return value * 2;
};

exports.name = name;
exports.foo = foo;
```

**注意：**导出模块时优先使用module.exports。因为Node为每个模块提供一个exports变量，该变量指向module.exports。等同于每个模块头部有一句`const exports = module.exports;`。

**暴露模块方式二：module.exports**

module.exports用来导出一个默认对象，没有指定对象名。

```js
const name = 'zrtty';
const foo = function (value) {
  return value * 2;
};

module.exports = name;
module.exports.foo = foo;
```

**注：**Node中每个模块的最后，都会执行`return module.exports`

**引入模块：require**

require用来在一个模块中引入另外一个模块。传入模块名，返回模块导出的对象。

```js
const module1 = require('module name');
```

其中引入的模块名的写法：

- 内置模块则引入**包名**
- 下载的第三方模块则引入**包名**
- 自定义模块则引入**文件路径**，后缀.js可以省略

**注：**一个模块中的JS代码仅在模块第一次使用时执行一次，并在使用过程中初始化，然后被缓存起来，便于后续继续使用。

```js
// array.js
var a = 1;

function add() {
  return ++a;
}

exports.add = add;
```

```js
// main.js
const myModule1 = require('./array');
const myModule2 = require('./array');

console.log(myModule1.add()); // 2
console.log(myModule2.add()); // 3
```

可以看到，array.js被引用两次，但只初始化了一次。

