def flatten_this_list(my_list):
  '''will take a list input and return the list without any embedded lists.'''
  result = []
  for item in my_list:
    if isinstance(item, list):
      flattened_list = flatten(item)
      result += flattened_list
    else:
      result.append(item)

  return result
### reserve for testing...
pancake = ['flour', 'eggs', ['milk'], 'maple syrup', [['brandy butter', 'bacon']], 'powdered sugar', ['lemon juice', 'cinnamon']]
print(flatten_this_list(pancake))
