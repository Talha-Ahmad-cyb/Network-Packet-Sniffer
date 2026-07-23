import tkinter as tk
from tkinter import ttk,messagebox
class PacketSnifferGUI:
    def __init__(self,root):
        self.root=root
        root.title("Packet Sniffer")
        ttk.Label(root,text="Network Packet Sniffer",font=("Arial",16)).pack()
        btns=ttk.Frame(root);btns.pack()
        ttk.Button(btns,text="Start").pack(side="left",padx=5)
        ttk.Button(btns,text="Stop").pack(side="left",padx=5)
        cols=("Time","Source","Destination","Protocol")
        self.tree=ttk.Treeview(root,columns=cols,show="headings")
        for c in cols:self.tree.heading(c,text=c)
        self.tree.pack(fill="both",expand=True)
