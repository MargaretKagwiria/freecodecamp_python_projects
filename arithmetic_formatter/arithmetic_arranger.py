import re
def arithmetic_arranger(problems, display_values=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  first_digits = []
  last_digits = []
  operators = []
  error_message = None
  for item in problems:
    first_digit, operator, last_digit = item.split(" ")
    if operator not in ['+', '-']:
      error_message = "Error: Operator must be '+' or '-'."
      
    elif len(first_digit) > 4 or len(last_digit) > 4:
      error_message = 'Error: Numbers cannot be more than four digits.'
      
    elif re.findall('[^0-9]+', first_digit):
      error_message = "Error: Numbers must only contain digits."
      
    elif re.findall('[^0-9]+', last_digit):
      error_message = "Error: Numbers must only contain digits."
      
    first_digits.append(first_digit)
    last_digits.append(last_digit)
    operators.append(operator)
  if error_message:
    return error_message
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []

  for i in range(len(first_digits)):
    if len(first_digits[i]) > len(last_digits[i]):
        first_line.append(" "*2 + first_digits[i])
    else:
        first_line.append(" "*(len(last_digits[i]) - len(first_digits[i]) + 2) + first_digits[i])

  for i in range(len(last_digits)):
      if len(last_digits[i]) > len(first_digits[i]):
          second_line.append(operators[i] + " " + last_digits[i])
      else:
          second_line.append(operators[i] + " "*(len(first_digits[i]) - len(last_digits[i]) + 1) + last_digits[i])

  for i in range(len(first_digits)):
      third_line.append("-"*(max(len(first_digits[i]), len(last_digits[i])) + 2))

  if display_values:
    for i in range(len(first_digits)):
        if operators[i] == "+":
            ans = str(int(first_digits[i]) + int(last_digits[i]))
        else:
            ans = str(int(first_digits[i]) - int(last_digits[i]))

        if len(ans) > max(len(first_digits[i]), len(last_digits[i])):
            fourth_line.append(" " + ans)
        else:
            fourth_line.append(" "*(max(len(first_digits[i]), len(last_digits[i])) - len(ans) + 2) + ans)
    arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line) + "\n" + "    ".join(fourth_line)
  else:
      arranged_problems = "    ".join(first_line) + "\n" + "    ".join(second_line) + "\n" + "    ".join(third_line)
  return arranged_problems
  