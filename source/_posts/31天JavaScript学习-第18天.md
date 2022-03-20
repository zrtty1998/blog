---
title: 31天JavaScript学习-第18天
reprint: false
date: 2022-03-16 20:00:22
updated: 2022-03-16 20:00:22
conver:
categories: 前端
tags:
  - JavaScript
---

# Promise（一）

<!--more-->

JS是一门单线程语言，早期我们解决异步场景时，大部分情况都是通过回调函数来进行。

## 回调函数

把函数A传给另一个函数B调用，那么函数A就是回调函数。

例如浏览器中发送Ajax请求，就是一个常见的异步场景，发送请求后，需要等待服务端响应之后我们才能拿到结果。如果希望在异步结束之后执行某个操作，就需要通过回调函数进行操作。

```js
myAjax('a.php', (res1) => {
  console.log(res1);
  myAjax('b.php', (res2) => {
    console.log(res2);
    myAjax('c.php', (res3) => {
      console.log(res3);
    });
  });
});
```

回调的写法比较直观，但层层嵌套也会出现两个问题：

- 嵌套过深会出现回调地狱的问题
- 不同的函数，回调的参数，写法上不一致导致写法复杂

因此ES6引入Promise以解决以上问题。

## Promise

Promise是一个对象，它可以获取异步操作的消息，可以用同步的表现形式来书写异步代码。

使用Promise的基本步骤：

1. 构建一个Promise实例，在其构造函数中传入一个参数，这个参数是一个函数，该函数用于处理异步任务。
2. 函数中传入两个参数：resolve和reject，分别代表异步执行成功和失败后的回调函数
3. 通过`promise.then()`和`promise.catch()`处理返回结果

**Promise对象的三个状态**

- 初始化（等待中）：pending
- 成功：fulfilled
- 失败：rejected

```js
let promise = new Promise((resolve, reject) => {
  // 此时new的操作是同步的，promise的状态被初始化为pending
  setTimeout(function(){ 
    // 模拟异步操作，成功则调用resolve()，此时promise状态会修改为fulfilled
    resolve('成功');
  }, 200);
});

promise.then(
  (response) => { console.log(response); }, // 如果promise的状态为fulfilled，则执行该行语句，函数的参数为resolve()中传递的参数
  (err) => { console.log(err); } // 如果promise的状态为rejected，则执行该行语句，函数的参数为reject()中传递的参数
);
```

**注：Promise的状态一旦改变，就不能再变了**

**举例一**

```js
function delayfunc (callback) {
  setTimeout(function () {
    console.log('等待一秒执行callback');
    callback();
  }, 1000);
}

function myCallback() {
  console.log('被延迟的函数');
}

delayfunc(myCallback);
```

或

```js
function delayfunc (callback) {
  setTimeout(callback, 1000);
}

delayfunc(function() {
  console.log('被延迟的函数');
})
```

用Promise改写

```js
function myPromise() {
  return new Promise((resolve) => {
    setTimeout(resolve, 10000);
  });
}

myPromise().then(() => {
  console.log('被延迟的函数');
});
```

**举例二**

```js
function ajax(url, success, fail) {
  let xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', url);
  xmlhttp.send();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
      success && success(xmlhttp.responseText);
    } else {
      fail && fail(new Error('err'));
    }
  };
}

function promiseA() {
  return new Promise((resolve, reject) => {
    ajax('test.php', (res) => {
      if (res.retCode == 0) {
        resolve('request success' + res);
      } else {
        reject({ retCode: -1, msg: 'error' });
      }
    });
  });
}

promiseA()
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });

// 或promise实例定义成变量
const promiseB = Promise((resolve, reject) => {
  ajax('test.php', (res) => {
    if (res.retCode == 0) {
      resolve('request success' + res);
    } else {
      reject({ retCode: -1, msg: 'error' });
    }
  });
});

promiseB()
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });
```

**Promise处理失败的写法**

1. 通过catch方法捕获状态变为reject的promise
2. then可以传递两个参数，第一个参数为resolve后执行，第二个参数为reject后执行

## Promise的链式调用

使用Promise优化回调地狱的写法。也就是将多层嵌套调用按照线性的方式进行书写。

```js
function ajax(url, success, fail) {
  let xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', url);
  xmlhttp.send();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
      success && success(xmlhttp.responseText);
    } else {
      fail && fail(new Error('err'));
    }
  };
}

new Promise((resolve, reject) => {
  ajax('a.php', (res_a) => {
    resolve(res_a); // 状态改为fulfilled,then()方法接收
  });
}).then((res_a) => {
  return new Promise((resolve, reject) => {
    ajax('b.php', (res_b) => {
      resolve(res_b);
    });
  });
}).then((res_b) => {
  console.log(res_b);
});
```

可以对promise的链式调用进行封装

```js
// 定义ajax请求
function ajax(url, success, fail) {
  let xmlhttp = new XMLHttpRequest();
  xmlhttp.open('GET', url);
  xmlhttp.send();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
      success && success(xmlhttp.responseText);
    } else {
      fail && fail(new Error('err'));
    }
  };
}

// model层，接口封装
function getPromise(url) {
  return new Promise((resolve, reject) => {
    ajax(url, (res) => {
      //res是接口的返回结果
      if (res.retCode == 0) {
        resolve('success' + res);
      } else {
        reject({ retCode: -1, msg: 'error'});
      }
    });
  });
}

// 业务层的接口调用
getPromise('a.php')
  .then((res) => {
    // a请求成功，res是从resolve获取的结果
    return getPromise('b.php');
  })
  .then((res) => {
    return getPromise('c.php');
  })
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });
```

## reject状态的处理

**不处理reject**

```js
getPromise('a.php')
  .then(
    (res) => {
      // a请求成功，res是从resolve获取的结果
      console.log('a:' + res)
      return getPromise('b.php');
    },
    (err) => {
      console.log('a:' + err);
    })
  .then((res) => {
    console.log('b:' + res)
    return getPromise('c.php');
  })
  .then((res) => {
    console.log('c:' + res);
  });
```

a请求失败，在a的then()方法里只打印err。打印结果

```
a:err
undefined
c:success
```

虽然a请求失败，但后续请求依然会执行

**单独处理reject**

```js
getPromise('a.php')
  .then(
    (res) => {
      // a请求成功，res是从resolve获取的结果
      console.log('a:' + res)
      return getPromise('b.php');
    },
    (err) => {
      console.log('a:' + err);
      return getPromise('b.php'); // 即使a请求失败，也继续执行b请求
    })
  .then((res) => {
    console.log('b:' + res)
    return getPromise('c.php');
  })
  .then((res) => {
    console.log('c:' + res);
  });
```

**统一处理reject**

```js
getPromise('a.php')
  .then((res) => {
    // a请求成功，res是从resolve获取的结果
    return getPromise('b.php');
  })
  .then((res) => {
    return getPromise('c.php');
  })
  .then((res) => {
    console.log(res);
  })
  .catch((err) => {
    console.log(err);
  });
```

上面这种写法只要有一个请求失败了，就直接执行catch，剩下的请求就不会继续执行了。

## return的返回值

then()方法里的返回值，有两种情况：

1. 返回Promise实例对象。返回的该实例对象会调用下一个then
2. 返回普通值。返回的值会直接传递给下一个then，通过then参数中函数的参数接收该值。返回普通值时，由于并没有返回promise实例对象，那它的then是谁来调用的呢？是产生的一个新的默认的promise实例以确保可以继续链式操作。

