class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
      std::vector<std::pair<int, int>> zerosIndex;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == 0) {
                    zerosIndex.push_back(std::make_pair(i, j));
                }
            }
        }

        for (auto index : zerosIndex) {
            for (int row = 0; row < matrix.size(); row++) {
                for (int col = 0; col < matrix[0].size(); col++) {
                    if (row == index.first || col == index.second) {
                        matrix[row][col] = 0;
                    }
                }
            }
        }  
    }
};