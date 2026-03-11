import pathlib as file
import os.path
from colorama import Fore, Back, Style
import time
import sys
from box_to_json import mk, undo_mk
import argparse

import threading, queue

class BoxedVM:
    global def __init__(self):
        # Two mailboxes
        self.inbox  = queue.Queue()  # you → VM
        self.outbox = queue.Queue()  # VM → you    
    def start(self, code, name):
        # Run the VM in the background so both sides work at once
        t = threading.Thread(target=self._run, args=(code,name), daemon=True)
        t.start()
    def send(self, data):
        # YOU drop something in the VM's mailbox
        self.inbox.put(data)
    def recv(self):
        # YOU check your mailbox, waits if nothing is there yet
        return self.outbox.get()
    def _vm_send(self, data):
        # VM drops something in YOUR mailbox
        self.outbox.put(data)
    def _vm_recv(self):
        # VM checks its mailbox, waits if nothing is there yet
        return self.inbox.get()
    def _run(self, code, name):
        print("run")
        start_boxed_code(code, name)
        self._vm_send({"end": "script"})


boxes = {}
marks = {}
l = -1

def get_arg(argnumb, args,boxes):
	try:
		arg = str(args[argnumb])
		for i in range(0, arg.count("$")):
			cur_box = arg.split("$")[arg.count("$")]
			if "~" in cur_box:
				cur_box = cur_box.split("~")[0]
			if ":" in cur_box:
				cur_box = cur_box.split(":")[0]
			arg = arg.replace("$" + cur_box, boxes[cur_box])
		arg = arg.replace("~", " ")
		arg = arg.replace(":", "")
		for i in range(0, arg.count("🗕")):
			cur = arg.split("🗕")[1]
			arg = arg.replace("🗕" + cur, str(len(str(cur))))
	except IndexError:
			arg = ""
	return arg

def test(arg1,arg2,op):
	match op:
						case "==":
							if arg1 == arg2:								
								return True
							else:
								return False
						case "!=":
							if arg1 != arg2:
								return True
							else:
								return False
						case ">":
							if float(arg1) > float(arg2):
								return True
							else:
								return False
						case "<":
							if float(arg1) < float(arg2):								
								return True
							else:
								return False
						case ">=":
							if float(arg1) >= float(arg2):
								return True
							else:
								return False
						case "<=":
							if float(arg1) <= float(arg2):
								return True
							else:
								return False	
						case "<=":
							if float(arg1) <= float(arg2):
								return True
							else:
								return False
							
def math(numb1,numb2,op):
	if op == "+":
		return int(numb1) + int(numb2)
	elif op == "-":
		return int(numb1) - int(numb2)
	elif op == "*" or "x":
		return int(numb1) * int(numb2)
	elif op == "/":
		return int(numb1) / int(numb2)
	elif op == "%":
		return int(numb1) % int(numb2)
		
def handle_command(command):
	global boxes
	global marks
	global l
	try:
		args = command['args']
		match command['cmd']:
				case "box" | "b":
					boxes = boxes | {get_arg(0, args, boxes): get_arg(1, args, boxes)}
				case "say" | "s":
					self._vm_send({"say": get_arg(0, args, boxes), "time": get_arg(1, args, boxes)})
				case "ask" | "a":
					temp = get_arg(0, args, boxes).split(" ")
					self._vm_send({"ask": get_arg(0, args, boxes)})
					boxes = boxes | ({temp[len(temp)-1]: "fill here with bs" + " : "})
				case "del" | "d":
					del boxes[get_arg(0, args, boxes)]
				case "test" | "t":
					if test(get_arg(1, args, boxes), get_arg(2, args, boxes), get_arg(3, args, boxes)):
						boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
					else:
						boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
				case "math" | "m":
					boxes = boxes | {get_arg(0, args, boxes): str(math(get_arg(1, args, boxes),get_arg(2, args, boxes),get_arg(3, args, boxes)))}
				case "wait" | "wt":
					time.sleep(float(get_arg(0, args, boxes)))
				case "mark" | "mk":
					marks = marks | {get_arg(0, args, boxes): l }	
				case "premark":
					marks = marks | {get_arg(0, args, boxes): l }	
				case "jump" | "j":
					if get_arg(1 ,args, boxes) == "m":
						l = marks[get_arg(0, args, boxes)]
					else:
						l = int(get_arg(0, args, boxes)) - 1
				case "if" | "i":
					run = test(get_arg(0, args, boxes), get_arg(2, args, boxes), get_arg(1, args, boxes))
					if run == True:
						cm_torn = get_arg(3, args, boxes) + " "
						i = 3
						while i <= len(args)-1:
							i = i + 1
							cm_torn = cm_torn + get_arg(i, args, boxes) + "|"
						cm_torn = mk(cm_torn)[1]
						handle_command(cm_torn)
				case "jumpif" | "ji":
					jump = test(get_arg(0, args, boxes), get_arg(2, args, boxes), get_arg(1, args, boxes))
					if jump == True:
						if get_arg(4, args, boxes) == "m":
							l = marks[get_arg(3, args, boxes)]
						else:
							l = int(get_arg(3, args, boxes))
				case "end" | "e":
					exit()
				case "weigh" | "wh":
					boxes = boxes | {get_arg(1,args,boxes): str(len(str(get_arg(0,args,boxes))))}
				case "mrkst":
					arg1 = get_arg(0, args, boxes)
					marks = marks | {arg1: l - 1 }
					if not boxes.__contains__(arg1):
						boxes = boxes | {arg1: "1"}
					else:
						val = str(int(boxes[arg1] + 1))
						print(val)
						boxes = boxes | {arg1: val}
						print(boxes)
	except Exception as e:
		print(Back.RED + Fore.WHITE + "ERROR : " + str(e))
		print(Back.RED + Fore.WHITE + "at line : " + str(l) + "  " + str(undo_mk([command]))  + "boxes : " + str(boxes) + "  marks : " + str(marks))
		print("raw cmd : " + str(command) + Style.RESET_ALL)




def run_boxed_code(boxed_code):
	boxed_code = mk(boxed_code)
	global boxes
	global marks
	global l
	for m in boxed_code:
		marks = marks | m['marks']
	l = 0
	while l < len(boxed_code)-1:
		l = l + 1
		cur_line = boxed_code[l]
		handle_command(cur_line)

def start_boxed_code(boxed_code, name):
	__init__()
	print(Back.BLUE + Fore.GREEN + "RUNNING " + name + Style.RESET_ALL)
	run_boxed_code(boxed_code)
