import numpy as np

msg = input("Enter the encoded message: ").split()
password = input("Enter the password (4 numbers separated by space): ")
pass_matrix = np.array(password.split(), dtype=int).reshape((2, 2))
msg_mat = np.array([[msg[i] for i in range(0, len(msg) // 2)], [msg[i] for i in range(len(msg) // 2, len(msg))]], dtype=int)
result_mat = np.dot(np.linalg.inv(pass_matrix), msg_mat)
print("The decoded message is: ")
for i in result_mat:
    for j in i:
        print(chr(abs(round(j))), end="")
