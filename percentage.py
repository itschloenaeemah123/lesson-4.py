print("Enter marks for 4 subjects")
maths= int(input("Maths: "))
english= int(input("English: "))
science= int(input("Science: "))
computer= int(input("Computer: "))

sum= maths+english+science+computer
print("Total Marks: ", sum )

perc = (sum/400) * 100
print("percentage: ", perc)