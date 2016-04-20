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
void war(std::vector<int> &player1, std::vector<int> &player2, int &start) {
  //Checks if each player's hand is smaller than 4, which would prevent 3 cards being moved to the back of the deck
  //If this has been called on multiple wars, increases the needed hand size by 3 each time
  if(player1.size() <= 3+start) {
    player1.clear();
    return;
  } else if (player2.size() <= 3+start) {
    player2.clear();
    return;
  }
  //If the hand size is valid
  else {
    //Put the next 3 cards to the back of each player's deck, then delete the unneeded values.
    for(int i = 1+start; i < 4+start;i++) {
      player1.push_back(player1[i]);
      player2.push_back(player2[i]);
      player1.erase(player1.begin()+1+start);
      player2.erase(player1.begin()+1+start);
    }
    //If player 1 wins, put the winning cards on the bottom of their deck and delete the unneeded cards.
    if(player1[1+start] > player2[1+start]) {
      player1.push_back(player1[1+start]);
      player1.push_back(player2[1+start]);
      player1.erase(player1.begin()+1+start);
      player2.erase(player2.begin()+1+start);
      start = 0;
      return;
    //If player 2 wins, put the winning cards on the bottom of their deck and delete the unneeded cards.
    } else if(player1[1+start] < player2[1+start]) {
      player2.push_back(player1[1+start]);
      player2.push_back(player2[1+start]);
      player2.erase(player2.begin()+1+start);
      player1.erase(player1.begin()+1+start);
      start = 0;
      return;
    //If there is a tie, increase the starting index by 3 and do another war.
    } else {
      start += 3;
      war(player1,player2,start);
    }
  }

}

int main() {
//Vectors representing each player's hands
std::vector<int> player1;
std::vector<int> player2;
std::ifstream myFile;
//Int passed by reference used to determine if a war has been called multiple times
int start;

myFile.open("input1.txt");

//Put the input into the needed vectors
for(int i = 0; i < 26; i++) {
  player1.push_back(convert(myFile.get()));
}
myFile.ignore();
 for(int i = 0; i < 26; i++) {
  player2.push_back(convert(myFile.get()));
}

//Run the game until one player has no cards
while(!player1.empty() || !player2.empty()) {
  //If player 1 wins, put both cards at the back of their deck and then delete each player's first cards
  if(player1[0] > player2[0]) {
    player1.push_back(player1[0]);
    player1.push_back(player2[0]);
    player1.erase(player1.begin());
    player2.erase(player2.begin());
    start = 0;
  //If player 2 wins, put both cards at the back of their deck and then delete each player's first cards
  } else if(player1[0] < player2[0]) {
    player2.push_back(player1[0]);
    player2.push_back(player2[0]);
    player1.erase(player1.begin());
    player2.erase(player2.begin());
    start = 0;
  //If there is a tie, do a war
  } else {
    war(player1,player2,start);
  }
}

};

#endif
