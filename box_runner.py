import pathlib 
from colorama import Fore, Back, Style
import time
import sys
import box_to_json as bx2json


CODE = pathlib.Path(sys.argv[1]).read_text()
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
			arg = "ERROR : " + cur_box
	return arg
		
def handle_command(command, boxes, marks,l = 0):
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
					match get_arg(3, args, boxes):
						case "==":
							if get_arg(1, args, boxes) == get_arg(2, args, boxes):								
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
						case "!=":
							if get_arg(1, args, boxes) != get_arg(2, args, boxes):
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
						case ">":
							if float(get_arg(1, args, boxes)) > float(get_arg(2, args, boxes)):
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
						case "<":
							if float(get_arg(1, args, boxes)) < float(get_arg(2, args, boxes)):								
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
						case ">=":
							if float(get_arg(1, args, boxes)) >= float(get_arg(2, args, boxes)):
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
						case "<=":
							if float(get_arg(1, args, boxes)) <= float(get_arg(2, args, boxes)):
								boxes = boxes | {get_arg(0, args, boxes): get_arg(4, args, boxes)}
							else:
								boxes = boxes | {get_arg(0, args, boxes): get_arg(5, args, boxes)}
				case "math":
					boxes = boxes | {get_arg(0, args, boxes): str(eval(get_arg(1, args, boxes) + get_arg(3, args, boxes) + get_arg(2, args, boxes)))}
				case "wait":
					time.sleep(float(get_arg(0, args, boxes)))
				case "mark":
					marks = marks | {get_arg(0, args, boxes): cur_line['ln']}	
				case "jump":
					if get_arg(1 ,args, boxes) == "m":
						l = marks[get_arg(0, args, boxes)]
					else:
						l = int(get_arg(0, args, boxes)) - 1
				case "if":
					run = False
					match get_arg(2, args, boxes):
						case "==":
							if get_arg(0, args, boxes) == get_arg(3, args, boxes):								
								run = True
						case "!=":
							if get_arg(0, args, boxes) != get_arg(3, args, boxes):
								run = True
						case ">":
							if float(get_arg(0, args, boxes)) > float(get_arg(3, args, boxes)):
								run = True
						case "<":
							if float(get_arg(0, args, boxes)) < float(get_arg(3, args, boxes)):
								run = True
						case ">=":
							if float(get_arg(0, args, boxes)) >= float(get_arg(3, args, boxes)):
								run = True
						case "<=":
							if float(get_arg(0, args, boxes)) <= float(get_arg(3, args, boxes)):
								run = True
					if run == True:
						cm_torn = get_arg(4, args, boxes)
						i = 4
						while get_arg(i, args, boxes) != "":
							i = 5
							if i > 5:
								cm_torn = cm_torn + "|" + get_arg(i, args, boxes)
							else:
								cm_torn = cm_torn + " " + get_arg(i, args, boxes)
							i = i + 1
						handle_command(bx2json.mk(cm_torn)[0], boxes, marks)
	except Exception as e:
		print(Back.RED + Fore.WHITE + "ERROR : " + str(e) + Style.RESET_ALL)
		print(Back.RED + Fore.WHITE + "at line : " + str(l) + "  " + str(bx2json.undo_mk([command])) + Style.RESET_ALL)



def run_boxed_code(boxed_code):
	

	boxes = {}
	l = -1
	marks = {}
	while l < len(boxed_code)-1:
		l = l + 1
		cur_line = boxed_code[l]
		handle_command(cur_line, boxes, marks, l)

print(Back.BLUE + Fore.GREEN + "RUNNING " + sys.argv[1] + Style.RESET_ALL)
run_boxed_code(CODE)