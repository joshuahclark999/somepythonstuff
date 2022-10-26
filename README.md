# Functions


 - **Organize your code**
    - Increases modularity
    - Enables expandability
    - DRY (don't repeat yourself)

&nbsp;
 - **Single-responsibility principle**
    - a good function should only do one thing
    - if you want your function to do something else, write another function and chain them together!


&nbsp;
# Defining a Function


&nbsp;
### Definition Syntax:

&nbsp;
1. Use the keyword `def` to start a function definition

```python
def
```


&nbsp;
2. Write the function name

```python
def func_name
```

&nbsp;
3. Add any necessary **PARAMETERS** inside of parens `()`, separated by commas if there are more than 1, and end with a `:`

```python
# FUNCTION WITH PARAMETERS

def func_name(param_1, param_2):



# FUNCTION WITHOUT PARAMETERS

def func_name():
```


&nbsp;
### Things to Note:
 - You **MUST** indent the code block beneath your function definition

 - Your code will not **RUN** during the definition

 - We use the **PARAMETERS** as placeholders for the **ARGUMENTS** we will pass to our function when we **RUN** our function

 - Variables defined inside a function's code block are **ONLY** accessible within the function itself


&nbsp;
## Examples:

```python
# FUNCTION DEFINITION SYNTAX

def func_name(param_1, param_2):
   
    # code block goes here



# VARIABLES DEFINED WITHIN A FUNCTION ONLY EXIST IN THE FUNCTION'S SCOPE

def func_name(param_1, param_2):

    func_var_1 = 'I only exist in func_name'    # we defined func_var_1 in the func_name function
    
    print(func_var_1)       # prints as expected, because func_var_1 is in func_name's scope


print(func_var_1)       # causes an NameError, because func_var_1 ONLY exists in func_name's scope

```




&nbsp;
# Execution of Functions


&nbsp;
### Running Your Function:
 - A few terms for **RUNNING** a function that mean the same thing:
    
    - **CALL**
    - **RUN**
    - **INVOKE**
    - **EXECUTE**


- To **EXECUTE** a function, you must have defined that same function above the line you want to **CALL** it on.


&nbsp;
### Execution Syntax:

&nbsp;

1. Write the function name
```python
func_name
```
&nbsp;
2. Use parens `()` and pass any **ARGUMENTS** necessary to the function, separated by commas if there are more than 1. If there are no arguments necessary to **INVOKE** your function, Use the parens `()` without anything inside of them

```python
# CALLING A FUNCTION WITH 2 ARGUMENTS

func_name(arg_1, arg_2)



# CALLING A FUNCTION WITH NO ARGUMENTS

func_name()
```
&nbsp;
3. Note you **do not** use the def keyword when **RUNNING** your function




&nbsp;
## Example:
```python
# First, define your function and PARAMETERS

def func_name(param_1, param_2):
    
    # code block goes here


# Second, call your function with the ARGUMENTS you want to run it with

func_name(arg_1, arg_2)

```

&nbsp;
# Returning Data


&nbsp;
### The return Keyword
 - `return` will capture the result from a function and give its value to the line in the code where it was **CALLED**

 - The data returned by `return` can be saved to a variable to be used in other parts of your code 

 - Returning **IS NOT** the same as printing

 - If no `return` keyword is used, python will return `None` by default

 - If a `return` is hit within a loop, the loop will stop, and `return` whatever value is assigned on that line


&nbsp;
## Examples:


&nbsp;
#### return VS print()

```python
# FUNC DEFINITION WITH 2 PARAMETERS (num_1 AND num_2) THAT RETURNS num_1 + num_2

def adder(num_1, num_2):

    return num_1 + num_2    # returning the sum of num_1 and num_2



# EXAMPLE 1: CALLING the func with ARGUMENTS 4 and 5

adder(4, 5)     # note nothing will print to the screen



# EXAMPLE 2: CALLING the func with ARGUMENTS 4 and 5 and printing the result

print(adder(4, 5))      # will print 9



# EXAMPLE 3: CALLING the func with ARGUMENTS 4 and 5, saving the result to a variable, then printing the variable

sum_of_1_and_2 = adder(4, 5)    # assigning the variable

print(sum_of_1_and_2)       # will print 3




# FUNC DEFINITION THAT PRINTS INSTEAD OF RETURNING IN THE FUNC:

def multiplier(num_1, num_2):

    print(num_1 * num_2)    # note we PRINTING not RETURNING


print(multiplier(2, 3))     # prints 6 and 'None' on a newline




# FUNC DEFINITION THAT RETURNS INSTEAD OF PRINTING IN THE FUNC:

def multiplier(num_1, num_2):

    return num_1 * num_2    # note we are RETURNING not PRINTING


print(multiplier(2, 3))     # prints 6

```


&nbsp;
#### return IN A LOOP

```python

def count_to_10():      # notice there are no PARAMETERS in this func

    for num in range(11):   # range defaults from 0, and goes to the passed ARGUMENT excusively
        
        print('num is currently: ' + num)   # print out the current iteration of ITERATOR num

        if num == 5:        # when the ITERATOR num is equal to 5
            
            return 'Done'   # RETURN the string 'Done'


print(count_to_10())        # notice the parens () to CALL the func, use print to see the output
                            
```


**QUESTION**: Why didn't count_to_10 count all the way to 10?

Once a `return` statement is reached in a loop, the loop stops and **returns** whatever is assigned to the line the return statement is on. In this case, when the **ITERATOR** `num` is equal to 5, our if statement is `True`, and python steps into the conditional statement.  It then reads the `return` statement, stops the loop, and **returns** the string `'Done'`.

