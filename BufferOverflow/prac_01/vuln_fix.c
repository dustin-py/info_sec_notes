// Resolution:
    // There is a safe version of the `strcpy` function, and
    // it is called `strncpy` ( notice the 'n' in the function
    // name). With this knowledge, we can say that a safe
    // implementation of the previous program would be something
    // like this:

#include <string.h>

int main(int argc, char** argv)
{
    argv[1] = (char*)"AAAAAAAAAAAAAAA";
    char buffer[10];
    strncpy(buffer, argv[1], sizeof(buffer));
    return 0;
}
