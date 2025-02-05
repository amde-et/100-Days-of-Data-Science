class Solution {
public:
    string sortSentence(string s) {
        vector<string> v(10, ""); 
        string hold = "";
        for(char i: s){ 
            if(isalpha(i)){ 
                hold += i; 
            }
            
            else{  
                if(!isblank(i)){ 
                    v[i - '0'] = hold; 
                    hold = ""; 
                }
            }
        }
        for(string i: v){
            if(i!= "") 
                hold += i + " "; 
        }
        hold.pop_back(); 
        return hold;
    }
};