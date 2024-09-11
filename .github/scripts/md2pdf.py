#
# md2pdf.py
#
# Carl Zeiss GOM Metrology GmbH, 2024
#
# ---
'''Convert Markdown document to PDF'''
import sys
from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=4)
pdf.add_section(Section(open(sys.argv[1], encoding='utf-8').read(), toc=False), user_css="body {font-family: sans-serif;}")
pdf.meta["title"] = "Releasenotes"
pdf.save(sys.argv[2])
