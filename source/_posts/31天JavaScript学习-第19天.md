---
title: 31天JavaScript学习-第19天
reprint: false
date: 2022-03-19 18:55:50
updated: 2022-03-19 18:55:50
conver:
categories: 前端
tags:
  - JavaScript
---

# Promise（二）

<!--more-->

## Promise的实例方法

实例方法指需要建立实例对象，再通过实例对象调用的方法叫做实例方法。Promise的实例方法有：

- **then()：**获取异步任务的正常结果
- **catch()：**获取异步任务的异常结果
- **finally()：**异步任务无论成功与否，都会执行

## Promise的静态方法

静态方法指直接可以通过类名调用的方法。Promise提供的静态方法有：

- **Promise.resolve()**
- **Promise.reject()**
- **Promise.all()**
- **Promise.race()**
- **Promise.allSettled()**
- **Promise.any()**

### Promise.resolve()和Promise.reject()

在某些场景下，我们并没有异步操作，但仍想调用promise.then()，可以通过Promise.resolve()将其包装成成功的状态。

```js
function foo (flag) {
  if (flag) {
    return Promise.resolve('success'); // 直接返回字符串
  } else {
    return Promise.reject('fail'); //直接返回字符串
  }
}

foo(true).then((res) => {
  console.log(res);
});
foo(false).then((err) => {
  console.log(err);
});
```

### Promise.all()

并发处理多个异步任务，所有任务都执行成功，才算成功，这时才会调用then()；如果有一个任务失败，就会调用catch()，整体任务视为失败。

Promise.all()参数传入的时多个Promise实例对象的数组。

**案例：多张图片上传**

如现在有一个上传九张图的需求，每次请求接口时只能上传一张图片。

```js
const imgArr = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg'];
const promiseArr = [];

imgArr.forEach((item) => {
  const p = new Promise((resolve, reject) => {
    // 上传图片伪代码
    // imgUrl = Upload item;
    if (imgUrl) {
      // 单张图片上传成功
      resolve(imgUrl);
    } else {
      reject(item + '上传失败');
    }
  });
  promiseArr.push(p);
});

Promise.all(promiseArr)
  .then((res) => {
    console.log('全部上传成功' + res);
  })
  .catch((err) => {
    console.log('上传失败');
  });
```

如果某张图上传失败，则表现为：

- 前端九张图都会reject，整体catch
- 后端除了上传失败的图片，其余的都会正常请求接口并写入数据库

### Promise.race()

并发处理多个异步任务，返回的是第一个执行完成的promise，且状态和第一个完成的任务状态保持一致。

多个同时执行的异步任务中，哪个异步任务最先执行完成（无论resolv还是reject），整体的状态就和这个任务的状态保持一致。

**应用场景：**在众多Promise实例中，最终结果只取一个Promise，谁返回得最快就用谁的Promise

**举例：timeout手动实现**

一个Promise用于请求接口，另一个Promise用于执行setTimeout()。把两个Promise用Promise.race()方法组装

```js
function query(url, delay = 4000) {
  let promsiseArr = [
    myAjax(url),
    new Promise((resolve, reject) => {
      setTimeout(() => {
        reject('timeout!')
      }, delay);
    })
  ];
  return Promise.race(promsiseArr);
}

query('https://localhost:8888/someurl', 3000)
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });
```

### Promise.allSettled()

该方法返回一个在所有给定的promise都fulfilled或reject后的promise，并带有一个对象数组，每个对象表示对应的promise结果。

当有多个彼此不依赖的异步任务成功完成时，或者想知道每个promise的结果时，通常使用该方法。

### Promise.any()

该方法处理多个promise任务，只要其中任何一个promise成功，就返回那个成功的promise。若没有一个promise成功，就返回一个失败的promise和AggregError类型的实例。
