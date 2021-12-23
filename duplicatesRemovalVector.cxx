#include<vector>
using namespace std;

int main()
{

	
	 vector<int> v {1,1,2,2,4,5,6,6,7,3,3,3};

	 if(v.size()==0 || v.size()==1) return 0;

	 int i=0;
	 int j=0;
	 for(i=0;i<v.size()-1;i++)
	 {
		 if(v[i] != v[i+1])
		 {
			 v[j++]=v[i];
		 }



	 }
	 v[j]=v[v.size()-1];

	 v.erase(v.begin()+j+1,v.end());

	 return 0;

	 
}