dna_sequence = input ("enter the sequence: ")

list = []
for i in range (0, len (dna_sequence)):
    list.append(dna_sequence[i:i+3])
    if i == len(dna_sequence) - 3:
        break

count = 0

for i in list:
    if i in ["TTA", "TTG", "ACA", "ACG"]:
        count += 1
    elif i in ["TAG", "TAA", "TGA"]:
        break
    
print("Register Number = 23MCA1030 \nName = Vinayak Kumar Singh")
print ("codon appears here in :", count)

