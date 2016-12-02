#!/usr/bin/python3
import sys, os
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup

#region iframe
def set_iframe(entry, href):
    entry.contents[0].append(
        BeautifulSoup('<iframe style="width:100%; height:100%;" src="{0}" frameborder="0" allowfullscreen></iframe>'
                      .format(href),'html.parser'))
setters = {'video':set_iframe,'applet':set_iframe}
#endregion iframe

#region dialog
def message(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

def select_file(type=QFileDialog.ExistingFile):
    dlg = QFileDialog()
    dlg.setFileMode(type)
    return dlg.selectedFiles() if dlg.exec() else None
#endregion dialog

def main():
    app = QApplication(sys.argv)
    if len(sys.argv)>1:
        src = sys.argv[1]
    else:
        sel = select_file()
        src = sel[0] if sel else None
    if not src:
        sys.exit(0)
    srcname = src.split('/')[-1].replace('.pdf','')
    destname = select_file(QFileDialog.Directory)
    if not destname:
        sys.exit(0)
    destname = destname[0]
    dest = destname + '/' + srcname + '.pdf'
    ret = os.system('gs -sDEVICE=pdfwrite -sOutputFile=%s -dNOPAUSE -dBATCH %s' % (dest, src))
    if ret:
        message('error while trying to run ghostscript')
        sys.exit(1)

    ret = os.system('pdf2htmlEX --dest-dir %s --embed cfij --process-nontext 1 %s' % (destname, dest))
    if ret:
        message('error while trying to run pdf2htmlEX')
        sys.exit(1)

    ht = destname + '/' + srcname + '.html'
    htfile = open(ht)

    soup = BeautifulSoup(htfile, 'html.parser')
    global setters
    for tag in soup.find_all('a'):
        href = tag.get('href')
        suffix = href.split('#')[-1]
        if suffix in setters.keys():
            newhref = href.replace('#' + suffix, '')
            setters[suffix](tag, newhref)

    with open(ht, "w") as file:
        file.write(str(soup))

    htfile.close()
    message('document successfully exported to %s' % destname)

if __name__ == '__main__':
    main()