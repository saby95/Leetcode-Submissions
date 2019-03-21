#include<string.h> 
#define NO_OF_CHARS 256 

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
    if(s == ""){
        return 0;
    }
    int n = s.length(); 
    int cur_len = 1;  // lenght of current substring 
    int max_len = 1;  // result 
    int prev_index;  //  previous index 
    int i; 
    int *visited = (int *)malloc(sizeof(int)*NO_OF_CHARS); 
  
    /* Initialize the visited array as -1, -1 is used to 
       indicate that character has not been visited yet. */
    for (i = 0; i < NO_OF_CHARS;  i++) 
        visited[i] = -1; 
  
    /* Mark first character as visited by storing the index 
       of first   character in visited array. */
    visited[s[0]] = 0; 
  
    /* Start from the second character. First character is 
       already processed (cur_len and max_len are initialized 
       as 1, and visited[str[0]] is set */
    for (i = 1; i < n; i++) 
    { 
        prev_index =  visited[s[i]]; 
  
        /* If the currentt character is not present in the 
           already processed substring or it is not part of 
           the current NRCS, then do cur_len++ */
        if (prev_index == -1 || i - cur_len > prev_index) 
            cur_len++; 
  
        /* If the current character is present in currently 
           considered NRCS, then update NRCS to start from 
           the next character of previous instance. */
        else
        { 
            /* Also, when we are changing the NRCS, we 
               should also check whether length of the 
               previous NRCS was greater than max_len or 
               not.*/
            if (cur_len > max_len) 
                max_len = cur_len; 
  
            cur_len = i - prev_index; 
        } 
  
        // update the index of current character 
        visited[s[i]] = i; 
    } 
  
    // Compare the length of last NRCS with max_len and 
    // update max_len if needed 
    if (cur_len > max_len) 
        max_len = cur_len; 
  
    free(visited); // free memory allocated for visited 
    return max_len; 
    }
};

string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

int main() {
    string line;
    while (getline(cin, line)) {
        string s = stringToString(line);
        
        int ret = Solution().lengthOfLongestSubstring(s);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}