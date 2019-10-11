A = input("").split()
B = input("").split()
print("VALOR A PAGAR: R$ %.2f" %
  ((int(A[1]) * float(A[2]))+
  (int(B[1]) * float(B[2])))
  )