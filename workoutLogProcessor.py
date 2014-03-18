import sys, os, re

NEUTRAL_MODE = 0
CANDP_MODE = 1

def annotate_press_volume(filename):
    mode = NEUTRAL_MODE
    volume  = 0
    f = open(filename)
    for line in f.readlines():
        if line.startswith("** "):
            if mode == CANDP_MODE:
                mode = NEUTRAL_MODE
                print "Press volume = %skg" % volume
                volume = 0
                
            print line.strip()
        if line.startswith("***"):
            if (line.find("C&P") > 0):
                mode = CANDP_MODE
                #print line
                #print "In C&P mode"
            else:
                print "Press volume = %skg" % volume
                volume = 0
                mode = NEUTRAL_MODE
        #print line
        if mode == CANDP_MODE:
            foo = re.findall("(\d+)x(\d+)kg", line)
            for item in foo:
                volume += (int(item[0]) * int(item[1]))
            #print foo
    f.close()

if __name__ == "__main__":
    annotate_press_volume("workout-log.org")
