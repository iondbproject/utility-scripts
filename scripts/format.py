import platform
import os
import os.path
import subprocess
import argparse

filexts = [
	'.c',
	'.cpp',
	'.h',
	'.hpp',
	'.ino',
]

parser = argparse.ArgumentParser()
parser.add_argument("dir", help="Directory target to format.")
parser.add_argument("--dry-run", help="Show what files would be formatted without performing any modifications.", action="store_true")
args = parser.parse_args()

for root, dirs, files in  os.walk(args.dir):
	for file_name in files:
		_, ext = os.path.splitext(file_name)
		if ext not in filexts:
			continue

		full_path = os.path.join(root, file_name)
		if args.dry_run:
			print(full_path)
		else:
			os.system("uncrustify -c dotfiles/iondb_style.cfg --replace --no-backup " + full_path)
			subprocess.call(["python", "dotfiles/scripts/spacestotabs.py", full_path, full_path])
