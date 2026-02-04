import pathlib 
from os.path import expanduser
from colorama import Fore, Back, Style
import time
import sys
import boxcode.boxrun.box_to_json as bx2json

boxes = {}
marks = {}
l = -1

CODE = pathlib.Path(expanduser(sys.argv[1])).read_text()
CODE = bx2json.mk(CODE)

def get_arg(argnumb, args,boxes):
	try:
		arg = args[argnumb]  
		for i in range(0, arg.count("$")):
			cur_box = arg.split("$")[1]
			cur_box = cur_box.split("~")[0]
			cur_box = cur_box.split(":")[0]
			arg = arg.replace("$" + cur_box, boxes[cur_box])
		arg = arg.replace("~", " ")
		arg = arg.replace(":", "")
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
		
def handle_command(command):
	global boxes
	global marks
	global l
	try:
		args = command['args']
		match command['cmd']:
				case "box":
					boxes = boxes | {get_arg(0, args, boxes): get_arg(1, args, boxes)}
				case "say":
					print(str(get_arg(0, args, boxes)))
					if len(args) > 1:
						time.sleep(float(get_arg(1, args, boxes)))
				case "ask":
					temp = get_arg(0, args, boxes).split(" ")
					boxes = boxes | {temp[len(temp)-1]: input(get_arg(0, args, boxes) + " : ")}
				case "del":
					del boxes[get_arg(0, args, boxes)]
				case "test":
					if test(get_arg(0, args, boxes), get_arg(1, args, boxes), get_arg(3, args, boxes)) == True:
						boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
					else:
						boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
				case "math":
					boxes = boxes | {get_arg(0, args, boxes): str(eval(get_arg(1, args, boxes) + get_arg(3, args, boxes) + get_arg(2, args, boxes)))}
				case "wait":
					time.sleep(float(get_arg(0, args, boxes)))
				case "mark":
					marks = marks | {get_arg(0, args, boxes): l }	
				case "jump":
					if get_arg(1 ,args, boxes) == "m":
						l = marks[get_arg(0, args, boxes)]
					else:
						l = int(get_arg(0, args, boxes)) - 1
				case "if":
					run = test(get_arg(0, args, boxes), get_arg(2, args, boxes), get_arg(1, args, boxes))
					if run == True:
						cm_torn = get_arg(3, args, boxes) + " "
						i = 3
						while i <= len(args)-1:
							i = i + 1
							cm_torn = cm_torn + get_arg(i, args, boxes) + "|"
						cm_torn = bx2json.mk(cm_torn)[1]
						handle_command(cm_torn)
				case "jumpif":
					jump = test(get_arg(0, args, boxes), get_arg(2, args, boxes), get_arg(1, args, boxes))
					if jump == True:
						if get_arg(4, args, boxes) == "m":
							l = marks[get_arg(3, args, boxes)]
						else:
							l = int(get_arg(3, args, boxes))
	except Exception as e:
		print(Back.RED + Fore.WHITE + "ERROR : " + str(e) + Style.RESET_ALL)
		print(Back.RED + Fore.WHITE + "at line : " + str(l) + "  " + str(bx2json.undo_mk([command]))  + "boxes : " + str(boxes) + Style.RESET_ALL)




def run_boxed_code(boxed_code):
	global boxes
	global marks
	global l
	while l < len(boxed_code)-1:
		l = l + 1
		cur_line = boxed_code[l]
		handle_command(cur_line)

print(Back.BLUE + Fore.GREEN + "RUNNING " + sys.argv[1] + Style.RESET_ALL)
run_boxed_code(CODE)