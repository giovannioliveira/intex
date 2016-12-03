#!/usr/bin/python3
import sys,os,easygui as eg
from bs4 import BeautifulSoup
from PyQt5 import QtWidgets as qtw


def set_iframe(entry, href):
    entry.contents[0].append(
        BeautifulSoup('<iframe style="width:100%; height:100%;" src="{0}" frameborder="0" allowfullscreen></iframe>'
                      .format(href),'html.parser'))

setters = {'iframe':set_iframe}

def abort(message):
    eg.msgbox(message)
    sys.exit(0)

def main(argv):
    src = None
    if len(argv) == 2:
        src = argv[1]
    else:
        dlg = qtw.QFileDialog()
        dlg.setFileMode(qtw.QFileDialog.ExistingFile)
        dlg.setFilter("PDF files (*.pdf)")
        dlg.exec()
        src = dlg.selectedFile()
#        src = eg.fileopenbox('source pdf',filetypes=['*.pdf'])
    if not src:
        sys.exit(0)
        
    try:
        f=open(src)
        src = f.name
        f.close()
    except FileNotFoundError:
        abort('%s not found'%src)

    srcname = src.split('/')[-1].replace('.pdf','')
    destname = eg.diropenbox('save files to:')
    if not destname:
        sys.exit(0)

    dest = destname + '/' + srcname + '.pdf'
    ret = os.system('gs -sDEVICE=pdfwrite -sOutputFile=%s -dNOPAUSE -dBATCH %s'%(dest, src))
    if ret:
        abort('error while trying to run ghostscript')

    ret = os.system('pdf2htmlEX --dest-dir %s --embed cfij --process-nontext 1 %s'%(destname,dest))
    if ret:
        abort('error while trying to run pdf2htmlEX')

    ht = destname + '/' + srcname + '.html'
    htfile = open(ht)

    soup = BeautifulSoup(htfile, 'html.parser')
    global setters
    for tag in soup.find_all('a'):
        href = tag.get('href')
        suffix = href.split('.')[-1]
        if suffix in setters.keys():
            newhref = href.replace('.'+suffix,'')
            setters[suffix](tag,newhref)

    with open(ht, "w") as file:
        file.write(str(soup))

    htfile.close()


if __name__ == "__main__":
    main(sys.argv)
