'''
Program: filedialogdemo.py
Author: Mike Horan
Date: 10/1/20
p.279-280

Simple GUI based application that highlights the use of file dialog
'''
from breezypythongui import EasyFrame
import tkinter.filedialog

class FileDialogDemo(EasyFrame):
	#Demonstrates the use of a file dialog
	def __init__(self):
		#sets up window and widget
		EasyFrame.__init__(self, title = 'File Dialog Demo')
		self.outputArea = self.addTextArea(text = '', row = 0, column = 0, width = 80, height = 15)
		self.addButton(text = 'Open', row = 1, column = 0, command = self.openFile)

	#Event handlinvg method
	def openFile(self):
		#Pops up open file dialog, if a file is selected, displays its text in the text area and path name in title bar of window
		fList = [("Python files", "*.py"), ("Text files", "*.txt")]
		fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)

		#If the filename is NOT just an empty string, open thefile contents, set the text of the text area and updtate the title of window
		if fileName != '':
			file = open(fileName, 'r')
			text = file.read()
			file.close()
			self.outputArea.setText(text)
			self.setTitle(fileName)

def main():
	#instantiates and pops up window
	FileDialogDemo().mainloop()

main()