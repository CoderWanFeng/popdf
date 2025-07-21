# pip install pymupdf pillow
import pymupdf  # PyMuPDF
from pathlib import Path
import PIL.Image
import io


def extract_images_from_pdf(
        pdf_path: str,
        out_dir: str = ".",
        prefix: str = "img"
):
    """
    把 pdf_path 里的所有图片提取成独立文件，保存在 out_dir。
    文件名形如：img-001.png、img-002.jpg ……
    """
    pdf_path = Path(pdf_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    doc = pymupdf.open(pdf_path)

    img_idx = 0
    for page_index in range(len(doc)):
        for img in doc.get_page_images(page_index):
            # img: (xref, smask, width, height, bpc, colorspace, ...)
            xref = img[0]
            base_image = doc.extract_image(xref)
            if base_image is None:
                continue

            img_idx += 1
            ext = base_image["ext"]  # 自动识别扩展名：png, jpeg, jbig2, ccitt ……
            image_bytes = base_image["image"]
            save_path = out_dir / f"{prefix}-{img_idx:03d}.{ext}"

            # 对于 JPEG/PNG 直接写磁盘
            if ext in {"png", "jpeg"}:
                save_path.write_bytes(image_bytes)
            else:
                # 其它格式用 Pillow 统一转 PNG
                image = PIL.Image.open(io.BytesIO(image_bytes))
                image.save(save_path.with_suffix(".png"))

            print(f"Saved {save_path}")


if __name__ == "__main__":
    # import argparse
    # parser = argparse.ArgumentParser(description="Extract images from PDF")
    # parser.add_argument("pdf", help="输入 PDF 文件")
    # parser.add_argument("-o", "--out", default=".", help="输出目录")
    # parser.add_argument("-p", "--prefix", default="img", help="文件名前缀")
    # args = parser.parse_args()

    # extract_images_from_pdf(args.pdf, args.out, args.prefix)
    pdf = r'./files/test.pdf'
    out = r'./imgs'
    prefix = 'img'
    extract_images_from_pdf(pdf, out, prefix)
