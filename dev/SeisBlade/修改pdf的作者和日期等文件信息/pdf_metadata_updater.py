from PyPDF2 import PdfReader, PdfWriter
import os

def update_pdf_info(**metadata_info):
    """
    更新PDF文件的元数据信息
    
    Args:
        metadata_info: 要更新的元数据，可包含：
            - input_pdf: 输入PDF文件名
            - output_pdf: 输出PDF文件名
            - author: 作者
            - title: 标题
            - subject: 主题
            - keywords: 关键词
            - creator: 创建者
            - producer: 制作者
            - creation_date: 创建时间 (格式如: "D:20240101120000")
            - mod_date: 修改时间 (格式如: "D:20240101120000")
    """
    try:
        # 获取输入输出文件名
        input_pdf = metadata_info.get('input_pdf', 'example.pdf')
        output_pdf = metadata_info.get('output_pdf', 'example_new.pdf')
        
        # 获取当前脚本所在目录
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 构建完整的文件路径
        input_path = os.path.join(script_dir, input_pdf)
        output_path = os.path.join(script_dir, output_pdf)
        
        # 检查输入文件是否存在
        if not os.path.exists(input_path):
            print(f"错误：找不到文件 {input_pdf}")
            return False
            
        # 读取PDF
        reader = PdfReader(input_path)
        writer = PdfWriter()
        
        # 复制所有页面
        for page in reader.pages:
            writer.add_page(page)
        
        # 创建元数据字典
        metadata = {}
        
        # 添加用户指定的元数据
        metadata_mapping = {
            'author': '/Author',
            'title': '/Title',
            'subject': '/Subject',
            'keywords': '/Keywords',
            'creator': '/Creator',
            'producer': '/Producer',
            'creation_date': '/CreationDate',
            'mod_date': '/ModDate'
        }
        
        # 添加元数据
        for key, pdf_key in metadata_mapping.items():
            if key in metadata_info:
                metadata[pdf_key] = metadata_info[key]
        
        writer.add_metadata(metadata)
        
        # 保存文件
        with open(output_path, 'wb') as output:
            writer.write(output)
            
        print(f"成功更新PDF，已保存为：{output_pdf}")
        return True
        
    except Exception as e:
        print(f"处理PDF时出错：{str(e)}")
        return False

if __name__ == "__main__":
    # 更新PDF信息
    update_pdf_info(
        input_pdf="example.pdf",
        output_pdf="example_new.pdf",
        author="张三",
        title="测试文档",
        subject="PDF元数据测试",
        keywords="PDF,测试,元数据",
        creator="自定义创建者",
        producer="自定义制作者",
        creation_date="D:20240101120000",
        mod_date="D:20240101120000"
    ) 