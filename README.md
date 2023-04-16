# ChatBotHub
ChatBotHub get response from multi chatgpt website. ChatBotHub 一键同时从多个 chatgpt 网页获得回复。

## Motivation

不论是 ChatGPT 官网还是众多替代网站都存在发送消息失败的情况，往往需要再开一个网页重新复制问题获取答案。
所以，一个同时发送给多个网页的 Hub 就很有必要，免去了新开网页，复制粘贴等操作，非常简单。

## 依赖

```
pip install selenium
```

## 配置
* 发送内容
```
chat_content = "你的内容"

```

* 常用网址
最好选择不需要登录的网址，或者是提前登录好。
```
# 打开多个网页，可以自行增删改
driver.get("https://openmao.panchuang.net/#/chat/")
driver.execute_script("window.open('https://zlv7o.aichatos.com/#/chat/');")
driver.execute_script("window.open('https://free.anzz.top/#/chat/');")
```

# todolist

* 增加多次对话功能，从命令行获取提问内容，然后连续对话。 