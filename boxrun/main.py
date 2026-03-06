from . import box_to_json as bx2json
from . import box_runner as bxr


import argparse
import pathlib as file
import os.path

def main(code):
    bxr.start_boxed_code(code, args.file)


if __name__ == "__main__":
	import argparse
	parser = argparse.ArgumentParser(description="boxedLANG interpreter")
	parser.add_argument("file", help="path to the boxedLANG source file to run")
	args = parser.parse_args()
    CODE = str(file.Path(os.path.expanduser(args.file)).resolve().read_text())
	try:
		main(CODE)
	except KeyboardInterrupt:
		print("KeyboardInterrupt by user")