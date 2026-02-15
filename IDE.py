import tkinter as tk
from tkinter import scrolledtext, filedialog
import re
import sys
import subprocess
from interpreter.box_to_py import to_py
import yaml
from interpreter import box_to_json as b2j
import atexit
import os

with open(os.path.expanduser("~/boxedLANG/IDE/BoxSyntax.yaml")) as f:
    syntax = yaml.safe_load(f)


back1 = "#424242"
back2 = "#575757"
text =  "#ffffff"

keywords = syntax['keywords']
operators = syntax['operators']
var_prefix = syntax['variables']['prefix']
special_symbols = syntax['special_symbols']

root = tk.Tk()
root.title("BoxedLANG IDE")
root.geometry("800x600")

def run_code():
    code = editor.get("1.0", tk.END).rstrip()

    try:
        code_json = b2j.make_code_from(code)
        py_code = "import time\n" + to_py(code_json)
    except Exception as e:
        print(f"Translation failed: {str(e)}")
        return

    temp_file = "temp_run_boxed.py"
    def cleanup_temp():
        try:
            os.remove(temp_file)
        except:
            pass

    atexit.register(cleanup_temp)
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(py_code)

        if sys.platform == "win32":
            subprocess.Popen(
                ["cmd", "/k", "python", temp_file, "&", "pause"],
                creationflags=subprocess.CREATE_NEW_CONSOLE
            )
        elif sys.platform == "darwin":
            script = f'python3 "{temp_file}" ; echo ; echo "Press Enter to close..." ; read'
            subprocess.Popen(["osascript", "-e", f'tell application "Terminal" to do script "{script}"'])
        else:
            try:
                subprocess.Popen(["x-terminal-emulator", "-e", f"python3 {temp_file} ; read -p 'Press Enter...'"])
            except:
                try:
                    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"python3 {temp_file} ; read -p 'Press Enter...'"])
                except:
                    print("Couldn't open terminal. Run manually: python3 temp_run_boxed.py")

    except Exception as e:
        print(f"Failed to start run: {str(e)}")

def save_code():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".bx",
        filetypes=[("BoxedLANG files", "*.bx"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(editor.get("1.0", tk.END).rstrip())
            print(f"Saved to {file_path}")
        except Exception as e:
            print(f"Save failed\n{str(e)}")


def open_code():
    file_path = filedialog.askopenfilename(
        filetypes=[("BoxedLANG files", "*.bx"), ("All files", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            editor.delete("1.0", tk.END)
            editor.insert(tk.END, content)
            highlight_code()
            print(f"Opened {file_path}")
        except Exception as e:
            print(f"Open failed\n{str(e)}")


run_btn = tk.Button(text="Run", command=run_code, foreground=text, background=back2)
run_btn.pack(side=tk.TOP, anchor="ne", padx=3, pady=3)

save_btn = tk.Button(text="Save", command=save_code, foreground=text, background=back2)
save_btn.pack(before=run_btn, side=tk.LEFT, anchor="nw", padx=3, pady=3)

open_btn = tk.Button(text="Open", command=open_code, foreground=text, background=back2)
open_btn.pack(after=save_btn, anchor="w", padx=3, pady=3)

editor = scrolledtext.ScrolledText(root, height=20,background=back1, foreground=text)
editor.pack(fill=tk.BOTH, expand=True)

editor.tag_config('keyword', foreground='green')
editor.tag_config('operator', foreground='red')
editor.tag_config('variable', foreground='teal')
editor.tag_config('special', foreground='purple')
editor.tag_config('default', foreground=text)


def highlight_code(event=None):
    content = editor.get("1.0", tk.END)
    editor.tag_add('default', "1.0", tk.END)
    editor.tag_remove('keyword', "1.0", tk.END)
    editor.tag_remove('operator', "1.0", tk.END)
    editor.tag_remove('variable', "1.0", tk.END)
    editor.tag_remove('special', "1.0", tk.END)

    for kw in keywords:

        for m in re.finditer(r'\b' + re.escape(kw) + r'\b', content):
            start = f"1.0 + {m.start()} chars"
            end = f"1.0 + {m.end()} chars"
            editor.tag_remove('default', "1.0", tk.END)
            editor.tag_add('keyword', start, end)

    for op in operators:
        for m in re.finditer(re.escape(op), content):
            start = f"1.0 + {m.start()} chars"
            end = f"1.0 + {m.end()} chars"
            editor.tag_remove('default', "1.0", tk.END)
            editor.tag_add('operator', start, end)

    for m in re.finditer(r'\$[A-Za-z_][A-Za-z0-9_]*', content):
        start = f"1.0 + {m.start()} chars"
        end = f"1.0 + {m.end()} chars"
        editor.tag_remove('default', "1.0", tk.END)
        editor.tag_add('variable', start, end)

    for sym in special_symbols:
        for m in re.finditer(re.escape(sym), content):
            start = f"1.0 + {m.start()} chars"
            end = f"1.0 + {m.end()} chars"
            editor.tag_remove('default', "1.0", tk.END)
            editor.tag_add('special', start, end)


editor.bind("<KeyRelease>", highlight_code)

root.mainloop()