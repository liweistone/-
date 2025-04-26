import os

def process_text(content):
    """将换行符替换为单个空格"""
    # 先处理回车符，再将换行符替换为空格
    return content.replace("\r", "").replace("\n", " ")

def process_files(folder_path):
    """处理指定文件夹内所有txt文件"""
    # 获取所有txt文件列表
    txt_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]
    total_files = len(txt_files)
    
    if total_files == 0:
        print("未找到任何txt文件！")
        return
    
    print(f"共找到 {total_files} 个txt文件，开始处理...")
    print("=" * 40)
    
    processed_count = 0
    for filename in txt_files:
        file_path = os.path.join(folder_path, filename)
        
        # 显示当前处理进度
        processed_count += 1
        print(f"正在处理 [{processed_count}/{total_files}]: {filename}")
        
        try:
            # 读取文件内容（自动检测编码）
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # 处理文本内容
            new_content = process_text(content)
            
            # 覆盖写入原文件
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
                
        except Exception as e:
            print(f"处理文件 {filename} 时出错: {str(e)}")
            continue
    
    print("=" * 40)
    print(f"处理完成！共处理 {processed_count} 个文件，所有换行符已替换为空格")

if __name__ == "__main__":
    # 设置你的文件夹路径（注意使用原始字符串）
    folder_path = r"提示词"
    process_files(folder_path)