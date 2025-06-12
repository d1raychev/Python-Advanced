text = input()

stacks = []
for i in range(len(text)):
    if text[i] == "(":
        stacks.append(i)

    elif text[i] == ")":
        start_index = stacks.pop()
        end_index = i + 1
        print(text[start_index:end_index])
