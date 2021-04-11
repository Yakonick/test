import errant


annotator = errant.load('en')
# orig = annotator.parse('This are gramamtical sentence .')
# cor = annotator.parse('This is a grammatical sentence .')
# edits = annotator.annotate(orig, cor)
# for e in edits:
#     print(e.o_start, e.o_end, e.o_str, e.c_start, e.c_end, e.c_str, e.type)

dictionary_or_cor = dict()
with open("tmp.txt", 'r') as f:
	or_cor = f.readlines()

list_of_all_edits = []
for i in range(0, len(or_cor), 3):
	orig = annotator.parse(or_cor[i].replace("\n", ""))			# Original
	cor = annotator.parse(or_cor[i + 1].replace("\n", ""))		# Corrected
	dictionary_or_cor[orig] = cor

for key in dictionary_or_cor:
	edits = annotator.annotate(key, dictionary_or_cor[key])
	for e in edits:
		if "OTHER" in e.type or "UNK" in e.type or "ORTH" in e.type \
			or "PUNCT" in e.type or "SPELL" in e.type:
			edits.remove(e)
	if edits != []:
		list_of_all_edits.append((key, dictionary_or_cor[key], edits))

with open("answer.txt", 'w') as f:
	for edits in list_of_all_edits:
		f.write(str(edits[0]) + '\n')
		f.write(str(edits[1]) + '\n')
		for e in edits[2]:
			f.write(e.o_str + " -> " + e.c_str + "\t" + e.type + "\n")
		f.write("\n\n")