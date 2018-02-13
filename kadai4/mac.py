import struct, sys, uuid;

sys.stdout.write("-".join([hex(fragment)[2:].zfill(2)
for fragment in struct.unpack( "BBBBBB", struct.pack("!Q", uuid.getnode())[2:])]) + "\n")
