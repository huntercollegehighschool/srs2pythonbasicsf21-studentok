"""
Define a function diamond that takes a single integer input size. The function then prints (doesn't have to return) a hollow diamond made of asterisks.

Hint: <string>.center(2*size - 1) may be helpful in your code (for center aligning)

Examples of what should appear:

diamond(4) -->
   *   
  * *  
 *   * 
*     *
 *   * 
  * *  
   * 

diamond(5) -->
      *      
     * *     
    *   *    
   *     *   
  *       *  
 *         * 
*           *
 *         * 
  *       *  
   *     *   
    *   *    
     * *     
      * 
"""

def diamond(size):
  string = ""
  for i in range(size):
    string = " "*(size-i) 
    string += "*" 
    if i != 0:
      string += " "*i*2
      string += "*" 
    print(string) 
  for i in range(2,size+1):
    string = " "*i 
    string += "*"
    if i != size:
      string += " "*(size-i)*2
      string += "*" 
    print(string)
    
