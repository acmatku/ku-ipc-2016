#ifndef MAIN_CPP
#define MAIN_CPP

#include <algorithm>
#include <vector>
#include <iostream>

int main() {

std::vector<char> cards = {'1','1','1','1','2','2','2','2','3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6','7','7','7','7','8','8','8','8','9','9','9','9','T','T','T','T','J','J','J','J','Q','Q','Q','Q','K','K','K','K'};
std::vector<char> player1;
std::vector<char> player2;

std::random_shuffle(cards.begin(), cards.end());

for(int i = 0; i < 26; i++) {
  player1.push_back(cards[i]);
  std::cout << player1[i];
}

std::cout << "\n";

for(int i = 0; i < 26; i++) {
  player2.push_back(cards[i+26]);
  std::cout << player2[i];
}


};

#endif
