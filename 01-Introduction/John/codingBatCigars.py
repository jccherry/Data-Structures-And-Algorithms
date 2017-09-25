#http://codingbat.com/prob/p195669

def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  elif isBetween(40,cigars,60) and not is_weekend:
    return True
  else:
    return False
  

def isBetween(lowerBound, value, upperBound):
  if value >= lowerBound and value <= upperBound:
    return True
  else:
    return False

