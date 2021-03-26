"""
@author GanciDev
"""
import sys
import os
from pdfrw import PdfReader, PdfWriter, PageMerge


def sizepage(page):
    result = PageMerge()
    result.add(page)
    return result[0].w, result[0].h


def fixpage(page, width,height):
    result = PageMerge()
    result.add(page)
    if width > height:
        if width > 842:
            result[0].w = height * 1.6
            result[0].x = 50
        else:
            result[0].x = 0
            result[0].w = height * 1.4
    else:
        if height > 842:
            result[0].y = 125
        result[0].w = width
        result[0].x = 0
    return result.render()


def filigrana(tipo, opacita, input_file, output_file):
    reader_input = PdfReader(input_file)
    writer_output = PdfWriter()

    page=reader_input.pages[0]
    w,h = sizepage(page)

    if tipo=="logo":
        if int(w) > int(h):
            watermark_input=PdfReader("filigrane/fil_"+str(opacita)+"_logo_or.pdf")
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))
        else:
            watermark_input=PdfReader("filigrane/fil_"+str(opacita)+"_logo_ver.pdf")
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))
    else:
        if int(w) > int(h):
            watermark_input=PdfReader("filigrane/fil_"+str(opacita)+"_or.pdf")
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))
        else:
            watermark_input=PdfReader("filigrane/fil_"+str(opacita)+"_ver.pdf")
            watermark = fixpage(watermark_input.pages[0],int(w),int(h))

    for current_page in range(len(reader_input.pages)):
        merger = PageMerge(reader_input.pages[current_page])
        merger.add(watermark).render()
    writer_output.write(output_file, reader_input)


def main():
    print(f"{sys.argv[1]}, {sys.argv[2]}, {sys.argv[3]}, {sys.argv[3].replace('.pdf','_f.pdf')}")
    # DEVO RISCRIVERE LA FUNZIONE
    filigrana(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[3].replace(".pdf","_f.pdf"))
    os.system("chmod -R 777 documenti")


if __name__ == "__main__":
    main()