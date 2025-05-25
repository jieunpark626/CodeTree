#include <iostream>
#include <vector>

using namespace std;
vector<int> answer;
int K,N;
void Print(){
    for (int i=0; i<answer.size(); i++){
        cout<<answer[i]<<" ";
    }
    cout<<endl;
}

void Choose(int cur_num){
    if(cur_num == N+1){
        Print();
        return;
    }
    for (int i=1; i<=K; i++){
        answer.push_back(i);
        Choose(cur_num+1);
        answer.pop_back();
    }
}

int main(){
    cin >> K >> N;
    Choose(1);
    return 0;
}