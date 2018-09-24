def weight_on_planets():
    # write your code here
    planets = ["Mars", "Jupiter"]
    wmult = [0.38, 2.34]

    weight = int(input("What do you weigh on earth? "))
    result = "\n"

    for i in range(2):
        result += "On " + planets[i] + " you would weigh " + format(wmult[i]*weight) + " pounds."

        if i == 0:
            result += "\n"

    print(result, end='')
   
   
if __name__ == '__main__':
    weight_on_planets()
