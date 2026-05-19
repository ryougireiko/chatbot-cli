# ChatBot CLI

一个基于DeepSeek API的命令行聊天机器人，支持多轮对话，命令系统

，历史保存与加载。

## 功能特性

* 多轮对话，自动维护上下文
* 命令系统（/help可查看所有命令，如/save等）
* 完整的异常处理（api失效、文件不存在、用户重点）

## 环境要求

* Python 3.10以上
* 一个deepseek的api，官网是https://platform.deepseek.com

## 安装与运行

1.克隆仓库

~~~bash
git clone https://github.com/ryougireiko/chatbot-cli.git
cd chatbot-cli
~~~

2.安装依赖

~~~bash
pip install openai python-dotenv
~~~

3.配置api key：复制‘’.env.example‘’ 为 ‘’.env‘’，填入自己在deepseek官网购买的key替换。DEEPSEEK_API_KEY=sk-你的key

4.运行：

~~~bash
python main.py
~~~

## 命令列表





|      命令      |        功能        |
| :------------: | :----------------: |
|     /help      |      显示帮助      |
|     /clear     |      清空历史      |
|     /save      | 保存对话到json文件 |
|     /load      |  加载对话历史文件  |
|    /history    |  显示当前对话轮数  |
| /exit or /quit |      退出程序      |

## 技术栈

* Python 3.10+
* OpenAI Python SDK 兼容deepseek api
* python-dotenv

