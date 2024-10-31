from pulp import LpMaximize, LpProblem, LpVariable, lpSum

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + fruit_juice, "Total_Products"

model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"      
model += 1 * lemonade <= 50, "Sugar_Constraint"                          
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"          
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"        

model.solve()

print("Результати:")
print(f"Кількість виробленого Лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого Фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість продуктів: {model.objective.value()}")