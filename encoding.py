import numpy as np

message = input("Enter the sentence for encoding:\n")
password = input("Enter the password (4 numbers separated by space): ")
pass_matrix = np.array(password.split(), dtype=int).reshape((2, 2))

if len(message) % 2 == 1:
    message += " "
message_matrix = np.array(
    [
        [ord(message[i]) for i in range(len(message) // 2)],
        [ord(message[i]) for i in range(len(message) // 2, len(message))],
    ]
)
# print(message_matrix)
result_mat = np.dot(pass_matrix, message_matrix)

print("\nThe encoded numbers are: ")
for i in result_mat:
    for j in i:
        print(j, end=" ")
