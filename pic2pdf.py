import os
# from PIL import Image
from img2pdf import convert


def images_to_pdf(folder_path, output_pdf_path):
    """
    将指定文件夹内的所有图片转换为PDF文件。

    :param folder_path: 包含图片的文件夹路径
    :param output_pdf_path: 输出的PDF文件路径
    """
    # 查找文件夹内的所有图片文件
    images = [os.path.join(folder_path, img) for img in os.listdir(folder_path)
              if img.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    print(sorted(images, key=lambda x: (len(x), x), reverse=False))
    # 使用Pillow和img2pdf将图片列表转换为PDF
    if images:
        with open(output_pdf_path, "wb") as f:
            f.write(convert(sorted(images, key=lambda x: (len(x), x), reverse=False)))
        print(f"PDF文件已生成: {output_pdf_path}")
    else:
        print(f"文件夹 {folder_path} 中没有找到图片文件。")


def process_folder(folder_path):
    """
    处理指定文件夹，将其中的图片合并成PDF文件，文件名以文件夹名命名，并保存在该文件夹内。

    :param folder_path: 要处理的文件夹路径
    """
    # 构造PDF文件的路径
    pdf_name = os.path.basename(folder_path) + '.pdf'
    output_pdf_path = os.path.join(current_dir, pdf_name)  # 放在当前目录下。

    # 调用images_to_pdf函数
    images_to_pdf(folder_path, output_pdf_path)


# 示例：处理当前目录下的所有文件夹# 如果只想处理特定文件夹，直接调用process_folder('特定文件夹的路径')
current_dir = '/Users/gdhjx/Desktop/'
for folder in [f.path for f in os.scandir(current_dir) if f.is_dir()]:
    process_folder(folder)
