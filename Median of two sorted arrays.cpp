class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int size1=nums1.size(), size2=nums2.size();
        int size = size1+size2;
        int arr[size];
        int i=0,j=0,k=0;
        for(;i<size;){
            if(j==size1){
                arr[i++] = nums2[k++];
            }
            else if(k==size2){
                arr[i++] = nums1[j++];
            }
            else{
                if(nums1[j]<nums2[k]){
                    arr[i++] = nums1[j++];
                }
                else{
                    arr[i++] = nums2[k++];
                }
            }
        }
        if(size%2!=0){
            return arr[size/2];
        }
        else{
            return ((arr[(size/2)-1]+arr[size/2])/2.0);
        }
        return 0;
    }
};

void trimLeftTrailingSpaces(string &input) {
    input.erase(input.begin(), find_if(input.begin(), input.end(), [](int ch) {
        return !isspace(ch);
    }));
}

void trimRightTrailingSpaces(string &input) {
    input.erase(find_if(input.rbegin(), input.rend(), [](int ch) {
        return !isspace(ch);
    }).base(), input.end());
}

vector<int> stringToIntegerVector(string input) {
    vector<int> output;
    trimLeftTrailingSpaces(input);
    trimRightTrailingSpaces(input);
    input = input.substr(1, input.length() - 2);
    stringstream ss;
    ss.str(input);
    string item;
    char delim = ',';
    while (getline(ss, item, delim)) {
        output.push_back(stoi(item));
    }
    return output;
}

int main() {
    string line;
    while (getline(cin, line)) {
        vector<int> nums1 = stringToIntegerVector(line);
        getline(cin, line);
        vector<int> nums2 = stringToIntegerVector(line);
        
        double ret = Solution().findMedianSortedArrays(nums1, nums2);

        string out = to_string(ret);
        cout << out << endl;
    }
    return 0;
}