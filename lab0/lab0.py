# MIT 6.034 Lab 0: Getting Started
# Written by jb16, jmn, dxh, and past 6.034 staff

from point_api import Point

#### Multiple Choice ###########################################################

# These are multiple choice questions. You answer by replacing
# the symbol 'None' with a letter (or True or False), corresponding 
# to your answer.

# True or False: Our code supports both Python 2 and Python 3
# Fill in your answer in the next line of code (True or False):
ANSWER_1 = False

# What version(s) of Python do we *recommend* for this course?
#   A. Python v2.3
#   B. Python V2.5 through v2.7
#   C. Python v3.2 or v3.3
#   D. Python v3.4 or higher
# Fill in your answer in the next line of code ("A", "B", "C", or "D"):
ANSWER_2 = "D"


################################################################################
# Note: Each function we require you to fill in has brief documentation        # 
# describing what the function should input and output. For more detailed      # 
# instructions, check out the lab 0 wiki page!                                 #
################################################################################


#### Warmup ####################################################################

def is_even(x):
    """If x is even, returns True; otherwise returns False"""
    if x >= 0:
        return (x % 2) == 0
    return False

def decrement(x):
    """Given a number x, returns x - 1 unless that would be less than
    zero, in which case returns 0."""
    if x <= 0:
        return 0
    
    return x - 1

def cube(x):
    """Given a number x, returns its cube (x^3)"""
    return x**3


#### Iteration #################################################################

def is_prime(x):
    """Given a number x, returns True if it is prime; otherwise returns False"""
    
    if x <= 1:
        return False
    
    if type(x) == float and type(x) != int: 
        return False
    
    for i in range(2,x):
        
        if (x % i) == 0:
            return False
    
    return True
    

def primes_up_to(x):
    """Given a number x, returns an in-order list of all primes up to and including x"""
    
    listOfPrimes = []
    
    for i in range(2,int(x+1)):
        
        if is_prime(i):
            listOfPrimes.append(i)
    
    return listOfPrimes
        


#### Recursion #################################################################

def fibonacci(n):
    """Given a positive int n, uses recursion to return the nth Fibonacci number."""
    
    if n < 0:
        raise ValueError("fibonacci: input must not be negative")
    
    elif n < 3:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def expression_depth(expr):
    """Given an expression expressed as Python lists, uses recursion to return
    the depth of the expression, where depth is defined by the maximum number of
    nested operations."""
    
    if len(expr) == 1:
        return 0
    
    depths = set([1])
    
    for elem in expr:
        
        if type(elem) is list:
            depths.add(expression_depth(elem)+1)
            
    return max(depths)


#### Built-in data types #######################################################

def remove_from_string(string, letters):
    """Given an original string and a string of letters, returns a new string
    which is the same as the old one except all occurrences of those letters
    have been removed from it."""
    
    for l in letters:
        string = string.replace(l,'')
        
    return string
            

def compute_string_properties(string):
    """Given a string of lowercase letters, returns a tuple containing the
    following three elements:
        0. The length of the string
        1. A list of all the characters in the string (including duplicates, if
           any), sorted in REVERSE alphabetical order
        2. The number of distinct characters in the string (hint: use a set)
    """
    
    return (len(string), sorted(string,reverse=True),len(set(string)))

def tally_letters(string):
    """Given a string of lowercase letters, returns a dictionary mapping each
    letter to the number of times it occurs in the string."""
    
    dictString = {}
    
    for i in string:
        if i in dictString:
            dictString[i] += 1
        else:
            dictString[i] = 1
    
    return dictString


#### Functions that return functions ###########################################

def create_multiplier_function(m):
    """Given a multiplier m, returns a function that multiplies its input by m."""
    return lambda x : x*m

def create_length_comparer_function(check_equal):
    """Returns a function that takes as input two lists. If check_equal == True,
    this function will check if the lists are of equal lengths. If
    check_equal == False, this function will check if the lists are of different
    lengths."""
    
    if check_equal:
        return lambda x,y : len(x) == len(y)
    else:
        return lambda x,y : len(x) != len(y)


#### Objects and APIs: Copying and modifying objects ############################

def sum_of_coordinates(point):
    """Given a 2D point (represented as a Point object), returns the sum
    of its X- and Y-coordinates."""
    return point.getX() + point.getY()

def get_neighbors(point):
    """Given a 2D point (represented as a Point object), returns a list of the
    four points that neighbor it in the four coordinate directions. Uses the
    "copy" method to avoid modifying the original point."""
    x = point.getX()
    y = point.getY()
    l, r, u, d = point.copy(),point.copy(),point.copy(),point.copy()
    l.setX(x-1)
    r.setX(x+1)
    u.setY(y+1)
    d.setY(y-1)
    return [l,r,u,d]


#### Using the "key" argument ##################################################

def sort_points_by_Y(list_of_points):
    """Given a list of 2D points (represented as Point objects), uses "sorted"
    with the "key" argument to create and return a list of the SAME (not copied)
    points sorted in decreasing order based on their Y coordinates, without
    modifying the original list."""
    my_sorting_function = lambda tup : tup.getY() # [1] is the second element
    sorted_list = sorted(list_of_points, key=my_sorting_function)
    return sorted_list[::-1]

def furthest_right_point(list_of_points):
    """Given a list of 2D points (represented as Point objects), uses "max" with
    the "key" argument to return the point that is furthest to the right (that
    is, the point with the largest X coordinate)."""
    sort_by_x = lambda x : x.getX()
    sorted_list_by_x = sorted(list_of_points,key=sort_by_x,reverse=True)
    
    return sorted_list_by_x[0]


#### SURVEY ####################################################################

# How much programming experience do you have, in any language?
#     A. No experience (never programmed before this lab)
#     B. Beginner (just started learning to program, e.g. took one programming class)
#     C. Intermediate (have written programs for a couple classes/projects)
#     D. Proficient (have been programming for multiple years, or wrote programs for many classes/projects)
#     E. Expert (could teach a class on programming, either in a specific language or in general)

PROGRAMMING_EXPERIENCE = ""


# How much experience do you have with Python?
#     A. No experience (never used Python before this lab)
#     B. Beginner (just started learning, e.g. took 6.0001)
#     C. Intermediate (have used Python in a couple classes/projects)
#     D. Proficient (have used Python for multiple years or in many classes/projects)
#     E. Expert (could teach a class on Python)

PYTHON_EXPERIENCE = ""


# Finally, the following questions will appear at the end of every lab.
# The first three are required in order to receive full credit for your lab.

NAME = None
COLLABORATORS = None
HOW_MANY_HOURS_THIS_LAB_TOOK = None
SUGGESTIONS = None #optional
