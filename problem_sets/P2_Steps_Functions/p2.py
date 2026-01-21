#      program: p2.py
#         date:
#       author:
#  description: Calculates miles walked from steps and stride length,
#               and reports how far over or under 10,000 steps.
#               Demonsrates use of return functions.

# functions

def get_steps():
    return -1


def get_stride_inches():
    return -1


def calculate_miles(steps, stride_inches):
    return -1


def additional_steps_needed(steps):
    return -1

def miles_output_line(steps, miles):
    msg = "miles walked"
    return msg

def steps_output_line( additional ):
    msg = "steps needed"
    
    return msg

# +------ do not modify this section ----------+
def main():

    # input
    steps = get_steps()
    stride_inches = get_stride_inches()

    # processing
    miles = calculate_miles(steps, stride_inches)
    additional = additional_steps_needed(steps)

    # output
    print( miles_output_line(steps, miles) )
    print( steps_output_line(additional) )

if __name__ == "__main__":
    main()

# +------ do not modify this section ----------+
