#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <dlfcn.h>
#include <string.h>

// Name: Sahal Shaikh 
// netID: 
// RUID:

// your code for readdir goes here


struct dirent *readdir(DIR *dirp){
  struct dirent *d;

  struct dirent* (*original_readdir)(DIR*) = dlsym(RTLD_NEXT, "readdir");
  d = original_readdir(dirp);
  char* hidden_file = getenv("HIDDEN");

  if (d != NULL) {
    if (strcmp(hidden_file, d->d_name) == 0) {
      d = original_readdir(dirp);
      return d;
    }
  }
  
  return d;
}
