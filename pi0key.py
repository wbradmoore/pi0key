#!/usr/bin/python3

import time
import random
import sys

def main():
    keys = sys.argv[1]
    keys = keys.split(",")

    sequences = [[]]
    repeats = []

    for key in keys:
        if key.startswith("repeat:"):
            repeats.append(int(key[7:]))
            sequences.append([])
        else:
            sequences[len(sequences)-1].append(key)

    if len(repeats) < len(sequences):
        repeats.append(1)

    print(sequences)
    print(repeats)

    for i in range(len(sequences)):
        keys=sequences[i]
        num_repeats=repeats[i]
        for j in range(num_repeats):
            for key in keys:
                print(key)
                if key.startswith('sleep:'):
                    sleeps = [float(s) for s in key.split(":")[1:]]
                    if len(sleeps) == 1:
                        smin=.707*sleeps[0]
                        smax=1.404*sleeps[0]
                        styp=sleeps[0]
                    elif len(sleeps) == 2:
                        smin=sleeps[0]
                        smax=sleeps[1]
                        styp=(sleeps[0]+sleeps[1])/2
                    else:
                        smin=sleeps[0]
                        styp=sleeps[1]
                        smax=sleeps[2]
                    sleep_func(smin,styp,smax)
                else:
                    exec(keypress_functions[key])
                    write_report(chr(0) * 8)
                sleep_func(.1,.2,.6)


#----------------------------------------------------------------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------


def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

def sleep_func(smin,styp,smax):
    time.sleep(random.triangular(smin,smax,styp))

keypress_functions = {
'comma':"write_report(chr(0)*2 +chr(54)+chr(0)*5)",

'a':"write_report(chr(0)*2 +chr(4)+chr(0)*5)",
'b':"write_report(chr(0)*2 +chr(5)+chr(0)*5)",
'c':"write_report(chr(0)*2 +chr(6)+chr(0)*5)",
'd':"write_report(chr(0)*2 +chr(7)+chr(0)*5)",
'e':"write_report(chr(0)*2 +chr(8)+chr(0)*5)",
'f':"write_report(chr(0)*2 +chr(9)+chr(0)*5)",
'g':"write_report(chr(0)*2 +chr(10)+chr(0)*5)",
'h':"write_report(chr(0)*2 +chr(11)+chr(0)*5)",
'i':"write_report(chr(0)*2 +chr(12)+chr(0)*5)",
'j':"write_report(chr(0)*2 +chr(13)+chr(0)*5)",
'k':"write_report(chr(0)*2 +chr(14)+chr(0)*5)",
'l':"write_report(chr(0)*2 +chr(15)+chr(0)*5)",
'm':"write_report(chr(0)*2 +chr(16)+chr(0)*5)",
'n':"write_report(chr(0)*2 +chr(17)+chr(0)*5)",
'o':"write_report(chr(0)*2 +chr(18)+chr(0)*5)",
'p':"write_report(chr(0)*2 +chr(19)+chr(0)*5)",
'q':"write_report(chr(0)*2 +chr(20)+chr(0)*5)",
'r':"write_report(chr(0)*2 +chr(21)+chr(0)*5)",
's':"write_report(chr(0)*2 +chr(22)+chr(0)*5)",
't':"write_report(chr(0)*2 +chr(23)+chr(0)*5)",
'u':"write_report(chr(0)*2 +chr(24)+chr(0)*5)",
'v':"write_report(chr(0)*2 +chr(25)+chr(0)*5)",
'w':"write_report(chr(0)*2 +chr(26)+chr(0)*5)",
'x':"write_report(chr(0)*2 +chr(27)+chr(0)*5)",
'y':"write_report(chr(0)*2 +chr(28)+chr(0)*5)",
'z':"write_report(chr(0)*2 +chr(29)+chr(0)*5)",
'A':"write_report(chr(2)+chr(0)+chr(4)+chr(0)*5)",
'B':"write_report(chr(2)+chr(0)+chr(5)+chr(0)*5)",
'C':"write_report(chr(2)+chr(0)+chr(6)+chr(0)*5)",
'D':"write_report(chr(2)+chr(0)+chr(7)+chr(0)*5)",
'E':"write_report(chr(2)+chr(0)+chr(8)+chr(0)*5)",
'F':"write_report(chr(2)+chr(0)+chr(9)+chr(0)*5)",
'G':"write_report(chr(2)+chr(0)+chr(10)+chr(0)*5)",
'H':"write_report(chr(2)+chr(0)+chr(11)+chr(0)*5)",
'I':"write_report(chr(2)+chr(0)+chr(12)+chr(0)*5)",
'J':"write_report(chr(2)+chr(0)+chr(13)+chr(0)*5)",
'K':"write_report(chr(2)+chr(0)+chr(14)+chr(0)*5)",
'L':"write_report(chr(2)+chr(0)+chr(15)+chr(0)*5)",
'M':"write_report(chr(2)+chr(0)+chr(16)+chr(0)*5)",
'N':"write_report(chr(2)+chr(0)+chr(17)+chr(0)*5)",
'O':"write_report(chr(2)+chr(0)+chr(18)+chr(0)*5)",
'P':"write_report(chr(2)+chr(0)+chr(19)+chr(0)*5)",
'Q':"write_report(chr(2)+chr(0)+chr(20)+chr(0)*5)",
'R':"write_report(chr(2)+chr(0)+chr(21)+chr(0)*5)",
'S':"write_report(chr(2)+chr(0)+chr(22)+chr(0)*5)",
'T':"write_report(chr(2)+chr(0)+chr(23)+chr(0)*5)",
'U':"write_report(chr(2)+chr(0)+chr(24)+chr(0)*5)",
'V':"write_report(chr(2)+chr(0)+chr(25)+chr(0)*5)",
'W':"write_report(chr(2)+chr(0)+chr(26)+chr(0)*5)",
'X':"write_report(chr(2)+chr(0)+chr(27)+chr(0)*5)",
'Y':"write_report(chr(2)+chr(0)+chr(28)+chr(0)*5)",
'Z':"write_report(chr(2)+chr(0)+chr(29)+chr(0)*5)",
'1':"write_report(chr(0)*2 +chr(30)+chr(0)*5)",
'2':"write_report(chr(0)*2 +chr(31)+chr(0)*5)",
'3':"write_report(chr(0)*2 +chr(32)+chr(0)*5)",
'4':"write_report(chr(0)*2 +chr(33)+chr(0)*5)",
'5':"write_report(chr(0)*2 +chr(34)+chr(0)*5)",
'6':"write_report(chr(0)*2 +chr(35)+chr(0)*5)",
'7':"write_report(chr(0)*2 +chr(36)+chr(0)*5)",
'8':"write_report(chr(0)*2 +chr(37)+chr(0)*5)",
'9':"write_report(chr(0)*2 +chr(38)+chr(0)*5)",
'0':"write_report(chr(0)*2 +chr(39)+chr(0)*5)",
'!':"write_report(chr(2)+chr(0)+chr(30)+chr(0)*5)",
'@':"write_report(chr(2)+chr(0)+chr(31)+chr(0)*5)",
'#':"write_report(chr(2)+chr(0)+chr(32)+chr(0)*5)",
'&':"write_report(chr(2)+chr(0)+chr(36)+chr(0)*5)",
'*':"write_report(chr(2)+chr(0)+chr(37)+chr(0)*5)",
'(':"write_report(chr(2)+chr(0)+chr(38)+chr(0)*5)",
')':"write_report(chr(2)+chr(0)+chr(39)+chr(0)*5)",
'-':"write_report(chr(0)*2 +chr(45)+chr(0)*5)",
'=':"write_report(chr(0)*2 +chr(46)+chr(0)*5)",
'{':"write_report(chr(0)*2 +chr(47)+chr(0)*5)",
'}':"write_report(chr(0)*2 +chr(48)+chr(0)*5)",
'\\':"write_report(chr(0)*2 +chr(49)+chr(0)*5)",
';':"write_report(chr(0)*2 +chr(51)+chr(0)*5)",
'':"write_report(chr(0)*2 +chr(52)+chr(0)*5)",
'`':"write_report(chr(0)*2 +chr(53)+chr(0)*5)",
',':"write_report(chr(0)*2 +chr(54)+chr(0)*5)",
'.':"write_report(chr(0)*2 +chr(55)+chr(0)*5)",
'/':"write_report(chr(0)*2 +chr(56)+chr(0)*5)",
'0':"write_report(chr(2)+chr(0)+chr(50)+chr(0)*5)",
':':"write_report(chr(2)+chr(0)+chr(51)+chr(0)*5)",
'"':"write_report(chr(2)+chr(0)+chr(52)+chr(0)*5)",
'<':"write_report(chr(2)+chr(0)+chr(54)+chr(0)*5)",
'>':"write_report(chr(2)+chr(0)+chr(55)+chr(0)*5)",
'?':"write_report(chr(2)+chr(0)+chr(56)+chr(0)*5)",
'}':"write_report(chr(0)*2 +chr(79)+chr(0)*5)",
'{':"write_report(chr(0)*2 +chr(80)+chr(0)*5)",
']':"write_report(chr(2)+chr(0)+chr(79)+chr(0)*5)",
'[':"write_report(chr(2)+chr(0)+chr(80)+chr(0)*5)",

'f1':"write_report(chr(0)*2 +chr(58)+chr(0)*5)",
'f2':"write_report(chr(0)*2 +chr(59)+chr(0)*5)",
'f3':"write_report(chr(0)*2 +chr(60)+chr(0)*5)",
'f4':"write_report(chr(0)*2 +chr(61)+chr(0)*5)",
'f5':"write_report(chr(0)*2 +chr(62)+chr(0)*5)",
'f6':"write_report(chr(0)*2 +chr(63)+chr(0)*5)",
'f7':"write_report(chr(0)*2 +chr(64)+chr(0)*5)",
'f8':"write_report(chr(0)*2 +chr(65)+chr(0)*5)",
'f9':"write_report(chr(0)*2 +chr(66)+chr(0)*5)",
'f10':"write_report(chr(0)*2 +chr(67)+chr(0)*5)",
'f11':"write_report(chr(0)*2 +chr(68)+chr(0)*5)",
'f12':"write_report(chr(0)*2 +chr(69)+chr(0)*5)",

# ']':"write_report(chr(5)+chr(0)+chr(76)+chr(0)*5)", #CTRL+ALT+DEL
'ent':"write_report(chr(0)*2 +chr(40)+chr(0)*5)",
'esc':"write_report(chr(0)*2 +chr(41)+chr(0)*5)",
'bs':"write_report(chr(0)*2 +chr(42)+chr(0)*5)", #BACKSPACE
'tab':"write_report(chr(0)*2 +chr(43)+chr(0)*5)",
'space':"write_report(chr(0)*2 +chr(44)+chr(0)*5)",
'ps':"write_report(chr(0)*2 +chr(70)+chr(0)*5)", #PRINT SCREEN
'del':"write_report(chr(0)*2 +chr(76)+chr(0)*5)",


'right':"write_report(chr(0)*2 +chr(79)+chr(0)*5)",
'left':"write_report(chr(0)*2 +chr(80)+chr(0)*5)",
'down':"write_report(chr(0)*2 +chr(81)+chr(0)*5)",
'up':"write_report(chr(0)*2 +chr(82)+chr(0)*5)",
}

if __name__ == '__main__':
    main()
