def arithmetic_arranger(*problems):
    # --- START OF TESTS ---
    # Testing the length of the list
    problem_list = problems[0]
    if len(problem_list) > 5:
        return "Error: Too many problems."

    # Testing the operator sign
    for i in problem_list:
        if i.split()[1] == "+" or i.split()[1] == "-":
            operator_error = False
        else:
            operator_error = True
            break
    if operator_error:
        return "Error: Operator must be '+' or '-'."

    # Testing numbers. Must contain only digits.
    for i in problem_list:
        if i.split()[0].isdigit() and i.split()[2].isdigit():
            number_error = False
        else:
            number_error = True
            break
    if number_error:
        return "Error: Numbers must only contain digits."

    # Testing the length of operands
    for i in problem_list:
        if len(i.split()[0]) > 4 or len(i.split()[2]) > 4:
            numlen_error = True
            break
        else:
            numlen_error = False
    if numlen_error:
        return "Error: Numbers cannot be more than four digits."
        # --- END OF TESTS ---

    # --- STARTING THE CREATION OF THE FINAL STRING ---
    # Creating empty lists for lines
    fi_line = []
    se_line = []
    th_line = []
    fo_line = []

    # Appending values to lists
    for i in problem_list:
        # Calculating the length of lines
        fll = len(i.split()[0]) + 2
        sll = len(i.split()[2]) + 2
        maxlen = max([fll, sll])

        # Calculating the value of spacing after operator
        if len(i.split()[2]) > len(i.split()[0]) or len(i.split()[2]) == len(i.split()[0]):
            spacing = " "
        elif len(i.split()[0]) == 4:
            spacing = " " * 4
        else:
            spacing = " " * (maxlen - (len(i.split()[0])))

        # Appending values to lines
        fi_line.append((i.split()[0]).rjust(maxlen))
        se_line.append(spacing.join([i.split()[1], i.split()[2]]).rjust(maxlen))
        th_line.append("-" * maxlen)

        # Calculating and appending values to last line
        if i.split()[1] == "+":
            fn = int(i.split()[0])
            sn = int(i.split()[2])
            fo_line.append(str(fn + sn).rjust(maxlen))
        elif i.split()[1] == "-":
            fn = int(i.split()[0])
            sn = int(i.split()[2])
            fo_line.append(str(fn - sn).rjust(maxlen))

    # Printing out lines
    try:
        if problems[1]:
            return "    ".join(fi_line) + "\n" + "    ".join(se_line) + "\n" + "    ".join(th_line) + "\n" + "    ".join(fo_line)
    except:
        return "    ".join(fi_line) + "\n" + "    ".join(se_line) + "\n" + "    ".join(th_line)

    # --- END OF FUNCTION ---
