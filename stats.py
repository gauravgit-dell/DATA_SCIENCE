import matplotlib.pyplot as plt
# marks = [12,35,22,41,20,10,33,45,27,38,24,31,16,30,39,26,29,36,44]
# plt.hist(marks, bins=[10,20,30,40,50], edgecolor="black")
# plt.xlabel("marks")
# plt.ylabel("frequency")
# plt.title("histogram of quiz marks")
# #plt.show()

# plt.scatter(range(len(marks)), marks)
# plt.show()

# plt.boxplot(marks)
# plt.show()
# plt.bar(range(len(marks)), marks)
# plt.xlabel("Index")
# plt.ylabel("Marks")
# plt.show()

age = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
stems = {}
for values in sorted(age):
    stem , leaf = values // 10, values % 10
    if stem not in stems:
        stems[stem] = []
    stems[stem].append(leaf)
    print(f"{stem} | {' '.join(map(str, stems[stem]))}")