from chatbot import Chatbot
def main():
    bot = Chatbot()
    while True:
        user_input = input("用户：").strip() # 防止用户多打了空格，这个可以消除输入内容前面的空格
        if not user_input: # 空输入就跳过，防止用户输入空格
            continue

        # 命令系统
        if user_input.startswith("/"): # 检测用户输入命令
            if user_input in ['/exit', '/quit']: # 检测用户输入退出的命令
                print('再见！')
                break
            elif user_input == '/clear':
                bot.clear_history()
                print('历史对话已清空！')
                continue
            elif user_input.startswith('/save'):
                filename = user_input[6:].strip() # 从第六个字符开始，并且这里strip可以防止用户多打了空格，/save正好是五个字符
                #前面的最开始那个strip是防止/前不小心输入空格，而这个防止了在输入文件名字的时候多打了空格
                if not filename:
                    print('请输入保存的文件名！')
                    continue
                bot.save_history(filename)
                continue
            elif user_input.startswith('/load'):
                filename = user_input[6:].strip()
                if not filename:
                    print('请输入要加载的文件名！')
                    continue
                bot.load_history(filename)
                continue
            elif user_input == "/history":
                print(f"当前对话轮数: {bot.get_history_count()}")
                continue
            elif user_input == "/help":
                print("命令列表:")
                print("  /exit     - 退出程序")
                print("  /clear    - 清空对话历史")
                print("  /save <文件名> - 保存对话到 JSON")
                print("  /load <文件名> - 从 JSON 加载对话")
                print("  /history  - 显示对话轮数")
                print("  /help     - 显示此帮助")
                continue
            else:
                print(f"未知命令: {user_input}，输入 /help 查看可用命令")
                continue
        reply = bot.chat(user_input) # 正常输入问题
        print(f"AI: {reply}") # 输出回复
if __name__ == "__main__":
    main()