#ifndef WARGEN_CPP
#define WARGEN_CPP

#include <algorithm>
#include <vector>
#include <iostream>
#include <fstream>

int main() {

std::vector<char> cards = {'1','1','1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','T','T','T','T','J','J','J','J','Q','Q','Q','Q','K','K','K','K'};
std::ofstream myFile;
myFile.open("input1.txt");

std::random_shuffle(cards.begin(), cards.end());

for(int i = 0; i < 52; i++) {
  myFile << cards[i];
  if(i==25) {
    myFile << "\n";
  }
}

};

#endif
