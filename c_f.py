import os
import shutil

def create_subfolders(folder_path):
    try:
        # 获取原始文件夹中的所有文件
        files = os.listdir(folder_path)
        for filename in files:
            # 构建子文件夹路径
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                # 获取文件名（不包含扩展名）
                base_name = os.path.splitext(filename)[0]
                # 创建同名的子文件夹
                subfolder_path = os.path.join(folder_path, base_name)
                # 处理同名文件
                count = 1
                while os.path.exists(subfolder_path):
                    subfolder_path = os.path.join(folder_path, f"{base_name} ({count})")
                    count += 1
                os.makedirs(subfolder_path, exist_ok=True)
                print(f"已创建子文件夹：{subfolder_path}")
                # 移动文件到子文件夹
                new_file_path = os.path.join(subfolder_path, filename)
                shutil.move(file_path, new_file_path)
                print(f"已将文件移动到子文件夹：{new_file_path}")
        # 删除所有文件夹名称中包含 .DS_Store 的文件夹
        for subfolder in os.listdir(folder_path):
            if ".DS_Store" in subfolder:
                subfolder_path = os.path.join(folder_path, subfolder)
                shutil.rmtree(subfolder_path)
                print(f"已删除文件夹：{subfolder_path}")
        # 一键给所有文件夹编号
        subfolders = sorted([f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))])
        for i, subfolder in enumerate(subfolders, start=1):
            new_subfolder_name = f"{i}. {subfolder}"
            new_subfolder_path = os.path.join(folder_path, new_subfolder_name)
            os.rename(os.path.join(folder_path, subfolder), new_subfolder_path)
            print(f"已重命名子文件夹：{new_subfolder_path}")
    except Exception as e:
        print(f"出现错误：{e}")

if __name__ == "__main__":
    original_folder_path = input("请输入原始文件夹的地址：")
    create_subfolders(original_folder_path)
