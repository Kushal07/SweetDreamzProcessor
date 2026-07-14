import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading, os
from ..services.controller import SweetDreamzController

class SweetDreamzGUI:
    def __init__(self, root):
        self.root = root; self.root.title('Commercial Sorting Processor'); self.root.geometry('1150x650'); self.root.configure(bg='#E5E4D7')
        self.ctrl = SweetDreamzController(); self.file = ''; self._build()

    def _build(self):
        tk.Label(self.root, text='Wellcome to Automated Excel Workbook Processing & Arrangement', bg='#E5E4D7', fg='#E67E22', font=('Comic Sans MS', 18, 'bold')).pack(pady=20)
        c_p = tk.Frame(self.root, bg='black', padx=2, pady=2); c_p.pack(pady=10)
        self.p = tk.Canvas(c_p, width=800, height=35, bg='white', highlightthickness=0); self.p.pack()
        self.st = tk.Label(self.root, text='', bg='#E5E4D7', font=('Arial', 11, 'bold'), fg='#2C3E50'); self.st.pack()
        mid = tk.Frame(self.root, bg='#E5E4D7'); mid.pack(fill='both', expand=True, padx=60, pady=20)
        self.dc = tk.Canvas(mid, width=580, height=280, bg='white', highlightthickness=0); self.dc.pack(side='left')
        self.dc.create_rectangle(2, 2, 578, 278, outline='#00FFCC', width=4)
        self.log = tk.Label(self.dc, text='System Online.', bg='white', font=('Consolas', 10), anchor='nw', justify='left', wraplength=540); self.log.place(x=20, y=20, width=540, height=240)
        br = tk.Frame(mid, bg='#E5E4D7'); br.pack(side='right', padx=40)
        self.b1 = tk.Button(br, text='Browse the file', bg='#FF3B30', fg='white', font=('Arial', 12, 'bold'), width=22, height=2, command=self.browse, relief='flat'); self.b1.pack(pady=10)
        self.b2 = tk.Button(br, text='Process Data', bg='#5856D6', fg='white', font=('Arial', 12, 'bold'), width=22, height=2, command=self.proc, relief='flat'); self.b2.pack(pady=10)
        self.b3 = tk.Button(br, text='Save Your Data', bg='#5856D6', fg='white', font=('Arial', 12, 'bold'), width=22, height=2, state='disabled', command=self.save, relief='flat'); self.b3.pack(pady=10)
        ft = tk.Frame(self.root, bg='#E5E4D7'); ft.pack(side='bottom', pady=15)
        tk.Label(ft, text='© 2026 Kushal Bera', bg='#E5E4D7', font=('Arial', 9)).pack()
        tk.Label(ft, text='Developed & Maintained by Kushal Bera', bg='#E5E4D7', fg='#2C3E50', font=('Arial', 10, 'bold')).pack()
        tk.Label(ft, text='Thank you for using Sorting Processor. Enjoy your work! 🚀', bg='#E5E4D7', fg='#5856D6', font=('Arial', 10)).pack()

    def browse(self):
        p = filedialog.askopenfilename(filetypes=[('Excel Files', '*.xlsx')])
        if p: self.file = p; self.log.config(text='Source Path:\n' + str(p))

    def proc(self):
        if not self.file: return
        self.b2.config(state='disabled'); self.b1.config(state='disabled'); self.st.config(text='Processing Your Data')
        threading.Thread(target=self.logic, daemon=True).start()

    def logic(self):
        try:
            if self.ctrl.process(self.file, self.upd): self.root.after(100, self.succ)
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror('System Error', str(e)))
            self.root.after(0, lambda: self.b2.config(state='normal'))

    def upd(self, v, m):
        self.root.after(0, lambda: [self.p.delete('bk'), [self.p.create_rectangle(5+(i*66), 4, 5+(i*66)+60, 31, fill='#40C4FF', outline='', tags='bk') for i in range(int((v/100)*12))], self.log.config(text=m)])

    def succ(self):
        self.st.config(text='Arrangement Complete!')
        w = tk.Toplevel(self.root); w.title('Export Ready'); w.geometry('550x350'); w.configure(bg='#F8F9FA'); w.grab_set()
        tk.Label(w, text='🎉', font=('Arial', 40), bg='#F8F9FA').pack(pady=(20,0))
        tk.Label(w, text='Success!', font=('Arial', 24, 'bold'), bg='#F8F9FA', fg='#28A745').pack(pady=10)
        tk.Label(w, text='Your workbook has been reflowed and is ready for export.\nPlease choose your destination folder.', bg='#F8F9FA', font=('Arial', 12), justify='center').pack(pady=10)
        tk.Button(w, text='Continue to Save', font=('Arial', 11, 'bold'), width=20, bg='#007BFF', fg='white', command=lambda: [w.destroy(), self.b3.config(state='normal')], relief='flat').pack(pady=20)

    def save(self):
        f = os.path.basename(self.file).replace('.xlsx', '_Modified_KB.xlsx')
        p = filedialog.asksaveasfilename(initialfile=f, defaultextension='.xlsx', filetypes=[('Excel', '*.xlsx')])
        if p:
            self.ctrl.save(p)
            # Custom styled Save success
            sw = tk.Toplevel(self.root); sw.geometry('400x200'); sw.configure(bg='white'); sw.title('Stored')
            tk.Label(sw, text='Saved Successfully!', font=('Arial', 14, 'bold'), bg='white', fg='#46AB21').pack(pady=30)
            tk.Button(sw, text='Close', width=10, command=lambda: [sw.destroy(), self.b3.config(state='disabled'), self.b1.config(state='normal'), self.b2.config(state='normal')]).pack()
