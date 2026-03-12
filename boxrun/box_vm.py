"""
boxedLANG virtual machine interpreter

Note from Stormy:
    Please for goodness sake stop using global variables, they're gross,
    just pass them as function parameters smh.
"""

from colorama import Fore, Back, Style
import time
import threading
import queue
from box_to_json import mk, undo_mk


boxes = {}
marks = {}
line_index = -1


class BoxedVM:
    def __init__(self, inbox=queue.Queue(), outbox=queue.Queue()):
        self.inbox = inbox
        self.outbox = outbox

    def start(self, code: str, name: str):
        """
		Run the VM in the background so both sides work at once
		
		:param code: Code to run
		:param name: Name of instance
		"""
        t = threading.Thread(target=self._run, args=(code, name), daemon=True)
        t.start()

    def send(self, data):
        """
		Drop data into mailbox
		
		:param data: Data to put in mailbox
		"""
        self.inbox.put(data)

    def recv(self):
        """Check mailbox for data"""
        return self.outbox.get()

    def _vm_send(self, data):
        """
        Sends data between mailboxes
        
        :param data: Data to send
        """
        self.outbox.put(data)

    def _vm_recv(self):
        """Check for VM data"""
        return self.inbox.get()

    def _run(self, code, name):
        print("run")
        start_boxed_code(code, name)
        self._vm_send({"end": "script"})


def get_arg(argnumb, args, boxes):
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


def test(left: str, right: str, op: str) -> bool:
    """
    Test for operator with two different values
    
    :param left: First value
    :type left: str
    :param right: Second value
    :type right: str
    :param op: Operator for comparing
    :type op: str
    :return: Test result
    :rtype: bool
    """
    match op:
        case "==":
            if left == right:
                return True
            else:
                return False
        case "!=":
            if left != right:
                return True
            else:
                return False
        case ">":
            if float(left) > float(right):
                return True
            else:
                return False
        case "<":
            if float(left) < float(right):
                return True
            else:
                return False
        case ">=":
            if float(left) >= float(right):
                return True
            else:
                return False
        case "<=":
            if float(left) <= float(right):
                return True
            else:
                return False
        case "<=":
            if float(left) <= float(right):
                return True
            else:
                return False
    return False


def math(left: int, right: int, operator: str) -> int:
    """
    Perform math arithmetic to two integers
    
    :param left: First integer
    :type left: int
    :param right: First integer
    :type right: int
    :param operator: Arithmetic operator
    :type operator: str
    :return: Evaluated integer
    :rtype: int
    """
    if operator == "+":
        return int(left) + int(right)
    elif operator == "-":
        return int(left) - int(right)
    elif operator == "*" or "x":
        return int(left) * int(right)
    elif operator == "/":
        return int(left) // int(right)
    elif operator == "%":
        return int(left) % int(right)
    return 0


def handle_command(vm: BoxedVM, command: dict) -> None:
    """
    Handle and execute given command
    
    :param vm: BoxedVM instance
    :type vm: BoxedVM
    :param command: Commands dictionary
    :type command: dict
    """
    global boxes
    global marks
    global line_index
    try:
        args = command["args"]
        match command["cmd"]:
            case "box" | "b":
                boxes = boxes | {
                    get_arg(0, args, boxes): get_arg(1, args, boxes)
                }
            case "say" | "s":
                vm._vm_send(
                    {
                        "say": get_arg(0, args, boxes),
                        "time": get_arg(1, args, boxes)
                    }
                )
            case "ask" | "a":
                temp = get_arg(0, args, boxes).split(" ")
                vm._vm_send({"ask": get_arg(0, args, boxes)})
                boxes = boxes | ({
                    temp[len(temp) - 1]: "fill here with bs" + " : "
                })
            case "del" | "d":
                del boxes[get_arg(0, args, boxes)]
            case "test" | "t":
                if test(
                    get_arg(1, args, boxes),
                    get_arg(2, args, boxes),
                    get_arg(3, args, boxes),
                ):
                    boxes = boxes | {
                        get_arg(0, args, boxes): get_arg(4, args, boxes)
                    }
                else:
                    boxes = boxes | {
                        get_arg(0, args, boxes): get_arg(5, args, boxes)
                    }
            case "math" | "m":
                boxes = boxes | {
                    get_arg(0, args, boxes): str(
                        math(
                            int(get_arg(1, args, boxes)),
                            int(get_arg(2, args, boxes)),
                            get_arg(3, args, boxes),
                        )
                    )
                }
            case "wait" | "wt":
                time.sleep(float(get_arg(0, args, boxes)))
            case "mark" | "mk":
                marks = marks | {get_arg(0, args, boxes): line_index}
            case "premark":
                marks = marks | {get_arg(0, args, boxes): line_index}
            case "jump" | "j":
                if get_arg(1, args, boxes) == "m":
                    l = marks[get_arg(0, args, boxes)]
                else:
                    l = int(get_arg(0, args, boxes)) - 1
            case "if" | "i":
                run = test(
                    get_arg(0, args, boxes),
                    get_arg(2, args, boxes),
                    get_arg(1, args, boxes),
                )
                if run == True:
                    cm_torn = get_arg(3, args, boxes) + " "
                    i = 3
                    while i <= len(args) - 1:
                        i = i + 1
                        cm_torn = cm_torn + get_arg(i, args, boxes) + "|"
                    cm_torn = mk(cm_torn)[1]
                    handle_command(vm, cm_torn)
            case "jumpif" | "ji":
                jump = test(
                    get_arg(0, args, boxes),
                    get_arg(2, args, boxes),
                    get_arg(1, args, boxes),
                )
                if jump == True:
                    if get_arg(4, args, boxes) == "m":
                        l = marks[get_arg(3, args, boxes)]
                    else:
                        l = int(get_arg(3, args, boxes))
            case "end" | "e":
                exit()
            case "weigh" | "wh":
                boxes = boxes | {
                    get_arg(1, args, boxes): str(len(str(get_arg(0, args, boxes))))
                }
            case "mrkst":
                arg1 = get_arg(0, args, boxes)
                marks = marks | {arg1: line_index - 1}
                if not boxes.__contains__(arg1):
                    boxes = boxes | {arg1: "1"}
                else:
                    val = str(int(boxes[arg1] + 1))
                    print(val)
                    boxes = boxes | {arg1: val}
                    print(boxes)
    except Exception as e:
        print(Back.RED + Fore.WHITE + "ERROR : " + str(e))
        print(
            Back.RED
            + Fore.WHITE
            + "at line : "
            + str(line_index)
            + "  "
            + str(undo_mk([command]))
            + "boxes : "
            + str(boxes)
            + "  marks : "
            + str(marks)
        )
        print("raw cmd : " + str(command) + Style.RESET_ALL)


def run_boxed_code(vm: BoxedVM, boxed_code: list) -> None:
    """
    Runs given boxedLANG code in a VM
    
    :param vm: boxedLANG VM instance
    :type vm: BoxedVM
    :param boxed_code: Program to run
    :type boxed_code: list
    """
    global boxes
    global marks
    global line_index
    boxed_code = mk(boxed_code)
    marks = boxed_code[-1]['marks']
    line_index = 0
    while line_index < len(boxed_code) - 1:
        line_index += 1
        cur_line = boxed_code[line_index]
        handle_command(vm, cur_line)


def start_boxed_code(boxed_code: list, name: str) -> None:
    """
    Public function to run boxedLANG code
    
    :param boxed_code: Program to run
    :type boxed_code: list
    :param name: Name of instance
    :type name: str
    """
    vm = BoxedVM()
    print(Back.BLUE + Fore.GREEN + "RUNNING " + name + Style.RESET_ALL)
    run_boxed_code(vm, boxed_code)
