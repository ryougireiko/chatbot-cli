from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()  # 加载
api_key = os.getenv("DEEPSEEK_API_KEY")  # 导入apikey
base_url = "https://api.deepseek.com"


class Chatbot:

    def __init__(self,
                 system_prompt: str = '你是一个乐于助人的AI助手') -> None:  # 这里这个系统提示是一个默认值，自己可以使用bot=Chatbot(system_prompt="来添加人设")
        self.system_prompt = system_prompt  # 系统提示
        self.client = OpenAI(api_key=api_key, base_url=base_url)  # 创建client
        self.model = "deepseek-chat"  # 使用官方支持的模型名字
        self.history = [{"role": "system", "content": self.system_prompt}]

    def chat(self, userinput: str) -> str:
        self.history.append({"role": "user", "content": userinput})  # 添加用户输入
        try:  # 尝试

            response = self.client.chat.completions.create(model=self.model, messages=self.history)  # 调用api
            assistant_content = response.choices[0].message.content  # 获取结果
        except Exception as e:  # 如果出错
            self.history.pop()  # 删除用户最后一次输入的东西
            return f'[错误]api调用失败：{e}'  # 出错的话就到此为止了
        self.history.append({"role": "assistant", "content": assistant_content})  # 回复加入历史
        return assistant_content

    def clear_history(self) -> None:
        self.history = [{"role": "system", "content": self.system_prompt}]  # 把这个列表清空的只剩ai的人设了

    def get_history_count(self) -> int:
        return (len(self.history) - 1) // 2

    def save_history(self,filename: str) -> None: #保存历史
        try:
            with open(filename,'w',encoding='utf-8') as f: # f是文件名字
                json.dump(self.history,f,ensure_ascii=False,indent=2) #indent是缩进的意思，而ensure_ascii是编码，中文不显示的时候加这个
                # json.dump用于将python对象转换成json字符串，indent是缩进，ensure_ascii是编码，中文不显示的时候加这个
                print(f"对话历史已保存到 {filename}")
        except Exception as e:
            print(f"[错误] 保存失败: {e}")

    def load_history(self,filename: str) -> None:
        try:
            with open(filename,'r',encoding='utf-8') as f: # 读文件
                self.history = json.load(f)
                print(f"历史对话已经从{filename}加载成功！")
        except FileNotFoundError:
            print(f"[错误] 文件{filename}不存在")
        except Exception as e:
            print(f"[错误] 加载失败: {e}")
