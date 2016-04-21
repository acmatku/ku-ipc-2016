#ifndef MAIN_CPP
#define MAIN_CPP

#include <iostream>
#include <bitset>
#include <string>
#include <fstream>

int main() {

  std::ifstream myfile;
  std::string message,value,translate;
  enum States{W,Z,O,I};
  States state = W;

  myfile.open("input1.txt");

  while(!myfile.eof()) {
    std::getline(myfile,value,' ');
     value = value.substr(2,1);

    switch(state) {
      case W: {
        if(value == "0") {
          state = Z;
          message += value;
        }
        break;
      }
      case Z: {
        if(value == "1") {
          state = O;
          message +=value;
        }
        else {
          state = W;
          message = "";
        }
        break;
      }
      case O: {
        if(value == "1" || value == "0") {
          message += value;
          state = I;
        }
        else {
          state = W;
          value = "";
        }
        break;
      }
      case I: {
        if(!(value == "1" || value == "0")) {
          state = W;
        }

        else {
          message += value;

          if(message.length() == 8) {
            std::bitset<8> bs(message);
            translate += char(bs.to_ulong());
            message = "";

          }
        }
        break;
      }
      }

    }

    std::cout << translate;



};

#endif
