# 多进程源文件拷贝器
import os
import multiprocessing


def copy_file(file_name, dest_dir, source_dir):
    # 完成地址设置,拼接路径
    dest_path = dest_dir + "/" + file_name
    source_path = source_dir + "/" + file_name
    # 打开源文件 ,转录源文件
    with open(source_path, "r") as source_file:
        with open(dest_path, "w") as dest_file:
            while True:
                data = source_file.readline()
                if data:
                    dest_file.write(data)
                else:
                    break

        pass


if __name__ == "__main__":
    # 定义目标文件夹以及源文件夹
    source_file = "D:\Code\python\8_31"
    dest_file = "D:\Code\python\copy"
    # 创建文件夹
    try:
        os.mkdir(dest_file)

    except:
        print("文件已经存在")
        pass
    # 读取拷贝文件的目录
    file_list = os.listdir(source_file)
    # 使用循环进行拷贝
    for ls in file_list:
        copy_processing = multiprocessing.Process(target=copy_file, args=(ls, dest_file, source_file))
        copy_processing.start()
        pass

    pass
