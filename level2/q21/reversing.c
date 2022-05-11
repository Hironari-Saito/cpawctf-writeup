#include<stdio.h>

int main(int argc, const char **argv, const char **envp) {

  char a[] = "cpaw{";
  char flag[] = "yakiniku!";
  char b = '}';
  int x = 5;

  printf("%s", a);
  if (x == 5) {
    printf("%c", b);
  } else {
    for(int i = 0; i <= 8; i++ ) {
      putchar(flag[i]);
    }
    printf("%c", b);
  }
}

