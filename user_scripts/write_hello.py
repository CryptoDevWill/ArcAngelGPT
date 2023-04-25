def write_hello():
    # Open a file called hello.txt and write "Hello, World!" to it
    with open("hello.txt", "w") as f:
        f.write("Hello, World!")
        
    # Print a message to let the user know the program has finished
    print("File written successfully.")

# Call the write_hello() function
write_hello()
