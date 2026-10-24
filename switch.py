grade = input("Enter your grade (A+, A, B, C, D, F): ")

match grade:
    case "A" | "A+":
        print("Great performance, keep this up!")
    case "B":
        print("Very Good, keep imporving.")
    case "C":
        print("Could be better, keep working hard.")
    case "D":
        print("Poor performance. Need a lot of improvement")
    case "F":
        print("Need serious attention on development. Please contact the head master")
    case _:
        print("Please Enter Valid Grade")