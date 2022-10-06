class Checker {
    constructor(location, Pointer, color) {
        this.location = [location[0], location[1]]; //[y, x] format
        this.HTMLPointer = Pointer;
        this.color = color;
        this.team = parseInt(Pointer.classList[1].split("r").pop());
    }
    appendChecker() {
        return this.HTMLPointer;
    }
    getAvailableMoves() {
        let location = this.location;
        let moves = checkDiagonals(location);
        let final = [];
        for (let i = 0; i < moves.length; i++) {
            if (this.team == 0) {
                if (!(moves[i][0] < this.location[0])) {
                    final.push(moves[i]);
                } 
            } else {
                if (!(moves[i][0] > this.location[0])) {
                    final.push(moves[i]);
                }
            }
        }
        return final;
    }
    static makeCheckers(checkers) {
        let newList = []
        let count = 0;
        let i = 0;
        for (let line of checkers) {
            let temp = []
            let ii = 0
            for (let checker of line) {
                if (checker != 0) {
                    let color = (count < 32) ? 0 : 1;
                    c = new Checker([i, ii], checker, color);
                    temp.push(c);
                } else {
                    temp.push(0);
                }
                ii++; count++;
            }
            i++; newList.push(temp);  
        }
        return newList;
    }
    findIn2dArray(array) {
        for (let i = 0; i < array.length; i++) {
            for (let ii = 0; ii < array.length; ii++) {
                if (this == array[i][ii]) {
                    return [i, ii];
                }
            }
        }
    }
    print() {
        console.log(this.HTMLPointer + this.location);
    }
    updateLists(location) {
        let y = location[0]; let x = location[1];
        let oldy = this.location[0]; let oldx = this.location[1];
        checker_list[oldy][oldx] = 0; checker_list[oldy][oldx] = 0;
        checker_list[y][x] = this;
        board[y][x] = this.HTMLPointer;
    }
    move(location) {
        this.updateLists(location);
        for (let i = 0; i < nodes.length; i++) {
            for (let ii = 0; ii < nodes.length; ii++) {
                let node1 = nodes[i][ii];
                if (node1.firstChild == this) {
                    node1.remove(node1.firstChild);
                }
                if ([i, ii] = location) {
                    for (let i = 0; i < checker_list.length; i++) {
                        for (let ii = 0; ii < checker_list.length; ii++) {
                            if (checker_list[i][ii] == this) {
                                console.log(board[i][ii]);
                                node1.appendChild(board[i][ii]);
                            }
                        }
                    }
                    
                }
            }
        }
        //call update here
    }
}
class King extends Checker {
    constructor(c) {
        this.location = c.location
        this.HTMLPointer = c.HTMLPointerPointer;
        this.color = c.color;
        this.team = c.team
    }
    getAvailableMoves() {
        let location = this.location;
        return checkDiagonals(location);
    }
}

//global variables
var nodes; //array of environment pointers
var checker_list; //array of checker objects and 0s
var board; //array of checker pointers and 0s
const MOUSE_OVER_COLOR = "green";
const DEFAULT_COLOR0 = "burlywood";
const DEFAULT_COLOR1 = "brown";
const USER_TEAM = 1; //tags the checkers playable by the user
var recentlyClicked;
//end of global variables

function game() {//put gameflow in here
    buildGame();
}
function buildGame() { //call this first
    nodes = remove(buildBoard());
    board = buildCheckers(nodes);
    nodes = reformat2d(nodes);
    checker_list = Checker.makeCheckers(board);
}

function findIn2dArray(array, thing) {
    for (let i = 0; i < array.length; i++) {
        for (let ii = 0; ii < array.length; ii++) {
            if (thing == array[i][ii]) {
                return [i, ii];
            }
        }
    }
}
function remove(nodes) {
        let result = [];
        for (let i = 1; i < nodes.length; i++) {
            result.push(nodes[i])
        }
        return result;
    }
function buildBoard() {
    let location = document.getElementById("main_board")
    let size = 64;
    c = 0;
    prevC = 0;
    for (let i = 1; i < size + 1; i++) {
        let element = document.createElement("div");
        element.classList.add("boardAreas");
        element.classList.add("boardArea" + (c%2))
        location.appendChild(element);
        c++;
        if (i % 8 == 0 && i != 0) {
            c++;
        }
    }
    return location.childNodes;
}

function pointDistance(p1, p2) {
    return Math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2);
}
function checkDiagonals(location) {
    function rotate(a, b) {
        if (a == b) {//reflect over x 
            return [-a, b];   
        } else {
            return [a, -b];
        }
    }
    let result = [];
    let item2 = [];
    let y = location[0];
    let x = location[1];
    a = 1;
    b = 1;
    for (let i = 0; i < 4; i++) {
        let temp = rotate(a, b);
        result.push([y + temp[0], x + temp[1]]);
        item2.push([y + 2 * temp[0], x + 2 * temp[0]])
        a = temp[0];
        b = temp[1];
    }
    let final = [];
    let i = 0;
    for (item of result) {
        if (item[0] > -1 && item[1] > -1  && item[0] < 8 && item[1] < 8) {
            let value = index2d(board, item);
            if (value == 0) {
                final.push(item);
            } else {
                if (item2[0] > -1 && item2[1] > -1 && item2[0] < 8 && item2[1] < 8) {
                    if (index2d(board, item2[i]) == 0) {
                        final.push(item2[i]);
                    }
                } 
            }
        }
        i++;
    }
    return final;
}

function changeWhenOver() {
    let checker;
    for (let i = 0; i < board.length; i++) {
        for (let ii = 0; ii < board.length; ii++) {
            if (board[i][ii] == this) {
                checker = checker_list[i][ii];
            }
        }
    }
    let moves = checker.getAvailableMoves();
    for (move of moves) {
        if (node.style.backgroundColor != "purple") {
            let node = index2d(nodes, move);
            node.style.backgroundColor = MOUSE_OVER_COLOR;
        }
    }
}
function noYellow() { //scope in javascript is fucking retarded and I want to kill myself
    for (line of board) {
        for (checker2 of line) {
            if (checker2 != 0) {
                if (checker2.style.backgroundColor == "yellow") {
                    return false;
                }
            }
        }
    }
    return true;
}
function clickChecker() {
    let checker = this;
    if (noYellow() || this.style.backgroundColor == "yellow") {
        if (checker.style.backgroundColor == "yellow") {
            setDefaultBackgroundColorChecker(checker);
        } else {
            checker.style.backgroundColor = "yellow";
        }
        let checker_object;
        for (let i = 0; i < board.length; i++) {
            for (let ii = 0; ii < board.length; ii++) {
                if (board[i][ii] == this) {
                    checker_object = checker_list[i][ii];
                }
            }
        }
        let available = checker_object.getAvailableMoves();
        recentlyClicked = checker_object;
        prepare(available);
    }
}
function clickEnvironment() {
    for (let i = 0; i < nodes.length; i++) {
        for (let ii = 0; ii < nodes.length; ii++) {
            if (nodes[i][ii] == this) {
                recentlyClicked.move([i,ii]);
            }
        }
    }
}
function prepare(available) {
    for (move of available) {
        y = move[0];
        x = move[1];
        let current = nodes[y][x];
        current.style.backgroundColor = "purple";
        current.addEventListener("click", clickEnvironment);
    }
}
function setDefaultBackgroundColorChecker(checker) {
    if (checker.classList.contains("checker0")) {
        checker.style.backgroundColor = "white";
    } else {
        checker.style.backgroundColor = "black";
    }
    for (line of nodes) {
        for (node of line) {
            if (node.style.backgroundColor == "purple") {
                setDefaultBackgroundColor(node);
            }
        }
    }
}
function setDefaultBackgroundColor(node) {
    if (node.classList.contains("boardArea0")) {
        node.style.backgroundColor = DEFAULT_COLOR0;
    } else {
        node.style.backgroundColor = DEFAULT_COLOR1;
    }
}
function changeWhenOut() {
    for (line of nodes) {
        for (node of line) {
            if (node.style.backgroundColor = MOUSE_OVER_COLOR) {
                setDefaultBackgroundColor(node);
            }
        } 
    } 
}
function index2d(array, yx) {
    y = yx[0];
    x = yx[1];
    return array[y][x];
}
function reformat2d(array) {
    let result = [];
    let temp = [];
    for (let i = 1; i < array.length + 1; i++) {
        if (i % 8 == 0){
            temp.push(array[i-1]);
            result.push(temp);
            temp = [];
        } else {
            temp.push(array[i-1]);
        }
    }
    return result;
}
function buildCheckers(nodes) {
    function appendChecker(type) {
        let element = document.createElement("div");
        element.classList.add("checker");
        element.classList.add("checker" + type);
        //element.addEventListener("mouseover", changeWhenOver);
        //element.addEventListener("mouseout", changeWhenOut);
        element.addEventListener("click", clickChecker);
        return element;
    }
    c = 0;
    type = 0;
    num = 12;
    for (let i = 1; i < nodes.length + 1; i++) {
        if (c % 2 == 0) {
            let target = nodes[i-1];
            target.appendChild(appendChecker(type));
            num--;
        }
        c++;
        if (num == 0) {
            num = 12;
            type = 1;
            i = nodes.length - 22;
        }
        if (i % 8 == 0 && i != 0) {
            c++;
        }
    }
    nodes[41].appendChild(appendChecker(1));
    checkers = [];
    for (node of nodes) {
        if (node.firstChild == null) {
            checkers.push(0);
        } else {
            checkers.push(node.firstChild);
        }
    }
    return reformat2d(checkers);
}






