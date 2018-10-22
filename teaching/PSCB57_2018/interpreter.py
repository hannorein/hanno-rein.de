#!/usr/bin/python
import sys
import os

maxsteps = 0

def run(code):
    lines = code.splitlines()
    c = [i.upper().split() for i in lines]


    ip = 0 #instruction pointer
    r  = [0]*16
    print("----- START OF PROGRAM ----")

    def getRegister(s):
        if len(s)!=2:
            raise RuntimeError("Synatx error. Cannot parse register.\n")
        try:
            register = (int)(s[1])
        except:
            raise RuntimeError("Synatx error. Cannot parse register.\n")
        if register<0 or register>15:
            raise RuntimeError("Register out of bound.\n")
        return register

    steps = 0
    while maxsteps==0 or steps<=maxsteps:
        steps = steps + 1
        if ip>=len(c):
            break
        command = c[ip]
        if len(command) > 0:
            if command[0] == "SET":
                if len(command)!=3:
                    raise RuntimeError("Synatx error.\n")
                s0 = (int)(command[1])
                r0 = getRegister(command[2])
                r[r0] = s0
            elif command[0] == "PRINT":
                if len(command)!=2:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                print(r[r0])
            elif command[0] == "ADD":
                if len(command)!=4:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                r1 = getRegister(command[2])
                r2 = getRegister(command[3])
                r[r2] = r[r0] + r[r1]
            elif command[0] == "SUB":
                if len(command)!=4:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                r1 = getRegister(command[2])
                r2 = getRegister(command[3])
                r[r2] = r[r0] - r[r1]
            elif command[0] == "COPY":
                if len(command)!=3:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                r1 = getRegister(command[2])
                r[r1] = r[r0] 
            elif command[0] == "JUMP":
                if len(command)!=2:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                ip = ip + r[r0]-1 
            elif command[0] == "IF":
                if len(command)!=3:
                    raise RuntimeError("Synatx error.\n")
                r0 = getRegister(command[1])
                r1 = getRegister(command[2])
                if r[r1]>=r[r0]:
                    ip = ip + 1 
            else:
                raise RuntimeError("Unknown command: \n"+command[0])



        ip = ip + 1

    print("----- END OF PROGRAM ----")


if __name__ == "__main__":
    if len(sys.argv) <2:
        print("Usage: ./interpreter.py filename [maxsteps]\n")
        sys.exit(-1)

    filename = sys.argv[1]

    if len(sys.argv)>2:
        maxsteps = (int)(sys.argv[2])

    if not os.path.isfile(filename):
        print("Error. File not found.\n\n")
        print("Usage: ./interpreter.py filename\n")
        sys.exit(-1)

    with open(filename) as f:
        lines = f.readlines()

