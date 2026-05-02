from TermSelect import Term_Select

options = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5", "Option 6", "Option 7", "Option 8"]
term_select = Term_Select()

try:
    
    answer1 = term_select.select_interface(
        message = "Please select first option?", 
        choices = options, 
        endless = True
    )

    answer2 = term_select.select_interface(
        message = "Please select second option?", 
        choices = options, 
        endless = False
    )

    print("Your choice:")
    print(answer1)
    print(answer2)

except InterruptedError:
    print("\nProgram interupted")
except Exception as unknown_error:
    print(unknown_error)
finally:
    input()