import time
class App:
    @staticmethod
    def start() -> None:
        print("Calculator Program. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                time.sleep(1)
                break
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")
