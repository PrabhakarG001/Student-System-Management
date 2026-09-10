import tkinter as tk
from tkinter import messagebox as mb
import logic, styles

class App:
    def __init__(self, root):
        root.title("Student Management"); root.geometry("600x500"); root.configure(bg=styles.BG)
        tk.Label(root, text="Student Management System", font=("Helvetica", 20, "bold"), bg=styles.HDR, fg="white").pack(fill=tk.X, pady=10)
        
        i_frm, self.e = tk.Frame(root, bg=styles.BG), {}
        i_frm.pack(pady=10)
        for i, k in enumerate(["ID", "Name", "Marks"]):
            tk.Label(i_frm, text=f"{k}:", **styles.LBL).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            (ent := tk.Entry(i_frm, **styles.ENT)).grid(row=i, column=1, padx=10, pady=5)
            self.e[k] = ent

        b_frm = tk.Frame(root, bg=styles.BG)
        b_frm.pack(pady=5)
        for i, (txt, cmd) in enumerate([("Add", self.add), ("Search", self.src), ("Delete", self.del_), ("Clear", self.clr)]):
            bg, abg = styles.COLORS[txt]
            tk.Button(b_frm, text=txt, bg=bg, activebackground=abg, command=cmd, **styles.BTN).grid(row=0, column=i, padx=5)

        d_frm = tk.Frame(root, bg=styles.BG, bd=2, relief="sunken")
        d_frm.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.lb = tk.Listbox(d_frm, **styles.LB)
        self.lb.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.upd()

    def add(self):
        v = [e.get().strip() for e in self.e.values()]
        if not all(v): return mb.showerror("Error", "All fields required!")
        s, m = logic.add_student(*v)
        mb.showinfo("Result", m); self.clr() if s else None

    def src(self):
        i = self.e["ID"].get().strip()
        if not i: return mb.showerror("Error", "Enter ID")
        s = logic.get_student(i)
        self.upd([s]) if s else mb.showinfo("Result", "Not found!")

    def del_(self):
        i = self.e["ID"].get().strip()
        if not i: return mb.showerror("Error", "Enter ID")
        s, m = logic.delete_student(i)
        mb.showinfo("Result", m); self.clr() if s else None

    def clr(self):
        [e.delete(0, tk.END) for e in self.e.values()]
        self.upd()

    def upd(self, d=None):
        self.lb.delete(0, tk.END)
        for s in (d or logic.students):
            self.lb.insert(tk.END, f" ID: {s['id']:<10} | Name: {s['name']:<15} | Marks: {s['marks']}")

def run_app():
    r = tk.Tk(); App(r); r.mainloop()
