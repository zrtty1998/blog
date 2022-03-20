---
title: 31天JavaScript学习-第4天
reprint: false
date: 2022-02-23 10:28:39
updated: 2022-02-23 10:28:39
conver:
categories: 前端
tags:
  - JavaScript
---

# 内置引用类型（二）——Function、RegExp

<!--more-->

## Function

函数的特点：

- 函数是一个对象，每个函数都是Function类型的实例
- 函数名是一个指向函数对象的指针

### 函数的定义/声明

**方式一：函数关键字**

```js
function sum (a, b) {
	return a + b;
}
```

在使用函数关键字进行函数声明时，会有**函数声明提升**的过程。

**方式二：函数表达式（匿名函数）**

```js
var sum = function(a, b) {
	return a + b;
};
```

**方式三：构造函数**

```js
var sum = new Function('a', 'b', 'return a + b;');
```

注意，Function里的参数都必须是**字符串**形式。

### 函数内部属性

#### 内部对象

函数内部有两个特殊的对象：**arguments**和**this**。

##### arguments

arguments是一个类数组对象（伪数组），包含传入函数中的所有参数，可以通过索引来操作数据，也可以获取长度。**arguments代表的是实参，arguments只在函数中使用。**

**1、arguments.length**

arguments.length可以用来获取**实参的长度**。

**2、arguments.callee**

arguments有一个名为callee的属性，该属性是一个指针，指向拥有这个arguments对象的函数。

在使用函数**递归**调用时，推荐使用 arguments.callee 代替函数名本身。如阶乘函数：

```js
function factorial(num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
```

该函数的执行与函数名factorial紧紧耦合在了一起，为了消除耦合可以使用下面的写法：

```js
function factorial(num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * arguments.callee(num - 1);
  }
}
```

##### this

根据函数的调用方式的不同，this 会指向不同的对象：

- 以函数的形式（包括普通函数、定时器函数、立即执行函数）调用时，this 的指向永远都是 window。比如`fun();`相当于`window.fun();`
- 以方法的形式调用时，this 指向调用方法的那个对象
- 以构造函数的形式调用时，this 指向实例对象
- 以事件绑定函数的形式调用时，this 指向**绑定事件的对象**
- 使用 call 和 apply 调用时，this 指向指定的那个对象

ES6的箭头函数并不遵守上面的准则，而是会继承外层函数调用的this绑定。

JS专门提供了一些方法来改变函数内部的this指向，`call()、apply()、bind()`。

#### 内部属性

##### caller

caller保存着调用当前函数的函数的引用，如果是在全局作用域中调用当前函数，则它的值为null。

### 函数的属性和方法

ES中的函数时对象，因此函数也有属性和方法。

- 属性：length、prototype
- 方法：apply()、call()、bind()

#### 属性

##### length

length属性表示函数希望接收的命名参数的个数。

##### prototype

对于ES的引用类型，prototype是保存它们所有实例方法的真正所在。诸如toString()和valueOf()等方法实际上都保存在prototype名下，只不过是通过各自对象的实例访问罢了。详细见。

#### 方法

##### call()方法

可以调用一个函数，实际上等于设置函数体内this对象的值。

`fn1.call(this指向的作用域, 函数实参1, 函数实参2……);`

第一个参数中，如果不需要改变 this 指向，则传 null。

call() 方法的另一个应用：**可以实现继承**。之所以能实现继承，其实是利用了上面的作用。

```js
function Father(myName, myAge) {
  this.name = myName;
  this.age = myAge;
}

function Son(myName, myAge) {
    // 通过这一步，将 father 里面的 this 修改为 Son 里面的 this；另外，给 Son 加上相应的参数，让 	Son 自动拥有 Father 里的属性。最终实现继承
  Father.call(this, myName, myAge);
}

const son1 = new Son('jack', 16);
console.log(JSON.stringify(son1)); // {"name":"jack","age":16}
```

##### apply()方法

可以调用一个函数，实际上等于设置函数体内this对象的值。

apply()接收两个参数：

`fn1.apply(this指向的作用域, [参数数组]);`

其中第二个参数可以是Array的实例，也可以是arguments对象。

**apply() 方法的巧妙应用：求数组的最大值**

我们知道，如果想要求数组中元素的最大值的时候，数组本身是没有自带方法的。那怎么办呢？

虽然数组里没有获取最大值的方法，但是数值里面有 `Math.max(数字1，数字2，数字3)` 方法，可以获取**多个数值中的最大值**。 另外，由于 apply() 方法在传递实参时，必须要以数组的形式，所以我们可以 通过 Math.max() 和 apply() 曲线救国。

```js
const arr1 = [3, 7, 10, 8];

// 下面这一行代码的目的，无需改变 this 指向，所以：第一个参数填 null，或者填 Math，或者填 this 都可以。严格模式中，不让填null。
const maxValue = Math.max.apply(Math, arr1); // 求数组 arr1 中元素的最大值
console.log(maxValue);

const minValue = Math.min.apply(Math, arr1); // 求数组 arr1 中元素的最小值
console.log(minValue);
```

##### bind()方法

bind()会创建一个函数的实例，其this值会被绑定到传给bind()函数的值，

`new_func = fn1.bind(this指向的作用域, 函数实参1, 函数实参2……);`

如：

```js
window.color = 'red';
var o = { color: 'blue' };

function sayColor(){
  console.log(this.color);
}

var objectSayColor = sayColor.bind(o);
objectSayColor(); // blue
```

## RegExp

ES通过RegExp类型来支持正则表达式。

`var expression = / pattern / flags;`

其中模式（pattern）可以是任意正则表达式。每个正则表达式都可以带有一个或多个标志（flags），匹配模式支持下列三种模式：

- **g：**全局（global）模式。模式应用于所有字符串，发现第一个匹配项停止。
- **i：**不区分大小写。
- **m：**多行模式，到达一行文本末尾还会继续查找下一行。

### 实例属性

RegExp的每个实例都具有下列属性。

| 属性       | 数据类型 | 解释                                    |
| ---------- | -------- | --------------------------------------- |
| global     | boolean  | 是否设置g标志                           |
| ignoreCase | boolean  | 是否设置i标志                           |
| lastIndex  | 整数     | 开始搜索下一个匹配项的字符位置，从0开始 |
| multiline  | boolean  | 是否设置m标志                           |
| source     | String   | 正则表达式的字符串形式                  |
