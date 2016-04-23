//get input somehow

var input = ["8 11","XWX X X X  ", 
								"XWX X X X  ",
								"XWG X X X  ",
								"XWX G G G X",
								"XXXXXXXXX X",
								"        X X",
								"        X X",
								"        XXX"];

var xLen = input[0][0];
var yLen = input[0][2] + input[0][3];
console.log(xLen + " by " + yLen);
input.shift();

var activeWater = [];

console.log(input);
for(var i=0; i<xLen; i++){
	for(var j=0; j<yLen; j++){
		if(input[i][j] == "W"){
			var temp = new makeWater(i,j);
			activeWater.push(temp);
			input[i] = ssplice(input[i], j, 1, " ");
		}
	}
}

printArr[input];

var solution = solve(input, activeWater);
console.log("Solution: " + solution);

function makeWater(row,col){
	this.row = row;
	this.col = col;
	this.getMove = function(board){
        console.log("I'm at " + this.row + "," + this.col);
		var rowLen = board.length;
		var colLen = board[0].length;
		var result = [];
            if(this.row+1 < rowLen){
                if(board[(this.row+1)][(this.col)] == " "){//check if we can fall
                    result.push(this.row+1);
                    result.push(this.col);
                    result.push(0);
                    return result;
                }
            }
			if(this.col+2 < colLen){
                if((board[this.row][this.col+1] == "G")&&(board[this.row][this.col+2] == " ")){
                    result.push(this.row);
                    result.push(this.col+2);
                    result.push(1);
                    return result;
                }
			}
		return result;
	};
	console.log("Water made");
}

function paintScreen(blank, water){
	for(var i=0; i<water.length; i++){
		blank[water[i].row][water[i].col] = "W";
	}
	printArr(blank);
}

function deepCopy(arr){
	result = [];
	for(var i = 0; i<arr.length; i++){
		temp = [];
		for(var j = 0; j<arr[i].length; j++){
			temp.push(arr[i][j]);
		}
		result.push(temp);
	}
	return result;
}

function solve(blank, water){
	var pumped = 0;
	var notDone = true;
	while(notDone){
		var movesMade = 0;
		for(var i=0; i<water.length; i++){
			var state = deepCopy(blank);//start with fresh state
			paintScreen(state, water);//add in current position of all water
			var move = water[i].getMove(state);//get moves and make them
			console.log("Water returned the move: ");
			console.log(move.join(","));
			if (move.length>0){//if we got back a valid move, update the position
				water[i].row = move[0];
				water[i].col = move[1];
				pumped += move[2];
				movesMade++;
			}
		}
		if(movesMade === 0){
			notDone = false;
		}
	}
	return pumped;
}

function printArr(arr){
    for(var i = 0; i<arr.length; i++){
        temp = "" + i + " ";
        for(var j = 0; j<arr[i].length; j++){
            temp += arr[i][j];
        }
        console.log(temp);
    }
}

function ssplice(str, ind, count,val){
    var temp = str.split("");
    temp.splice(ind, count, val);
    return temp.join("");
}
