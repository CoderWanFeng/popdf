# -*- coding: utf-8 -*-
import os
import sys
import click
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

import popdf


def _convert_single(args):
    """单文件转换（供并行调用）"""
    input_file, output_file = args
    popdf.pdf2docx(input_file=input_file, output_file=output_file)
    return input_file


@click.command()
@click.option('-i', '--input', 'input_file', help='输入PDF文件路径（单个）')
@click.option('-o', '--output', 'output_file', help='输出Word文件路径（单个）')
@click.option('-p', '--path', 'input_path', help='输入文件夹路径（批量转换）')
@click.option('-op', '--output-path', 'output_path', help='输出文件夹路径（批量）')
@click.option('-t', '--threads', default=4, show_default=True, help='并行转换的线程数')
@click.option('-v', '--verbose', is_flag=True, help='显示详细输出')
def pdf2word(input_file, output_file, input_path, output_path, threads, verbose):
    """PDF转Word转换器 - 支持单个文件和批量并行转换"""
    
    # 批量模式：文件夹 → 文件夹
    if input_path and output_path:
        _batch_convert(input_path, output_path, threads, verbose)
    # 单个文件模式
    elif input_file and output_file:
        _single_convert(input_file, output_file, verbose)
    else:
        click.echo("用法错误：", err=True)
        click.echo("  单个转换: pdf2word -i input.pdf -o output.docx")
        click.echo("  批量转换: pdf2word -p ./pdfs/ -op ./docs/")
        sys.exit(1)


def _single_convert(input_file, output_file, verbose):
    """单个文件转换"""
    if not os.path.exists(input_file):
        click.echo(f"错误: 文件不存在 - {input_file}", err=True)
        sys.exit(1)

    if not input_file.lower().endswith('.pdf'):
        click.echo(f"错误: 输入文件必须是PDF格式", err=True)
        sys.exit(1)

    if not output_file.lower().endswith('.docx'):
        output_file += '.docx'

    if verbose:
        click.echo(f"输入文件: {input_file}")
        click.echo(f"输出文件: {output_file}")

    popdf.pdf2docx(input_file=input_file, output_file=output_file)
    click.echo(f"✓ 转换成功: {output_file}")


def _batch_convert(input_path, output_path, threads, verbose):
    """批量并行转换"""
    input_dir = Path(input_path)
    output_dir = Path(output_path)
    
    if not input_dir.is_dir():
        click.echo(f"错误: 输入路径不是有效目录 - {input_path}", err=True)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    # 收集所有PDF文件
    pdf_files = list(input_dir.glob('*.pdf')) + list(input_dir.glob('*.PDF'))
    if not pdf_files:
        click.echo(f"警告: 文件夹中没有PDF文件 - {input_path}")
        return

    # 准备转换任务
    tasks = [
        (str(pdf), str(output_dir / f"{pdf.stem}.docx"))
        for pdf in pdf_files
    ]

    click.echo(f"发现 {len(tasks)} 个PDF文件，使用 {threads} 线程并行转换...")

    success, failed = 0, 0
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(_convert_single, task): task for task in tasks}
        for future in as_completed(futures):
            task = futures[future]
            try:
                future.result()
                success += 1
                if verbose:
                    click.echo(f"✓ {task[0]} → {task[1]}")
            except Exception as e:
                failed += 1
                click.echo(f"✗ {task[0]} 失败: {e}", err=True)

    click.echo(f"\n完成！成功: {success}, 失败: {failed}")


if __name__ == '__main__':
    pdf2word()