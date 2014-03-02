from optparse import OptionParser
import sys

def checksum8(data):
    sum = 0
    for c in data:
        sum = sum + ord(c)
    return sum

def checksum16(data):
    sum = 0
    num = 0
    isFirstBytye = True

    for c in data:
        if isFirstBytye == True:
            isFirstBytye = False
            num = ord(c)
        else:
            isFirstBytye = True
            num = num * 256 + ord(c)
            sum = sum + num
    return sum

parser = OptionParser(usage="%prog [OPTION]... [FILE]", version="%prog 1.0")
parser.add_option("-w", "--width", type="int", dest="bits", default=8,
                  help="The number of bits of checksum (= 8 or 16)")
parser.add_option("--binary", action="store_true", dest="binary",
                  help="Checksum is output in binary")
(options, args) = parser.parse_args()

if len(args) != 1:
    parser.error("missing file operand")

infile = open(args[0], 'rb')
data = infile.read()
infile.close()

if options.bits == 8:
    sum = checksum8(data)
else:
    sum = checksum16(data)

if options.binary == True:
    sys.stdout.write("%c%c" % (chr(sum / 256), chr(sum % 256)))
else:
    print "%02X%02X" % (sum / 256, sum % 256),
