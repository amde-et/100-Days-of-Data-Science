class Solution {
private:
    bool isValid(vector<vector<char>>& board, int i, int j, char value){
        int sRow = i/3*3;
        int sCol = j/3*3;

        for(int k=0; k<9; k++){
            if(board[i][k] == value) return false;
            if(board[k][j] == value) return false;
            if(board[k/3+sRow][k%3+sCol] == value) return false;
        }
        return true;
    }
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j] == '.') continue;
                char value = board[i][j];
                board[i][j] = '.';
                if(!isValid(board,i,j, value)) return false;
                board[i][j] = value;
            }
        }
        return true;
    }
};