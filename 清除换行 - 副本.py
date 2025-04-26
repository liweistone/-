import os

def process_text(content):
    """将换行符替换为单个空格"""
    # 先处理回车符，再将换行符替换为空格
    return content.replace("\r", "").replace("\n", " ")

def process_files(folder_path):
    """处理指定文件夹内所有txt文件"""
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            
            # 读取文件内容（自动检测编码）
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # 处理文本内容
            new_content = process_text(content)
            
            # 覆盖写入原文件
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

if __name__ == "__main__":
    # 设置你的文件夹路径（注意使用原始字符串）
    folder_path = r"提示词"
    process_files(folder_path)
    print("处理完成！所有换行符已替换为空格，原有空格保留")