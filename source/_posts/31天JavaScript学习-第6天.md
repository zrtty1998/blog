---
title: 31天JavaScript学习-第6天
reprint: false
date: 2022-02-25 19:57:15
updated: 2022-02-25 19:57:15
conver:
categories: 前端
tags:
  - JavaScript
---

**day06-浅拷贝与深拷贝**

<!--more-->

由于引用类型变量名存在栈内存中，值存在堆内存中，因此深拷贝只针对较为复杂的object类型数据。

- **浅拷贝：**只拷贝最外面一层的数据；更深层次的对象，只拷贝引用
- **深拷贝：**拷贝多层数据，每一层级的数据都会拷贝

# 浅拷贝的实现方法

## for in（繁琐）

```js
var obj1 = {
  name: 'jack',
  age: 28,
  info: {
    desc: 'nice'
  }
};

const obj2 = {};
for (let key in obj1) {
  obj2[key] = obj1[key];
}
console.log('obj2:' + JSON.stringify(obj2));

obj1.age = 30;
console.log('obj2:' + JSON.stringify(obj2.age)); // obj2:28 修改了obj1的第一层属性，obj2没有随之更改

obj1.info.desc = 'good';
console.log('obj2:' + JSON.stringify(obj2.info.desc)); // obj2:"good" 修改了obj1的info.desc属性，obj2也随之更改，说明obj2对obj1的info复制是复制了其引用地址
```

上方代码中，用 for in 做拷贝时，只能做到浅拷贝。也就是说，在 obj2 中， name 和 age 这两个属性会单独存放在新的内存地址中，和 obj1 没有关系。但是，`obj2.info` 属性，跟 `obj1.info`属性，**它俩指向的是同一个堆内存地址**。所以，当我修改 `obj1.info` 里的值之后，`obj2.info`的值也会被修改。

## Object.assgin()（推荐）

ES6提供了新的语法糖，通过`Object.assgin()`可以快速实现**浅拷贝**。将 obj1 的值追加到 obj2 中。如果对象里的属性名相同，会被**覆盖**。

```js
// 语法1
obj2 = Object.assgin(obj2, obj1);

// 语法2
Object.assign(目标对象, 源对象1, 源对象2...);
```

如

```js
var myObj = {
  name: 'jack',
  age: 28,
  info: {
    desc: 'nice'
  }
};

// 写法1
const obj1 = {};
Object.assign(obj1, myObj);

// 写法2
const obj2 = Object.assign({}, myObj);

// 写法3
const obj31 = {};
const obj32 = Object.assign(obj31, myObj);

// 将myObj、myObj2内容赋值给obj4
let myObj2 = {
  city: 'xiamen',
  age: 32
}

const obj4 = Object.assign({}, myObj, myObj2);
```

# 深拷贝的实现方式

## for in递归实现

```js
var obj1 = {
  name: 'jack',
  age: 28,
  info: {
    desc: 'nice'
  }
};

var obj2 = {};

function deepCopy(newObj, oldObj) {
  for (let key in oldObj) {
    // 获取属性值
    let item = oldObj[key]
    // 判断这个属性值是否是数组
    if (item instanceof Array) {
      newObj[key] = [];
      deepCopy(newObj[key], item);
    } else if (item instanceof Object) { // 判断这个属性值是否为对象
      newObj[key] = {};
      deepCopy(newObj[key], item);
    } else { // 简单数据类型，直接赋值
      newObj[key] = item;
    }
  }
}

deepCopy(obj2, obj1);
console.log(obj2);
obj1.info.desc = 'github';
console.log(obj2);

```

