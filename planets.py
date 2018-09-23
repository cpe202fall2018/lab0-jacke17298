def weight_on_planets():
    # write your code here
    print("What do you weigh on earth? ", end='')

    planets = ["Mars", "Jupiter"]
    wmult = [0.38, 2.34]

    weight = int(input())
    result = "\n"

    for i in range(2):
        result += "On " + planets[i] + " you would weigh " + str(wmult[i]*weight) + " pounds."

        if i == 0:
            result += "\n"

    print(result, end='')
   
   
if __name__ == '__main__':
    weight_on_planets()
