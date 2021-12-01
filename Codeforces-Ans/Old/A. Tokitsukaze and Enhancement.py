n = int(input())
rank = {
    1: "A",
    3: "B",
    2: "C",
    0: "D"
}
grade = [rank[n % 4], rank[(n+1) % 4], rank[(n+2) % 4]]
if "A" in grade:
    print(grade.index("A"), "A")
elif "B" in grade:
    print(grade.index("B"), "B")
elif "C" in grade:
    print(grade.index("C"), "C")
elif "D" in grade:
    print(grade.index("D"), "D")