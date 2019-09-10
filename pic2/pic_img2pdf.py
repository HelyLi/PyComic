#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import img2pdf


    

def doImg2Pdf(bookname):
    pngList = []
    fileList = os.listdir(os.path.join(os.getcwd(), bookname))
    # print(fileList)
    for filename in fileList:
        jpgfile = os.path.join(os.getcwd(), bookname, filename)
        if os.path.splitext(jpgfile)[1] == '.jpg':
            pngList.append(jpgfile)
        # if not os.path.isfile(filename):
        #     doImg2Pdf(filename)
    pngList.sort()
    print(pngList)
    
    if len(pngList) == 0:
        return
    with open("{0}.pdf".format(bookname), "wb") as f:
        pfn_bytes = img2pdf.convert(pngList)
        f.write(pfn_bytes)
    print("转换完成")

def main():
    fileList = os.listdir(os.getcwd())
    # print(fileList)
    for filename in fileList:
        if not os.path.isfile(filename):
            doImg2Pdf(filename)
            # print(filename)
            

if __name__ == '__main__':
    main()