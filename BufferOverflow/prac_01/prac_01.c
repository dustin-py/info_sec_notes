// Code Observation:
    // The array of chars (buffer) is 10 bytes long.
    // The code uses the function strcpy.

// Code Task:
    // Try to copy more data than the buffer can handle,
    // using strcpy

#include <string.h>

int main(int argc, char** argv)
{
    argv[1] = (char*)"AAAAAAAAAAAAAA";
    char buffer[10];
    strcpy(buffer, argv[1]);
}

// Outcome:
    // We can see that argv[1] contains 15 'A' chars,
    // while the buffer can handle only 10. When the
    // program runs, the exceeding data has to go 
    // somewhere, and it will overwrite somthing in
    // the memory: this is a buffer overflow.

// Code Outcome:
    // Program Crashes.

// Post Evaluation:
    // The vulnerable function is `strcpy`.