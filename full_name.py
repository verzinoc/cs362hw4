def generate_name(first_name, last_name):
   if first_name == "":
      return last_name
   if last_name == "":
      return first_name
   return first_name + " " + last_name
