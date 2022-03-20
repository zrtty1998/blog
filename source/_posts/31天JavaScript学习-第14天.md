---
title: 31天JavaScript学习-第14天
reprint: false
date: 2022-03-07 10:39:41
updated: 2022-03-07 10:39:41
conver:
categories: 前端
tags:
  - JavaScript
---

# **ES6语法**

<!--more-->

## 简介

ES 的全称是 ECMAScript，它是由 ECMA 国际标准化组织 制定的一套**脚本语言的标准化规范**。

ES6 是新的 JS 语法标准。**ES6 实际上是一个泛指，泛指 ES 2015 及后续的版本**。

> 掌握 ES6 之后，如果你的业务需要考虑 ES5 的兼容性，则可以这样做：写 ES6 语法的 js 代码，然后通过 `Babel`将 ES6 转换为 ES5。

> PS：我们在写代码时，能用单引号尽量用单引号，而不是双引号，前者在压缩之后，程序执行会更快。

## let、const和块级作用域

ES6中，新增了let和const来定义变量：

- **let：**定义变量，替代var。用let声明的变量，具有块级作用域，只在局部起作用。
- **const：**定义常量，定义后不可修改。用const声明的常量，只在块级作用域内起作用，且必须在声明时赋值。

**暂时性死区（TDZ）**

ES6规定，使用let/const声明的变量，会使区块形成封闭的作用域。若在声明之前使用变量，就会报错。

**let 和 const 的特点【重要】**

- 不属于顶层对象 Window
- 不允许重复声明
- 不存在变量提升
- 暂时性死区
- 支持块级作用域

相反， 用`var`声明的变量：存在变量提升、可以重复声明、**没有块级作用域**。

## 变量的解构赋值

ES6允许我们，按照一一对应的方式，从数组或对象中提取值，再将提取出来的值赋值给变量。

### 数组的解构赋值

将数组中的值按照位置提取出来，然后赋值给变量

```js
let [a, b, c] = [1, 2, 3];
```

**两边数量不相等的情况：**

- **变量数量>值的数量：**多余的变量被赋值为undefined
- **变量数量<值的数量：**正常赋值

**解构时，左边变量可以有默认值**

```js
let [a, b, c=10] = [1, 2]
console.log(a); // 1
console.log(b); // 2
console.log(c); // 10
```

**赋值中含有undefined和null的情况**

```js
let [a, b, c=10] = [1, undefined, undefined]
console.log(a); // 1
console.log(b); // undefined
console.log(c); // 10
```

```js
let [a, b, c=10] = [1, null, null]
console.log(a); // 1
console.log(b); // null
console.log(c); // null
```

### 对象的解构赋值

将对象中的值按照属性匹配的方式提取出来，然后赋值给变量。

ES6前，我们从接口拿到json数据后，一般这么赋值

```js
var name = json.name;

var age = json.age;

var sex = json.sex;
```

ES6后，可以简化成

```js
const person = { name: 'zrtty', age: 28, sex: '男' };
let { age, name, sex } = person; // 对象的结构赋值

console.log(name); // 打印结果：zrtty
console.log(age); // 打印结果：28
console.log(sex); // 打印结果：男
```

上方代码可以看出，对象的解构与数组的结构，有一个重要的区别：**数组**的元素是按次序排列的，变量的取值由它的**位置**决定；而**对象的属性没有次序**，是**根据键来取值**的。

**两边数量不相等的情况：**

- **变量数量>值的数量：**多余的变量被赋值为undefined
- **变量数量<值的数量：**正常赋值

**变量自定义命名结构赋值**

```js
const person = { name: 'zrtty', age: 28 };
let { name: myName, age: myAge } = person; // 对象的结构赋值

console.log(myName); // 打印结果：zrtty
console.log(myAge); // 打印结果：28

console.log(name); // 打印报错：Uncaught ReferenceError: name is not defined
console.log(age); // 打印报错：Uncaught ReferenceError: age is not defined
```

**圆括号的使用**

如果变量 foo 在解构之前就已经定义了，此时你再去解构，就会出现问题。下面是错误的代码，编译会报错：

```
	let foo = 'haha';
	{ foo } = { foo: 'smyhvae' };
	console.log(foo);
```

要解决报错，只要在解构的语句外边，加一个圆括号即可：

```
let foo = 'haha';
({ foo } = { foo: 'smyhvae' });
console.log(foo); //输出结果：smyhvae
```

### 字符串结构

字符串也可以解构，这是因为，此时字符串被转换成了一个类似数组的对象。举例如下：

```js
const [a, b, c, d] = 'hello';
console.log(a); // h
console.log(b); // e
console.log(c); // l

console.log(typeof a); // string
```

## 箭头函数

ES6的箭头函数语法：

`(arg1, agr2, ...) => { 函数体 }`

注：

- 如果有且仅有1个形参，则`()`可以省略
- 如果函数体内有且仅有1条语句，则`{}`可以省略，前提是这条语句必须时return语句

如

```js
function fn1 (a, b) {
	console.log('haa');
	return a + b;
}

const fn2 = (a, b) => {
    console.log('haha');
    return a + b;
}
```

###  this指向

箭头函数的作用只是为了写法更简洁吗？不仅仅是这个原因，还有一个很大的作用是this的指向有关。

**this指向的区别**

- **ES5：**this指向函数被调用的对象
- **ES6：**箭头函数本身不绑定this，this指向的是箭头函数定义位置的this（箭头函数在哪个位置定义的，this就跟这个位置的this指向相同）。

例如

```js
const obj = { name: 'zrtty' };

function fn1() {
  console.log(this); // { name: 'zrtty' }
  return () => {
    console.log(this);
  };
}

const fn2 = fn1.call(obj);
fn2(); // { name: 'zrtty' }
```

`fn1.call(obj)`执行之后，第一个this就指向了被调用的对象obj；而箭头函数是在fn1()函数里定义的，所以第二个this和第一个this指向的是同一个位置。

**面试题**

```js
var name = '许嵩';
var obj = {
    name: 'zrtty',
    sayHello: () => {
        console.log(this.name);
    },
};

obj.sayHello();
```

打印结果是`许嵩`。因为obj对象并不产生作用域，定义在obj内部的sayHello箭头函数实际仍定义在全局作用域中，也就是this指向window。

### 参数默认值

传统写法：

```js
function fn(param) {
    let p = param || 'hello';
    console.log(p);
}
```

ES6写法：

```js
function fn(param = 'hello') {
    console.log(param);
}
```

**注：**默认值的后面，不能再有**没有默认值的变量**

### 剩余参数

**剩余参数**允许我们将不确定数量的**剩余的元素**放到一个**数组**中。

比如说，当函数的实参个数大于形参个数时，我们可以将剩余的实参放到一个数组中。

**传统写法（会报错）**

```js
function fn(a, b, c) {
    console.log(a);
    console.log(b);
    console.log(c);
    console.log(d);
}

fn(1, 2, 3);
```

**ES6 写法**：

```js
const fn = (...args) => {
    //当不确定方法的参数时，可以使用剩余参数
    console.log(args[0]);
    console.log(args[1]);
    console.log(args[2]);
    console.log(args[3]);
};

fn(1, 2); // 1 2 undefined undefined
fn(1, 2, 3); // 1 2 3 undefined
```

方法的定义中了四个参数，但调用函数时只使用了三个参数，ES6 中并不会报错。

**注：**args 参数之后，不能再加别的参数，否则编译报错。

## 扩展语法（展开语法）

扩展运算符和剩余参数是相反的。

剩余参数是将剩余的元素放到一个数组中；而扩展运算符是将数组或者对象拆分成逗号分隔的参数序列。

如

```js
const arr = [10, 20, 30];

console.log(arr); // [ 10, 20, 30 ]
console.log(...arr); // 10 20 30
console.log(10, 20, 30); // 10 20 30
```

**举例1：数组赋值**

```js
let arr1 = ['www', 'smyhvae', 'com'];
let arr2 = arr1; // 将 arr1 赋值给 arr2，其实是让 arr2 指向 arr1 的内存地址
console.log('arr1:' + arr1); // arr1:www,smyhvae,com
console.log('arr2:' + arr2); // arr2:www,smyhvae,com

arr2.push('你懂得'); //往 arr2 里添加一部分内容
console.log('arr1:' + arr1); // arr1:www,smyhvae,com,你懂得
console.log('arr2:' + arr2); // arr2:www,smyhvae,com,你懂得
```

```js
let arr1 = ['www', 'smyhvae', 'com'];
let arr2 = [...arr1]; //【重要代码】arr2 会重新开辟内存地址
console.log('arr1:' + arr1);
console.log('arr2:' + arr2);

arr2.push('你懂得'); //往arr2 里添加一部分内容
console.log('arr1:' + arr1); // arr1:www,smyhvae,com
console.log('arr2:' + arr2); // arr2:www,smyhvae,com,你懂得
```

**举例2：合并数组**

```js
let arr1 = ['王一', '王二', '王三'];
let arr2 = ['王四', '王五', '王六'];
// ...arr1  // '王一','王二','王三'
// ...arr2  // '王四','王五','王六'

// 方法1
let arr3 = [...arr1, ...arr2];
console.log(arr3); // ["王一", "王二", "王三", "王四", "王五", "王六"]

// 方法2
arr1.push(...arr2);
console.log(arr1); // ["王一", "王二", "王三", "王四", "王五", "王六"]
```

**举例3：将伪数组或者可遍历对象转换为真正的数组**

```js
const myDivs = document.getElementsByClassName('div');
const divArr = [...myDivs]; // 利用扩展运算符，将伪数组转为真正的数组
```

## Set数据结构

ES6提供了新的数据结构Set。Set类似于数组，但成员的值都是唯一的，没有重复的值。

**Set的创建**

```js
const set1 = new Set();
console.log(set1.size);
```

**Set的用法之一：数组去重**

```js
const set2 = new Set(['张三', '李四', '王五', '张三']); // 注意，这个数组里有重复的值

// 注意，这里的 set2 并不是数组，而是一个单纯的 Set 数据结构
console.log(set2); // {"张三", "李四", "王五"}
console.log(typeof set2); // object
console.log(set2 instanceof Array); 

// 通过扩展运算符，拿到 set 中的元素（用逗号分隔的序列）
// ...set2 //  "张三", "李四", "王五"

// 注意，到这一步，才获取到了真正的数组
console.log([...set2]); // ["张三", "李四", "王五"]
```

