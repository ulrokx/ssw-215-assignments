Richard Kirk

*I pledge my honor that I have abided by the Stevens Honor System.*

# Time Complexity Analysis

## SSW-215 - Assignment for Week 8B


A. The program has 3 loops, not nested. The first only runs 7 times, and the next two run *n* times where *n* is the length of the input array. We can assume that the inner operations (print) take constant time. The detailed time complexity is *O(7 + n + n)*, so overall it is *O(n)*, where *n* is the length of the input array.

B. The program has 2 loops, where one is nested in the other. Both loops run *n* times, where *n* is the length of the input array. We can assume the inner operations (print) take constant time. Therefore, the overall time complexity is *O(n<sup>2</sup>)*.

C. The program has 2 loops, where one is nested in the other. The outer loop runs *n/2* times and the inner runs *(n-1)/2* times. Together, the detailed time complexity is *O((n/2) ⋅ (n-1)/2)*, so the overall is *O(n(n-1)/4)*, or simply *O(n<sup>2</sup>)*

D. The program has 2 loops, and they are not nested. The first loop runs *n* times, and the second runs *m* times. We can assume that the inner operations (addition and rand()) run in constant time. The detailed and overall time complexity therefore is *O(n+m)*

E. The program has 1 loop. The loop runs *n* times, where *n* is the length of the input array. The detailed and overall time complexity is *O(n)* 
    
