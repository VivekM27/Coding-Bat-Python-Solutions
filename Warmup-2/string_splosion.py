# STRING_SPLOSION
def string_splosion(str):
  l = len(str)
  string = ''
  for i in range(l):
    string += str[:int(i)]
  return string + str