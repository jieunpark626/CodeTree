#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> numbers;
int answer = 0;

void Choose(int cur_num){
    if (cur_num == N+1){
        answer++;
        return;
    }

    for (int i=1; i<=4; i++){
        //cout<<"curnum and i"<<cur_num<<i<<endl;
        if(cur_num + i - 1 > N)
            return;
        for (int j=0; j<i; j++){
            numbers.push_back(i);
        }
        Choose(cur_num+i);
        for (int k=0; k<i; k++){
            numbers.pop_back();
        }
    }
    return;

}

int main(){
    cin >> N;
    Choose(1);
    cout<<answer;
}