
tmp = open("test.h", "w")
tmp.write(" #define ONE ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,1):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define TWO ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,2):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define FOUR ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,4):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define EIGHT ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,8):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define SIXTEEN ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,16):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define THIRTYTWO ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,32):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define SIXTYFOUR ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,64):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define HUNDRED ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,128):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define TWOHUNDRED ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,256):
    tmp.write("\"ldr x10,[%0,#"+str(i*32)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define FIVEHUNDRED ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,512):
    tmp.write("\"ldr x10,[%0,#"+str((i*8)%1024)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")

tmp.write(" #define TENHUNDRED ")
tmp.write("asm(")
tmp.write("\"2: \" \\\n")
for i in range(0,1024):
    tmp.write("\"ldr x10,[%0,#"+str((i*8)%1024)+"]\\n\\t\" \\\n")
    tmp.write("\"cmp x10,#0\\n\\t \" \\\n")
    tmp.write("\"beq 1f\\n\\t 1: \" \\\n")
tmp.write("\"add %0, %0, #4\\n\\t \" \\\n")
tmp.write("\"subs %1, %1, #1 \\n\\t\" \\\n")
tmp.write("\"b.ne 2b \\n\\t\" \\\n")
tmp.write(" :\\\n : [src] \"r\" (c), \"r\"(repeat) \\\n :);\n ")