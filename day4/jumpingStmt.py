# jumping statements - break; continue(used/applied in loops)

# check if value in range is 70 and break/come out of loop

for i in range(5, 101, 5):
    print(i)  # 0....10
    if i==70:
	    break
print("program exited at 70")

# check if value in range is 25 and continue loop

for i in range(5, 101, 5):
    print(i)  # 0....10
    if i==25:
        continue
        print(i)
print("program continue at 25")

# multiple operators and use of jumpibg stmts
for i in range(5, 101, 5):
    if i==40 or i==45 or i==60:
        continue
        print(i)
