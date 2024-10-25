import fitz  # PyMuPDF
import os


def pdf_to_images(pdf_path, output_dir):
    # 检查输出目录是否存在，如果不存在则创建
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

        # 打开PDF文件
    pdf_document = fitz.open(pdf_path)

    # 遍历PDF的每一页
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)  # 加载页面
        pix = page.get_pixmap()  # 获取页面的像素图

        # 设置输出图片的文件名
        image_filename = os.path.join(output_dir, f"page_{page_num + 1}.png")

        # 保存图片到文件
        pix.save(image_filename)

        # 关闭PDF文件
    pdf_document.close()
    print(f"PDF分拆完成，图片保存在 {output_dir}")


# 示例使用
pdf_path = "/Users/gdhjx/Downloads/儿童游戏.pdf"  # 替换为你的PDF文件路径
output_dir = "/Users/gdhjx/Documents/test"  # 替换为你想要保存图片的目录
pdf_to_images(pdf_path, output_dir)