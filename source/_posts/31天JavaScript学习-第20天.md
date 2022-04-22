---
title: 31天JavaScript学习-第20天
reprint: false
date: 2022-03-20 20:03:44
updated: 2022-03-20 20:03:44
conver:
categories: 前端
tags:
  - JavaScript
---

# Async/Await

<!--more-->

async/await是ES8引入的新语法，是另外一种异步编程解决方案。

其本质是Generator的语法糖

async返回Promise实例对象，await可以得到异步结果。

## async

先查看一下async返回的结果

```js
async function testAsync() {
  return 'okk';
}

const result = testAsync();
console.log(result); // Promise { 'okk' }
```

可以看到，async函数返回一个Promise对象，如果在函数中return一个直接量，async会把这个直接量通过`Promise.resolve()`封装成一个Promise对象。因此，我们可以用`then()`来处理这个Promise对象

```js
testAsync().then(res => {
  console.log(res);
}); // okk
```

由上一节可以知道，Promise对象的生成是同步代码，在Promise对象中调用的`resolve()`和`reject()`才是异步任务。因此，在没有await的情况下执行async函数，它会按照同步顺序执行，返回一个Promise对象。

## await

await等待的是一个表达式，这个表达式可以是Promise对象或者其他值。（也即没有特殊限定一定是等待async）。

```js
function func1() {
  return 'func1';
}

async function func2() {
  return 'func2';
  // return Promise.resolve('func2');
}

async function test() {
  let v1 = func1(); 
  let v2 = func2();
  console.log(v1); // func1
  console.log(v2); // Promise { 'func2' }
 
  const res1 = await func1();
  const res2 = await func2();
  console.log(res1); // func1
  console.log(res2); // func2
}

test();

```

如果等到的不是一个Promise对象，await运算结果就是它等到的量。

如果等到的是一个Promise对象，它会阻塞后面的代码，等待Promise对象resolve，然后得到resolve的值，作为await表达式的运算结果。（这就是await必须用在async函数内部的原因，async函数调用不会造成阻塞，它内部所有的阻塞都被封装在一个Promise对象中异步执行。）

## 组合使用

首先看一下Promise与async/await的写法区别

```js
function waitForAwhile() {
  return new Promise(resolve => {
    setTimeout(() => resolve('long_time_step'), 2000);
  });
}

waitForAwhile().then(v => {
  console.log('got', v);
}); // got long_time_step
```

```js
function waitForAwhile() {
  return new Promise(resolve => {
    setTimeout(() => resolve('long_time_step'), 2000);
  });
}

async function test () {
  const v = await waitForAwhile();
  console.log(v);
}

test();
```

async/await的优势是在处理多个Promise的then链

```js
function waitForAwhile(n) {
  return new Promise(resolve => {
    setTimeout(() => resolve(n + 200), n);
  });
}

function step1(n) {
  console.log(`step1 with ${n}`);
  return waitForAwhile(n);
}

function step2(n) {
  console.log(`step2 with ${n}`);
  return waitForAwhile(n);
}

function step3(n) {
  console.log(`step3 with ${n}`);
  return waitForAwhile(n);
}
```

如果使用Promise来处理该步骤

```js
function doIt() {
  console.log('doIt');
  const time1 = 300;
  step1(time1)
    .then(time2 => step2(time2))
    .then(time3 => step3(time3))
    .then(result => {
      console.log(`result is ${result}`);
      console.log("finish");
    });
}
doIt();
```

如果用async/await来处理该步骤

```js
async function doIt() {
  console.log('doIt');
  const time1 = 300;
  const time2 = await step1(time1);
  const time3 = await step2(time2);
  const result = await step3(time3);
  console.log(`result is ${result}`);
  console.log('finish');
}

doIt();
```

async/await主要解决了Promise传递参数太麻烦的痛点。

## 处理reject状态

await处理的Promise对象，其状态可能是reject，因此最好把await命令放在try...catch代码块中。

```js
async function myFunction() {
  try {
    await returnSomePromise();
  } catch (err) {
    console.log(err);
  }
}

// 第二种写法
async function myFunction() {
  await returnSomePromise().catch(function (err) {
    console.log(err);
  });
}
```

