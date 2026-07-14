import os

def create_file(path, content):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    if folder and "src" in folder:
        init = os.path.join(folder, "__init__.py")
        if not os.path.exists(init):
            with open(init, "w") as fi: fi.write("# init")

# --- COMMERCIAL DOCS CONTENT ---
DEVELOPER = "Kushal Bera"
COPYRIGHT = "Copyright © 2026 Kushal Bera. All Rights Reserved."

BUS_SPEC = f"""# Business Specification: SweetDreamzProcessor
## 1. Executive Summary
Designed by {DEVELOPER}, this software automates the transformation of lottery data into analytical grids. 

## 2. Core Business Rules
- **Data Integrity:** Source columns A, B, and C are immutable.
- **Sorting Logic:** Numbers are decomposed into Series (1st digit), Middle Pair (2-3), and Last Pair (4-5).
- **Arrangement Types:** 
  1. Number Wise: Sorted by Middle Pair.
  2. Last Digit: Sorted by Last Pair.
- **Commercial Aesthetics:** Professional color coding (Blue/Yellow/Green) and specific line-counts for prize strings.

## 3. Legal & Ownership
{COPYRIGHT}
"""

SDS_SPEC = f"""# Software Design Specification
## 1. Technical Architecture
- **Fresh Start Engine:** To combat Excel XML ghost rules, the system deletes all old sheets and recreates them.
- **Style Injection:** Uses Direct Styling (Fill/Font/Alignment) instead of Conditional Formatting to ensure zero performance degradation at scale.

## 2. Formatting Standards
- **Date:** Long Date format (dddd, dd mmmm yyyy).
- **Wrapping:** 1st Prize (2 lines), 2nd Prize (3 lines).
- **Grid:** Freeze Panes enabled at Column B and Row 2.
"""

ARCH_DOC = f"""# System Architecture
## 1. Layered Pattern
- **UI Layer:** Tkinter-based event loop.
- **Application Layer:** Orchestrates the 'Nuclear Wipe' and 'Data Reflow'.
- **Persistence Layer:** Openpyxl-driven direct cell manipulation.

## 2. The 'Rebirth' Algorithm
Every sheet is duplicated into a memory buffer, the old sheet is destroyed, and a fresh grid is built to ensure total removal of hidden Excel rule caches.
"""

TEST_DOC = f"""# Test Strategy
## 1. Stress Tests
Verified against 'Sweet Dreamz - Deleted.xlsx' which contains fragmented columns and shifted rules.
## 2. Visual Regression
Ensured that Block 32 (Number Wise) and Block 43 (Last Digit) maintain color isolation using Direct Paint method.
"""

# --- SOURCE CODE DEFINITIONS ---

main_src = """import tkinter as tk
from src.ui.main_window import SweetDreamzGUI
if __name__ == '__main__':
    root = tk.Tk()
    app = SweetDreamzGUI(root)
    root.mainloop()
"""

models_src = """from dataclasses import dataclass
@dataclass
class LotteryNumber:
    full_number: str; series: str; middle_pair: str; last_pair: str
    @classmethod
    def from_str(cls, value):
        v = str(value).strip().zfill(5)
        if len(v) == 5 and v.isdigit(): return cls(v, v[0], v[1:3], v[3:5])
        return None
"""

proc_src = """import re, math
class NumberExtractor:
    def extract_numbers(self, val):
        return re.findall(r'\\b\\d{5}\\b', str(val or ""))
    def format_prize_text(self, val, lines_count):
        nums = self.extract_numbers(val)
        if not nums: return ""
        n = len(nums)
        per_line = math.ceil(n / lines_count)
        lines = []
        for i in range(0, n, per_line):
            lines.append(" ".join(nums[i:i + per_line]))
        return "\\n".join(lines[:lines_count]).strip()
"""

grid_src = """from openpyxl.styles import PatternFill, Font, Alignment
class GridManager:
    def __init__(self, wb):
        self.wb = wb
        self.fill_s = PatternFill(start_color='99D6EA', end_color='99D6EA', fill_type='solid')
        self.fill_y = PatternFill(start_color='FFB600', end_color='FFB600', fill_type='solid')
        self.fill_g = PatternFill(start_color='46AB21', end_color='46AB21', fill_type='solid')
        self.h_font = Font(bold=True, size=10)
        self.align = Alignment(wrap_text=True, vertical='top', horizontal='center')

    def recreate_clean_sheet(self, old_name):
        old_ws = self.wb[old_name]
        new_ws = self.wb.create_sheet(old_name + '_CLEAN')
        new_ws.freeze_panes = 'B2'
        new_ws.column_dimensions['A'].width, new_ws.column_dimensions['B'].width, new_ws.column_dimensions['C'].width = 30, 45, 45
        
        for c, txt in enumerate(['Date', '1st Prize', '2nd Prize'], 1):
            cell = new_ws.cell(1, c, value=txt)
            cell.font, cell.alignment = self.h_font, self.align
        
        is_ld = 'last' in old_name.lower() or 'digit' in old_name.lower()
        for i in range(100):
            pv, base = str(i).zfill(2), 4 + (i * 3)
            if not is_ld: h_data = [(f'S_{pv}', self.fill_s), (pv, self.fill_y), (f'B_{pv}', self.fill_g)]
            else: h_data = [(f'S_{pv}', self.fill_s), (f'B_{pv}', self.fill_g), (pv, self.fill_y)]
            for idx, (txt, fill) in enumerate(h_data):
                c = new_ws.cell(1, base + idx, value=txt)
                c.font, c.alignment, c.fill = self.h_font, self.align, fill
                new_ws.column_dimensions[c.column_letter].width = 10
        del self.wb[old_name]; new_ws.title = old_name; return new_ws
"""

writer_src = """from openpyxl.styles import PatternFill, Alignment
class WorkbookWriter:
    def __init__(self):
        self.fill_s = PatternFill(start_color='99D6EA', end_color='99D6EA', fill_type='solid')
        self.fill_y = PatternFill(start_color='FFB600', end_color='FFB600', fill_type='solid')
        self.fill_g = PatternFill(start_color='46AB21', end_color='46AB21', fill_type='solid')
        self.align = Alignment(wrap_text=True, vertical='top', horizontal='center')
    def write_block(self, ws, r, c, data, is_ld=False):
        c1 = ws.cell(r, c, value=data[0]); c1.fill, c1.alignment = self.fill_s, self.align
        c2, c3 = ws.cell(r, c+1, value=data[1]), ws.cell(r, c+2, value=data[2])
        if not is_ld: c2.fill, c3.fill = self.fill_y, self.fill_g
        else: c2.fill, c3.fill = self.fill_g, self.fill_y
        c2.alignment, c3.alignment = self.align, self.align
"""

ctrl_src = """from openpyxl import load_workbook
from ..business.models import LotteryNumber
from ..business.processor import NumberExtractor
from ..workbook.grid_manager import GridManager
from ..workbook.writer import WorkbookWriter

class SweetDreamzController:
    def __init__(self): self.wb = None
    def process(self, path, callback):
        self.wb = load_workbook(path)
        ex, wr, grid = NumberExtractor(), WorkbookWriter(), GridManager(self.wb)
        names = list(self.wb.sheetnames)
        for s_idx, sn in enumerate(names):
            old_ws = self.wb[sn]; src_data = []
            for r in range(2, old_ws.max_row + 1):
                src_data.append((old_ws.cell(r,1).value, old_ws.cell(r,2).value, old_ws.cell(r,3).value))
            is_ld = 'last' in sn.lower() or 'digit' in sn.lower()
            ws = grid.recreate_clean_sheet(sn)
            for r_idx, (d_v, p1_v, p2_v) in enumerate(src_data):
                rn = r_idx + 2
                ws.cell(rn, 1, value=d_v).number_format = 'dddd, dd mmmm yyyy'
                ws.cell(rn, 1).alignment = grid.align
                ws.cell(rn, 2, value=ex.format_prize_text(p1_v, 2)).alignment = grid.align
                ws.cell(rn, 3, value=ex.format_prize_text(p2_v, 3)).alignment = grid.align
                p1_n, p2_n = [LotteryNumber.from_str(n) for n in ex.extract_numbers(p1_v)], [LotteryNumber.from_str(n) for n in ex.extract_numbers(p2_v)]
                if not p1_n and not p2_n: continue
                row_map = {}
                for p in (p1_n + p2_n):
                    key = p.last_pair if is_ld else p.middle_pair
                    if key not in row_map: row_map[key] = ([], [], [])
                    row_map[key][0].append(p.series); row_map[key][1].append(p.middle_pair); row_map[key][2].append(p.last_pair)
                for k, v in row_map.items():
                    wr.write_block(ws, rn, 4+(int(k)*3), (','.join(v[0]), ','.join(v[1]), ','.join(v[2])), is_ld)
                if rn % 10 == 0: callback((s_idx/len(names)) + ((r_idx/len(src_data))/len(names))*100, f"Processing {sn}...")
        callback(100, "Done!")
        return True
    def save(self, path): self.wb.save(path)
"""

ui_src = """import tkinter as tk
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
        if p: self.file = p; self.log.config(text='Source Path:\\n' + str(p))

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
        tk.Label(w, text='Your workbook has been reflowed and is ready for export.\\nPlease choose your destination folder.', bg='#F8F9FA', font=('Arial', 12), justify='center').pack(pady=10)
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
"""

# --- EXECUTION ---
print("Generating Commercial Software Package v10.0...")
create_file("main.py", main_src)
create_file("src/business/models.py", models_src)
create_file("src/business/processor.py", proc_src)
create_file("src/workbook/grid_manager.py", grid_src)
create_file("src/workbook/writer.py", writer_src)
create_file("src/services/controller.py", ctrl_src)
create_file("src/ui/main_window.py", ui_src)

# Full Documentation Library
create_file("docs/Business_Specification.md", BUS_SPEC)
create_file("docs/Software_Design_Specification.md", SDS_SPEC)
create_file("docs/Architecture.md", ARCH_DOC)
create_file("docs/TestStrategy.md", TEST_DOC)
create_file("docs/governance/Developer_Guide.md", "## Dev Guide\\nPython 3.10+, openpyxl 3.1.2. Built for Kushal Bera.")
create_file("docs/governance/CHANGELOG.md", "## v10.0\\n- Redesigned Success Dialog\\n- Full Technical Documentation Suite\\n- Perfect Row Reflow logic.")
create_file("docs/governance/ROADMAP.md", "## Future\\n- AI Prediction integration\\n- Web portal deployment.")

print("Success! Version 10.0 (Commercial Standard) deployed.")
