from string import Template

# Define a template string with placeholders
template_string = "My name is $name and I am $age years old. My favorite symbol is $$"

# Create a Template object
template_obj = Template(template_string)

# Define a dictionary or use keyword arguments for substitution
data = {'name': 'Alice', 'age': 30}

# Use the substitute method to format the string
result_substitute = template_obj.substitute(**data)
print(f"Substitute result: {result_substitute}")

# Use safe_substitute with a missing value
result_safe = template_obj.safe_substitute(name='Bob',age=67)
print(f"Safe substitute result: {result_safe}")
