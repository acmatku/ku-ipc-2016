#ifndef MAIN_CPP
#define MAIN_CPP

#include <iostream>
#include <sstream>
#include <string>
#include <queue>

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
void war(std::queue<int> &player1, std::queue<int> &player2, std::queue<int> &warStack) {
  int size;
  std::queue<int> temp;
  temp.push(player1.front());
  temp.push(player2.front());
  player1.pop();
  player2.pop();
  //Checks if each player's hand is smaller than 4, which would prevent 3 cards being moved to the back of the deck
  //If this has been called on multiple wars, increases the needed hand size by 3 each time
  if(player1.size() < 4) {
    size = player1.size();
    for(int i = 0; i < size; i++) {
      player1.pop();
    }
    return;
  } else if (player2.size() < 4) {
    size = player2.size();
    for(int i = 0; i < size; i++) {
      player2.pop();
    }
    return;
  }
  //If the hand size is valid
  else {
    //Put the next 3 cards to the back of each player's deck, then delete the unneeded values.
    for(int i = 0; i < 3;i++) {
      warStack.push(player1.front());
      player1.pop();
    }
    for(int i = 0; i < 3;i++) {
      warStack.push(player2.front());
      player2.pop();
    }
    for(int i = 0; i < 2; i++) {
      warStack.push(temp.front());
      temp.pop();
    }
    //If player 1 wins, put the winning cards on the bottom of their deck and delete the unneeded cards.
    if(player1.front() > player2.front()) {
      player1.push(player1.front());
      player1.push(player2.front());
      player1.pop();
      player2.pop();
      size = warStack.size();
      for(int i = 0; i < size; i++) {
        player1.push(warStack.front());
        warStack.pop();
      }

      return;

    } else if(player1.front() < player2.front()) {
      player2.push(player2.front());
      player2.push(player1.front());
      player1.pop();
      player2.pop();
      size = warStack.size();
      for(int i = 0; i < size; i++) {
        player2.push(warStack.front());
        warStack.pop();
      }

      return;
    }
    else {
      war(player1,player2,warStack);
    }
}
}

int main() {
//Vectors representing each player's hands
std::string deck1;
std::string deck2;
std::string test;
std::queue<int> player1;
std::queue<int> player2;
std::queue<int> warStack;

//Put the input into the needed vectors

std::getline(std::cin, deck1);
std::istringstream iss (deck1);
std::getline(std::cin, deck2);
std::istringstream iss2 (deck2);

while(std::getline(iss,test,' ')) {
  player1.push(convert(test[0]));
}
while(std::getline(iss2,test,' ')) {
  player2.push(convert(test[0]));
}

//Run the game until one player has no cards
while(!player1.empty() && !player2.empty()) {
//std::cout << player1.size() << player2.size() << "\n";
  //If player 1 wins, put both cards at the back of their deck and then delete each player's first cards
  if(player1.front() > player2.front()) {
    player1.push(player1.front());
    player1.push(player2.front());
    player1.pop();
    player2.pop();

  //If player 2 wins, put both cards at the back of their deck and then delete each player's first cards
  } else if(player1.front() < player2.front()) {
    player2.push(player2.front());
    player2.push(player1.front());
    player1.pop();
    player2.pop();
  //If there is a tie, do a war
  } else {
    war(player1,player2,warStack);
  }
  if(player1.empty()) {
    std::cout << "PLAYER 1";
  } else if(player2.empty()){
    std::cout << "PLAYER 2";
  }

}


// return 0;
};

#endif
