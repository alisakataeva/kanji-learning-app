from tkinter import *
import sqlite3

class App:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.save = Button(frame, text="Save into db", command=self.insert)
		self.save.pack(side=LEFT)

		self.frame_eng = Frame(width=768, height=576, colormap="new")
		self.frame_eng.pack(fill=X, padx=5)
		self.label_eng = Label(self.frame_eng, text="English")
		self.label_eng.pack()
		self.eng = Entry(self.frame_eng)
		self.eng.pack()

		self.frame_hg = Frame(width=768, height=576, colormap="new")
		self.frame_hg.pack(fill=X, padx=5)
		self.label_hg = Label(self.frame_hg, text="Hiragana")
		self.label_hg.pack()
		self.hg = Entry(self.frame_hg)
		self.hg.pack()
		
		self.frame_kk = Frame(width=768, height=576, colormap="new")
		self.frame_kk.pack(fill=X, padx=5)
		self.label_kk = Label(self.frame_kk, text="Katakana")
		self.label_kk.pack()
		self.kk = Entry(self.frame_kk)
		self.kk.pack()
		
		self.frame_kj = Frame(width=768, height=576, colormap="new")
		self.frame_kj.pack(fill=X, padx=5)
		self.label_kj = Label(self.frame_kj, text="Kanji")
		self.label_kj.pack()
		self.kj = Entry(self.frame_kj)
		self.kj.pack()
		
	
	def say_hi(self):
		print("hi there, eberyone!")
		
	def insert(self):
		con = sqlite3.connect('d:/~/Sandbox/japanese/mydb.sqlite')
		cur = con.cursor()
		query = """
		INSERT INTO idols VALUES ("{}", "{}", "{}", "{}")
		""".format(
			self.eng.get(),
			self.hg.get(),
			self.kk.get(),
			self.kj.get()
		)
		cur.execute(query)
		con.commit()
		con.close()
		self.eng.delete(0, END)
		self.hg.delete(0, END)
		self.kk.delete(0, END)
		self.kj.delete(0, END)
		

root = Tk()

app = App(root)

root.mainloop()
root.destroy()