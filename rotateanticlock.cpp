#include <iostream>
using namespace std;


int main() {


    int a[3][3] = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    

    for (int i = 0; i < 2; i++)
    {
        for (int j = i+1; j < 3; j++)
        {
            swap(a[j][i], a[i][j]);
        }
    }
 

    for (int i = 0; i < 3; i++)
    {
        int start = 0;
        int end = 2;
       
        while (start < end)
        {
            swap(a[start][i], a[end][i]);
            start++;
            end--;
        }
    }


    return 0;
}
