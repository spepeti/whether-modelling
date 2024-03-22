def __init__(self):
        pass

    def temperature_modeling(self, a, b, c, time):
        """ Function to model temperature using a quadratic equation.
       
        Parameters:
        a (float): Coefficient a.
        b (float): Coefficient b.
        c (float): Coefficient c.
        time (float): Time in hours.
       
        Returns:
        float: Calculated temperature.
        """
        temperature = a * time**2 + b * time + c
        return temperature

    def get_user_input_coefficients(self):
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        return a, b, c

    def read_coefficients_from_file(self, filename):
        """ Function to read coefficients from a file.
       
        Parameters:
        filename (str): Name of the file containing coefficients.
       
        Returns:
        tuple: Coefficients (a, b, c) read from the file.
        """
        with open(filename, 'r') as file:
            coefficients = [float(x) for x in file.readline().split()]
        return tuple(coefficients)

    def get_time_input(self):
        time = float(input("Enter time in hours: "))
        return time

    def write_temperature_to_file(self, filename, time, temperature):
        """ Function to write temperature to a file.
       
        Parameters:
        filename (str): Name of the file to write temperature to.
        time (float): Time for which temperature is calculated.
        temperature (float): Calculated temperature.
        """
        with open(filename, 'w') as file:
            file.write(f"Time: {time} hours\nTemperature: {temperature}")

    def run(self):
        # Step 1: Hard-coded Variables for Weather Modeling
        print("Step 1: Hard-coded Variables for Weather Modeling")
        a_hardcoded, b_hardcoded, c_hardcoded = 0.1, 2, 30
        time_hardcoded = 6
        temperature_hardcoded = self.temperature_modeling(a_hardcoded, b_hardcoded, c_hardcoded, time_hardcoded)
        print("Temperature for hardcoded coefficients at time", time_hardcoded, ": ", temperature_hardcoded, "\n")

        # Step 2: Keyboard Input for Weather Modeling
        print("Step 2: Keyboard Input for Weather Modeling")
        a_keyboard, b_keyboard, c_keyboard = self.get_user_input_coefficients()
        time_keyboard = self.get_time_input()
        temperature_keyboard = self.temperature_modeling(a_keyboard, b_keyboard, c_keyboard, time_keyboard)
        print("Temperature for user-input coefficients at time", time_keyboard, ": ", temperature_keyboard)

        # Step 3: File Input for Weather Modeling
        print("Step 3: File Input for Weather Modeling")
        filename = "coefficients.txt"
        a_file, b_file, c_file = self.read_coefficients_from_file(filename)
        time_file = self.get_time_input()
        temperature_file = self.temperature_modeling(a_file, b_file, c_file, time_file)
        print("Temperature for coefficients from file at time", time_file, ": ", temperature_file)

        # Step 4: File Output for Weather Modeling
        print("Step 4: File Output for Weather Modeling")
        output_filename = "temperature_output.txt"
        self.write_temperature_to_file(output_filename, time_file, temperature_file)
        print("Temperature written to", output_filename)


# Main function to execute the program
def main():
    weather_model = WeatherModel()
    weather_model.run()


if __name__ == "__main__":
    main(
