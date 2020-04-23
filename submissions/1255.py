n = int(input(""))

for i in range(0,n):

  s  = input().lower()
  
  # finds the frequency for each character
  freq = {}
  for i in s: 
    if i in freq: 
        freq[i] += 1
    else: 
        freq[i] = 1

  # calculates the highest frequency
  x = 0
  for i in freq:
    # if its a letter of the alphabet and its frequency is higher than the latter
    if((ord(i)-97 >= 0 and ord(i)-97 <= 26) and freq[i] > x):
      # set it as the highest frequency
      x = freq[i]

  resp = ""
  # finding the highest frequencies and adding to answer string
  for i in freq:
    if(x == freq[i]):
      resp += i
  
  if(len(resp) > 1):
    resp = ''.join(sorted(resp))

  print(resp.strip())