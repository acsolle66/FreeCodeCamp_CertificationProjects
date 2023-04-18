class Category:

    def __init__(self, name=""):
        self.name = name
        self.ledger = []
        self.category_balance = 0
        self.ledger_description = None
        self.ledger_amount = None
        self.description_amount_dict = {}

    def recalculate_category_balance(self):
        ledger_amount = [sub["amount"] for sub in self.ledger]
        self.category_balance = sum(ledger_amount)

    def recalculate_description_amount_dict(self):
        self.ledger_description = [sub["description"] for sub in self.ledger]
        self.ledger_amount = [sub["amount"] for sub in self.ledger]
        ledger_amount_string_list = [str(format(st, ".2f")) for st in self.ledger_amount]
        ledger_description_string_list = [st[:23] for st in self.ledger_description]
        for i in range(0, len(ledger_amount_string_list)):
            self.description_amount_dict[ledger_description_string_list[i]] = ledger_amount_string_list[i]

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.recalculate_category_balance()
        self.recalculate_description_amount_dict()
        return True

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.recalculate_category_balance()
            self.recalculate_description_amount_dict()
            return True
        else:
            return False


    def transfer(self, amount, category):
        if self.check_funds(amount):
            transfer_name = category.name
            category.deposit(amount, f"Transfer from {self.name}")
            self.ledger.append({"amount": -amount, "description": f"Transfer to {transfer_name}"})
            self.recalculate_category_balance()
            self.recalculate_description_amount_dict()
            return True
        else:
            return False

    def get_balance(self):
        return self.category_balance
    def check_funds(self, amount):
        self.recalculate_category_balance()
        self.recalculate_description_amount_dict()
        if self.category_balance - amount < 0:
            return False
        else:
            return True

    def __str__(self):
        self.recalculate_description_amount_dict()
        description_amount_list = []
        for k, v in self.description_amount_dict.items():
            description_amount_list.append([f"{k.ljust(23)}{v.rjust(7)}"])

        for i in range(0, len(description_amount_list)):
            description_amount_list[i].append("\n")

        description_amount_string = []
        for i in range(0, len(description_amount_list)):
            for j in (description_amount_list[i]):
                description_amount_string.append(j)

        return self.name.center(30, "*") + "\n" + "".join(description_amount_string) + f"Total: {self.category_balance}"


def create_spend_chart(args):
    category_list = [cat for cat in args]

    # Creating a list where category names and ledger amount is grouped in separated lists
    category_amount_ledger = [[a.name, a.ledger_amount] for a in category_list]
    category_withdraw_ledger = [[a.name, []] for a in category_list]
    category_withdraw_percentage = [[a.name, []] for a in category_list]

    # Removing deposit values from category amount ledger >>> transition to category withdraw ledger
    for i in range(0, len(category_amount_ledger)):
        for j in category_amount_ledger[i][1]:
            if j < 0:
                category_withdraw_ledger[i][1].append(j)

    # Calculating the total spend amount
    total_amount_spent_list = []
    for i in range(0, len(category_withdraw_ledger)):
        for j in category_withdraw_ledger[i][1]:
            total_amount_spent_list.append(j)
    total_amount_spent = round(sum(total_amount_spent_list))

    # Calculating the total spent amount percentage by category
    for i in range(0, len(category_amount_ledger)):
        category_withdraw_percentage[i][1].append(
            round(100 * ((sum(category_withdraw_ledger[i][1]) / total_amount_spent))))

    PERCENTAGE_LABELS = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

    # PRINTING OUT THE RESULTS

    line_list = []

    for i in PERCENTAGE_LABELS:
        line_list.append([str(i).rjust(3)])

    for i in range(0, len(line_list)):
        line_list[i].append("|")

    for i in range(0, len(line_list)):
        for j in range(0, len(category_withdraw_percentage)):
            if category_withdraw_percentage[j][1][0] >= PERCENTAGE_LABELS[i]:
                line_list[i].append(" o ")
            else:
                line_list[i].append("   ")

    for i in range(0, len(line_list)):
        line_list[i].append(" ")

    for i in range(0, len(line_list)):
        line_list[i].append("\n")

    line_list_string = []
    for i in range(0, len(line_list)):
        for j in range(0, len(line_list[i])):
            line_list_string.append(line_list[i][j])

    # Printing the category name
    category_names_list = [[a.name] for a in category_list]

    max_string_length = None
    for i in range(0, len(category_names_list)):
        if max_string_length is None or max_string_length < len(category_names_list[i][0]):
            max_string_length = len(category_names_list[i][0])

    lines_names_list = []
    for i in range(0, max_string_length):
        lines_names_list.append([" " * 4])

    for i in range(0, len(lines_names_list)):
        for name in category_names_list:
            try:
                lines_names_list[i].append(f" {name[0][i]} ")
            except:
                lines_names_list[i].append("   ")

    for i in range(0, len(lines_names_list)):
        lines_names_list[i].append(" ")

    for i in range(0, len(lines_names_list)-1):
        lines_names_list[i].append("\n")

    lines_names_string = []
    for i in range(0, len(lines_names_list)):
        for j in range(0, len(lines_names_list[i])):
            lines_names_string.append(lines_names_list[i][j])

    return "".join(["Percentage spent by category", "\n"]) + "".join(line_list_string) \
    + "".join([" " * 4, "---" * len(category_list), "-", "\n"]) + "".join(lines_names_string)




