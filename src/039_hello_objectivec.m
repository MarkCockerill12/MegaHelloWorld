#import <Foundation/Foundation.h>
#include <stdio.h>
int main() {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    printf("Hello World\n");
    [pool drain];
    return 0;
}
