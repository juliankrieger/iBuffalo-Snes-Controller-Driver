import subprocess
from pprint import pprint
import sys
def main():
    p = subprocess.Popen("cat /proc/bus/input/devices | awk -F ':' '{print $2}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    output = p.stdout.readlines()
    entries = get_entries(output)
    dicts = get_dicts(entries)

    sys.exit(get_controller_event(dicts))


def get_entries(text):
    entrys = []
    entry = []

    for line in text:
        line = (line.decode("utf-8"))

        if line == "\n":
            entrys.append(entry)
            entry = []
            continue

        entry.append(line)
    return entrys

def get_dicts(entries):

    dicts = []
    d = {}

    for entry in entries:
        firstline = None
        for count, line in enumerate(entry):
            line = line.rstrip()
            if count is 0:
                firstline = line
            if count is not 0:
                ls = line.split("=")
                key, value = (ls[0], ls[1])
                d[key] = value

        add_firstline(firstline, d)

        dicts.append(d)
        d = {}

    return dicts

def add_firstline(firstline, d):
    for ln in firstline.split(" "):
            ln = ln.split("=")
            try:
                key, value = (ln[0], ln[1])
                d[key] = value
            except:
                pass

def get_controller_event(dicts):
    for d in dicts:
        for key, value in d.items():
            if "USB,2-axis 8-button gamepad" in value:
                return d[' Handlers'].split(" ")[0]
    
if __name__ == "__main__":
    main()
