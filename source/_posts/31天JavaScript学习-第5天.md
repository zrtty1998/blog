---

title: 31天JavaScript学习-第5天
reprint: false
date: 2022-02-24 10:29:47
updated: 2022-02-24 10:29:47
conver:
categories: 前端
tags:
  - JavaScript
---

# 内置引用类型（三）——基本包装类型和单体内置对象

<!--more-->

## 基本包装类型

我们都知道，js 中的数据类型包括以下几种。

- 基本数据类型：String、Number、Boolean、Null、Undefined
- 引用数据类型：Object

为了便于操作基本类型值，ES提供了三个特殊的引用类型。实际上，每当读取一个基本类型值的时候，后台就会创建一个对应的基本包装类型的对象。

- String()：将基本数据类型字符串，转换为 String 对象。
- Number()：将基本数据类型的数字，转换为 Number 对象。
- Boolean()：将基本数据类型的布尔值，转换为 Boolean 对象。

通过上面这这三个包装类，我们可以**将基本数据类型的数据转换为对象**。

**基本包装类型的作用**

当我们对一些基本数据类型的值去调用属性和方法时，浏览器会**临时使用包装类将基本数据类型转换为引用数据类型**，这样的话，基本数据类型就有了属性和方法，然后再调用对象的属性和方法；调用完以后，再将其转换为基本数据类型。

```js
var s1 = 'some text';
var s2 = s1.substring(2);
```

s1包含一个字符串，字符串是基本类型值，但第二行调用了s1的substring()方法。基本类型值不是对象，理应没有方法。其实该操作包含以下三个步骤：

1. 创建String类型的一个实例；`var s1 = new String('some text');`
2. 在实例上调用指定的方法；`var s2 = s1.substring(2);`
3. 销毁这个实例；`s1 = null;`

## 单体内置对象

### Global

Global（全局）对象不属于任何其他对象的属性和方法，所有的对象都是它的属性和方法。事实上，没有全局变量和全局函数，所有在全局作用域定义的属性和函数，都是Global对象的属性；某些函数如isNan()、parseInt()以及parseFloat()，实际上都是Global对象的方法。

### Math

Math 和其他的对象不同，它不是一个构造函数，不需要创建对象。所以我们不需要 通过 new 来调用，而是直接使用里面的属性和方法即可。

Math属于一个工具类，里面封装了数学运算相关的属性和方法。如下：

| 属性         | 描述                        | 备注 |
| ------------ | --------------------------- | ---- |
| Math.E       | 自然对数的底数，即常量e的值 |      |
| Math.LN10    | 10的自然对数                |      |
| Math.LN2     | 2的自然对数                 |      |
| Math.LOG2E   | 以2为底e的对数              |      |
| Math.LOG10E  | 以10为底e的对数             |      |
| Math.PI      | π的值                       |      |
| Math.SQRT1_2 | 1/2的平方根                 |      |
| Math.SQRT2   | 2的平方根                   |      |



| 方法              | 描述                                       | 备注              |
| ----------------- | ------------------------------------------ | ----------------- |
| Math.PI           | 圆周率                                     | Math对象的属性    |
| Math.abs()        | **返回绝对值**                             |                   |
| Math.random()     | 生成0-1之间的**随机浮点数**                | 取值范围是 [0，1) |
| Math.floor()      | **向下取整**（往小取值）                   |                   |
| Math.ceil()       | **向上取整**（往大取值）                   |                   |
| Math.round()      | 四舍五入取整（正数四舍五入，负数五舍六入） |                   |
| Math.max(x, y, z) | 返回多个数中的最大值                       |                   |
| Math.min(x, y, z) | 返回多个数中的最小值                       |                   |
| Math.pow(x,y)     | 乘方：返回 x 的 y 次幂                     |                   |
| Math.sqrt()       | 开方：对一个数进行开方运算                 |                   |
