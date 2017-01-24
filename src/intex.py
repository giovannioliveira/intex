#!/usr/bin/python3
import sys, os, platform
from os import path
from PyQt5.QtWidgets import *
from bs4 import BeautifulSoup
from conv import Ui_Dialog

def set_iframe(entry, href):
    entry.contents[0].append(
        BeautifulSoup('<iframe style="width:100%; height:100%;" src="{0}" frameborder="0" allowfullscreen></iframe>'
                      .format(href),'html.parser'))
setters = {'video':set_iframe,'applet':set_iframe}

def message(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

def select_file(type=QFileDialog.ExistingFile):
    dlg = QFileDialog()
    dlg.setFileMode(type)
    return dlg.selectedFiles() if dlg.exec() else None

class ConvDialog(QDialog,Ui_Dialog):

    def __init__(self):
        QDialog.__init__(self)
        Ui_Dialog.setupUi(self,self)
        if len(sys.argv)>1:
            self.etIn.setText(sys.argv[1])
            if len(sys.argv)>2:
                self.etOut.setText(sys.argv[2])
        self.set_listeners()
        self.inp,self.out = None,None

    def set_listeners(self):
        self.btIn.clicked.connect(self.on_in)
        self.btOut.clicked.connect(self.on_out)
        self.btBox.button(QDialogButtonBox.Ok).clicked.disconnect()
        self.btBox.button(QDialogButtonBox.Ok).clicked.connect(self.on_ok)

    def on_in(self):
        aux = select_file()
        if aux:
            self.etIn.setText(aux[0])
    def on_out(self):
        aux = select_file(QFileDialog.Directory)
        if aux:
            self.etOut.setText(aux[0])
    def on_ok(self):
        inp,out = self.etIn.text(),self.etOut.text()
        if len(inp)>0 and len(out)>0:
            self.inp,self.out = inp,out
            self.close()

def main():
    app = QApplication(sys.argv)
    if len(sys.argv)>2:
        src,destdir = sys.argv[1:3]
    else:
        aux = ConvDialog()
        aux.exec()
        if aux.inp and aux.out:
            src,destdir = aux.inp,path.normpath(aux.out)
        else:
            sys.exit(1)
    srcname,srcext = path.splitext(path.basename(src))
    dest = path.join(destdir,path.basename(src))
    ostype = platform.system()
    
    if ostype == 'Linux':

        ret = os.system('gs -sDEVICE=pdfwrite -sOutputFile="%s" -dNOPAUSE -dBATCH "%s"' % (dest, src))
        if ret:
            message('error while trying to run ghostscript')
            sys.exit(1)
        ret = os.system('pdf2htmlEX --dest-dir "%s" --embed cfij --process-nontext 1 "%s"' % (destdir, dest))
        if ret:
            message('error while trying to run pdf2htmlEX')
            sys.exit(1)
    elif ostype == 'Windows':
        
        root = getattr(sys,'_MEIPASS',path.dirname(sys.executable)) if getattr(sys,'frozen',False) else path.dirname(path.dirname(path.abspath(__file__)))
        gspath = path.join(root,'lib','win','gs','bin','gswin32.exe')
        p2hpath = path.join(root,'lib','win','pdf2htmlEX','pdf2htmlEX.exe') 

        ret = os.system('%s -sDEVICE=pdfwrite -sOutputFile="%s" -dNOPAUSE -dBATCH "%s"' % (gspath, dest, src))
        if ret:
            message('error while trying to run ghostscript')
            sys.exit(1)
        ret = os.system('%s --dest-dir "%s" --embed cfij --process-nontext 1 "%s"' % (p2hpath, destdir, dest))
        if ret:
            message('error while trying to run pdf2htmlEX')
            sys.exit(1)
    else:
        message('platform system not supported')
        sys.exit(1)

    ht = path.join(destdir,srcname+'.html')
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
    message('document successfully exported to %s' % destdir)

if __name__ == '__main__':
    main()
