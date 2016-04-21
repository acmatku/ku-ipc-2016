#ifndef MAIN_CPP
#define MAIN_CPP

#include <vector>
#include <iostream>
#include <fstream>

int convert(char card) {
    switch(card) {
      case 'T': return(10); break;
      case 'J': return(11); break;
      case 'Q': return(12); break;
      case 'K': return(13); break;
      case 'A': return(14); break;
      default: return(card - '0'); break;
    }
}

//
void war(std::vector<int> &player1, std::vector<int> &player2, std::vector<int> &warStack) {
  //Checks if each player's hand is smaller than 4, which would prevent 3 cards being moved to the back of the deck
  //If this has been called on multiple wars, increases the needed hand size by 3 each time
  if(player1.size() <= 3) {
    player1.clear();
    return;
  } else if (player2.size() <= 3) {
    player2.clear();
    return;
  }
  //If the hand size is valid
  else {
    //Put the next 3 cards to the back of each player's deck, then delete the unneeded values.
    for(int i = 0; i < 3;i++) {
      warStack.push_back(player1[i]);
      warStack.push_back(player2[i]);
      player1.erase(player1.begin());
      player2.erase(player1.begin());
    }
    //If player 1 wins, put the winning cards on the bottom of their deck and delete the unneeded cards.
    if(player1[0] > player2[0]) {
      for(int i = 0; i < warStack.size(); i++) {
        player1.push_back(warStack[0]);
        warStack.erase(warStack.begin());
      }
      player1.push_back(player1[0]);
      player1.push_back(player2[0]);
      player1.erase(player1.begin());
      player2.erase(player2.begin());
      return;
    } else if(player1[0] < player2[0]) {
      for(int i = 0; i < warStack.size(); i++) {
        player2.push_back(warStack[0]);
        warStack.erase(warStack.begin());
      }
      player2.push_back(player1[0]);
      player2.push_back(player2[0]);
      player1.erase(player1.begin());
      player2.erase(player2.begin());
      return;
    } else {
      warStack.push_back(player1[0]);
      warStack.push_back(player2[0]);
      player1.erase(player1.begin());
      player2.erase(player2.begin());
      war(player1,player2,warStack);
      return;
    }
}
}

int main() {
//Vectors representing each player's hands
std::string deck1;
std::string deck2;
std::vector<int> player1;
std::vector<int> player2;
std::vector<int> warStack;
char c;

//Put the input into the needed vectors
for(int i = 0; i < 26; i++) {
  std::cin >> c;
  player1.push_back(convert(c));
}

 for(int i = 0; i < 26; i++) {
  std::cin >> c;
  std::cout << player1[i];
  player2.push_back(convert(c));
  //std::cout << i;
}

std::cout << "test";
//Run the game until one player has no cards
while(!player1.empty() || !player2.empty()) {

  //If player 1 wins, put both cards at the back of their deck and then delete each player's first cards
  if(player1[0] > player2[0]) {
    player1.push_back(player1[0]);
    player1.push_back(player2[0]);
    player1.erase(player1.begin());
    player2.erase(player2.begin());
  //If player 2 wins, put both cards at the back of their deck and then delete each player's first cards
  } else if(player1[0] < player2[0]) {
    player2.push_back(player2[0]);
    player2.push_back(player1[0]);
    player1.erase(player1.begin());
    player2.erase(player2.begin());
  //If there is a tie, do a war
  } else {
    warStack.push_back(player1[0]);
    warStack.push_back(player2[0]);
    player1.erase(player1.begin());
    player2.erase(player2.begin());
    war(player1,player2,warStack);
  }

}

if(player1.empty()) {
  std::cout << "Player 1 wins";
}
else {
  std::cout << "Player 2 wins";
}
return 0;
};

#endif
