#define _GNU_SOURCE
#define _XOPEN_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <dlfcn.h>

// Name: Sahal Shaikh
// netID:
// RUID:
// your code for time() goes here

int count = 1;

time_t time(time_t *tloc){
  struct tm tm;
  strptime("1 Sep 2020 01:00:00", "%d %b %Y %T", &tm);
  tm.tm_isdst = -1;
  
  time_t t =  mktime(&tm);
  
  if (count == 1){
    count = 2;
  }else if (count == 2){
    // Returns the real time 
    count = 1;
    time_t (*realtime)(time_t*) = dlsym(RTLD_NEXT, "time");
    time_t t = realtime(NULL);
    
    if (tloc != NULL){
      *tloc = t;
    }
    
    return t;
  }

  if (tloc != NULL){
    *tloc = t;
  }
  
  return t;
}

