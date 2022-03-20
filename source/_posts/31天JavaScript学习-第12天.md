---
title: 31天JavaScript学习-第12天
reprint: false
date: 2022-03-05 16:53:32
updated: 2022-03-05 16:53:32
conver:
categories: 前端
tags:
  - JavaScript
---

# DOM

<!--more-->

## Node类型

DOM可以将任何HTML或XML文档描绘成一个由多层节点构成的结构。

**节点**（Node）是构成HTML的最基本单元。

DOM1级定义了一个Node接口，该接口实现了DOM中的所有节点类型。这个Node接口在JS中是作为Node类型实现的，所有节点类型都继承自Node类型，因此所有的节点类型都共享着相同的属性和方法。

**每个节点都有一个NodeType属性**，用于表明节点的类型：

| 节点类型                         | 值   |
| -------------------------------- | ---- |
| Node.ELEMENT_NODE                | 1    |
| Node.ATTRIBUTE_NODE              | 2    |
| Node.TEXT_NODE                   | 3    |
| Node.CDATA_SECTION_NODE          | 4    |
| Node.ENTITY_REFERENCE_NODE       | 5    |
| Node.ENTITY_NODE                 | 6    |
| Node.PROCESSING_INSTRUCTION_NODE | 7    |
| Node.COMMENT_NODE                | 8    |
| Node.DOCUMENT_NODE               | 9    |
| Node.DOCUMENT_TYPE_NODE          | 10   |
| Node.DOCUMENT_FRAGMENT_NODE      | 11   |
| Node.NOTATION_NODE               | 12   |

### 节点关系

节点之间存在着以下几种关系，均可通过节点属性访问

- childNodes：子节点
- parentNode：父节点
- previousSibling：上一个兄弟节点
- nextSibling：下一个兄弟节点
- firstChild：第一个子节点
- lastChild：最后一个子节点
- ownerDocument：指向整个文档的文档节点

### 节点操作

DOM树可以看成是由一系列指针连接起来的，但任何DOM节点不能同时出现在文档的多个位置上。

#### 节点创建和删除

DOM提供了一些操作节点的方法

| 方法            | 说明                             | 备注                                   |
| --------------- | -------------------------------- | -------------------------------------- |
| appendChild()   | 向childNodes列表末尾添加一个节点 | 返回新增的节点                         |
| insertBefore()  | 往特定的位置之前插入节点         | 返回新增的节点                         |
| replaceChild()  | 用新节点替换旧节点               | 被替代的节点仍在文档中，只是没有了位置 |
| removeChild()   | 移除节点                         | 返回移除的节点，仍在文档中             |
| createElement() | 创建节点                         | 返回新增的节点                         |
| cloneNode()     | 创建节点的副本                   | true深复制，false浅复制                |

## Document类型

### 文档信息

document对象是HTMLDocument的一个实例，存在一些表现网页的一些信息的属性。

| 属性              | 说明                  |
| ----------------- | --------------------- |
| document.title    | `<title>`元素中的文本 |
| document.URL      | 页面完整的URL         |
| document.domain   | 页面的域名            |
| document.referrer | 链接到当前页面的URL   |

| 方法                              | 说明                       | 备注 |
| --------------------------------- | -------------------------- | ---- |
| document.getElementById()         | 通过id获取一个元素节点     |      |
| document.getElementsByTagName()   | 通过标签名获取元素节点数组 |      |
| document.getElementsByClassName() | 通过类名获取元素节点数组   |      |

## Element类型

### 节点属性

| 方法              | 说明             |
| ----------------- | ---------------- |
| getAttribute()    | 获取节点的属性值 |
| setAttribute()    | 设置节点的属性值 |
| removeAttribute() | 删除节点的属性   |

