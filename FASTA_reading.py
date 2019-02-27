# Program to read a FASTA file
import re
import sys
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Fasta file")
flag = 1
i = -1
info = []
gene_sequence = []

# def callback():
#     global name
#     name = filedialog.askopenfilename()
#     print(name)

# Reading the file and seperating the information and gene sequence
def read_file():
    name = filedialog.askopenfilename()
    global i, info, gene_sequence

    with open(name, "r") as f:
        for line in f:
            if line[0] == '>':
                line = line.rstrip('\n')
                info.append(line.strip('>'))
                i = i + 1
                gene_sequence.append("")

            elif (bool(re.match('.[AGCT]', line)) or bool(re.match('^[AGCT]', line))):
                gene_sequence[i] = gene_sequence[i] + line.strip()

            else:
                # print("Either gene sequence contains letters other than AGCT or specification takes more than one line.")
                # print("Incorrect Fasta file.")
                flag = 0
                #sys.exit(1)

# Writing the output file in the speified format
def download_file():
    global i
    with open("Output.txt", "w") as fd:
        fd.write('{0:5}  {1:100}  {2}   \n'.format("Sl. No.", "Info", "Gene"))

        for iter in range(0, i):
            fd.write('{0:5}  {1:100}  {2}   \n'.format(str(iter + 1), str(info[iter]), str(gene_sequence[iter])))



Button(text = "Open File", command = read_file).pack(fill = X)

if flag:
    Button(text = "Download File", command = download_file).pack(fill = X)
else:
    text = Text(Tk)
    text.insert(END, "Either gene sequence contains letters other than AGCT or specification takes more than one line.\nIncorrect Fasta file.\n")

root.mainloop()
