# importing the module
import pywhatkit

# use Try Except to
# handle the Exceptions
try:

    # it will perform the Google search
    pywhatkit.search("google")
    print("Searching...")

except:

    # Printing Error Message
    print("An unknown error occurred")
