# wxpay

# 关于XML解析存在的安全问题, 所有请把xml替换成lxml
# 相关说明
 - [微信官方XML解析存在的安全问题说明](https://pay.weixin.qq.com/wiki/doc/api/jsapi.php?chapter=23_5)
 - [xml.etree.ElementTree说明](https://docs.python.org/2/library/xml.etree.elementtree.html)

## lxml代码段
```
from lxml import etree

xmlData = etree.parse(xmlSource,etree.XMLParser(resolve_entities=False))
```

## 微信小程序 支付demo 

## 文件描述：
 - pay: 微信小程序代码
 - server: python+flask

## 功能说明
 - 本程序只实现了最基本的统一下单支付接口

## 参考
 - [统一下单](https://pay.weixin.qq.com/wiki/doc/api/wxa/wxa_api.php?chapter=9_1)
 - [wx.requestPayment](https://mp.weixin.qq.com/debug/wxadoc/dev/api/api-pay.html)
