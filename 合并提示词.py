import os

def process_file(content):
    """处理单个文件内容：首行添加4个空格，保留原有换行"""
    lines = content.splitlines(keepends=True)  # 保留换行符分割
    if not lines:
        return ""
    lines[0] = "    " + lines[0].lstrip()  # 首行添加4空格并去原左空格
    return "".join(lines)

def merge_txt_files(source_folder, output_file):
    """合并文本文件主函数"""
    # 获取绝对路径
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(base_dir, source_folder)
    output_path = os.path.join(base_dir, output_file)

    with open(output_path, "w", encoding="utf-8") as merged_file:
        # 按文件名排序处理
        for filename in sorted(os.listdir(source_path)):
            if filename.endswith(".txt"):
                file_path = os.path.join(source_path, filename)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        processed = process_file(content)
                        merged_file.write(processed)
                        merged_file.write("\n\n")  # 文件之间添加两个空行分隔
                except Exception as e:
                    print(f"处理文件 {filename} 时出错：{str(e)}")

    print(f"合并完成！共处理 {len(os.listdir(source_path))} 个文件")
    print(f"输出文件位置：{output_path}")

if __name__ == "__main__":
    # 参数配置
    SOURCE_FOLDER = "提示词"    # 需要合并的文件夹名称
    OUTPUT_FILE = "提示词合并.txt"  # 输出文件名
    
    merge_txt_files(SOURCE_FOLDER, OUTPUT_FILE)