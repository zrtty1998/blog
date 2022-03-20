---
title: 31天JavaScript学习-第8天
reprint: false
date: 2022-02-28 19:32:32
updated: 2022-02-28 19:32:32
conver:
categories: 前端
tags:
  - JavaScript
---

# 面向对象（二）——继承

<!--more-->

在众多OO语言中支持两种继承方式：接口继承和实现继承。接口继承只继承方法签名，而实现继承则继承实际的方法。由于JS函数没有签名，无法实现接口继承，只能支持实现继承。

## 原型链

### 原型链实现继承

ES将原型链作为实现继承的主要方法。其基本思想是：利用原型让一个引用类型继承另一个引用类型的属性和方法。

每个构造函数都有一个由prototype属性指向的原型对象，原型对象包含一个指向构造函数的指针constructor，而实例都包含一个指向原型的内部指针[[prototype]]。

实现原型链有一种基本模式，代码如下：

```js
function SuperType() {
  this.property = true;
}

SuperType.prototype.getSuperValue = function() {
  return this.property;
};

function SubType(){
  this.subproperty = false;
}

SubType.prototype = new SuperType();

SubType.prototype.getSubValue = function() {
  return this.subproperty;
};

var instance = new SubType();
console.log(instance.getSuperValue());
```

这段代码的原型链图如下所示：

![image-20220228210259817](31天JavaScript学习-第8天/image-20220228210259817.png)

由于SubType的原型等于了SuperType的实例对象，等价于SubType的原型指向SuperType的原型。SubType继承了SuperType，而继承是通过创建SuperType的实例，并将该实例附给SubType的原型实现的。换句话说，原来存在SupeType的实例中的属性和方法，现在也存在于SubType的原型中了。

**别忘了默认的原型**

所有引用类型默认都继承了Object，而这个继承也是通过原型链实现的。

![image-20220228211923561](31天JavaScript学习-第8天/image-20220228211923561.png)

**确定原型和实例的关系**

- instanceof：实例与原型链中出现过的构造函数，结果就会返回true
- isPrototypeOf：原型链中出现过的原型，都是该原型链所派生的实例的原型

### 原型链的问题

使用原型链实现继承最大的问题就是包含引用类型值的原型。

```js
function SuperType() {
  this.color = ['red', 'green'];
}

function SubType() {
}

SubType.prototype = new SuperType();

var instance1 = new SubType();
instance1.color.push('black');
console.log(instance1.color); // [ 'red', 'green', 'black' ]

var instance2 = new SubType();
console.log(instance2.color); // [ 'red', 'green', 'black' ]
```

SubType的所有实例都会共享一个color属性，对instance1的修改能通过instance2反映出来。因此，实践中很少单独使用原型链。

## 借用构造函数

在子类型构造函数的内部调用超类型构造函数。

```js
function SuperType() {
  this.color = ['red', 'green'];
}

function SubType() {
  // 继承了SuperType
  SuperType.call(this);
}

SubType.prototype = new SuperType();

var instance1 = new SubType();
instance1.color.push('black');
console.log(instance1.color);

var instance2 = new SubType();
console.log(instance2.color);
```

SubType的每个实例都会具有自己的color属性的副本。

### 传递参数

借用构造函数有一个很大的优势，即可以在子类型构造函数中向超类型构造函数传递参数。

```js
function SuperType(name) {
  this.name = name;
}

function SubType() {
  SuperType.call(this, 'jack');
  this.age = 29;
}

var instance = new SubType();
console.log(instance.name); // jack
console.log(instance.age); // 29
```

但仅仅使用构造函数，也无法避免构造函数模式的问题——方法都在构造函数中定义，无法实现函数复用。

## 组合继承

使用原型链实现对原型属性和方法的继承，使用借用构造函数实现对实例属性的继承。

```js
function SuperType(name) {
  this.name = name;
  this.color = ['red', 'green'];
}

SuperType.prototype.sayName = function() {
  // 继承属性
  console.log(this.name);
};

function SubType(name, age){
  SuperType.call(this, name);
  this.age = age;
}

// 继承方法
SubType.prototype = new SuperType();
SubType.prototype.constructor = SubType;
SubType.prototype.sayAge = function() {
  console.log(this.age);
}

var instance1 = new SubType('jack', 20);
instance1.color.push('blue');
console.log(instance1.color); // [ 'red', 'green', 'blue' ]
instance1.sayName(); // jack
instance1.sayAge(); // 20

var instance2 = new SubType('Greg', 24);
console.log(instance2.color); // [ 'red', 'green' ]
instance2.sayName(); // Greg
instance2.sayAge(); // 24
```

组合式继承是JS中最常用的继承模式，而且，`instancof`和`isPrototypeOf()`也能够用于识别基于组合继承创建的对象。

## 原型式继承

该方法的原理是创建一个构造函数，构造函数的原型指向对象，然后调用new操作符创建实例，并返回这个实例，本质是一个浅拷贝。

```js
function object(obj) {
	function F() {};
	F.prototype = obj;
	return new F();
}
```

例子如下：

```js
function object(obj) {
	function F() {};
	F.prototype = obj;
	return new F();
}

var person = {
  name: 'jack',
  friends: ['a1', 'a2']
};

var anotherPerson = object(person);
anotherPerson.name = 'Greg';
anotherPerson.friends.push('b1');

var person3 = object(person);
person3.name = 'Linda';
person3.friends.push('c1');

console.log(person.friends); // [ 'a1', 'a2', 'b1', 'c1' ]
```

当想让一个对象与另一个对象保持类似的情况下，原型式继承可以胜任，其中包含引用类型值的属性始终都会共享相应的值，就像使用原型模式一样。

ES5使用`Object.create()`方法规范化了原型式继承。该方法接收两个参数：

- 新对象原型的对象
- （可选）为新对象定义额外属性的对象

``` js
var person = {
  name: 'jack',
  friends: ['a1', 'a2']
};

var anotherPerson = Object.create(person);
anotherPerson.name = 'Greg';
anotherPerson.friends.push('b1');

var person3 = Object.create(person, {
  name: {
    value: "Linda"
  }
});

console.log(person.friends); // [ 'a1', 'a2', 'b1' ]
console.log(person3.name); // "Linda"
```



## 寄生式继承

```js
function object(o) {
  function F() {}
  F.prototype = o;
  return new F();
}

function createAnother(original) {
  var clone = object(original);
  clone.sayHi = function() {
    console.log('hi');
  };
  return clone;
}

var person = {
  name: 'jack',
  friends: ['Linda', 'Cook']
};
var anotherPerson = createAnother(person);
anotherPerson.sayHi();

```

使用寄生式继承来为对象添加函数，**会由于不能做到函数复用而降低效率**；**这一点与构造函数模式类似**。

