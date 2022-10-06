class Test {
    constructor(age) {
        this.age = 9;
    }
}
t = new Test(5);
function pointDistance(p1, p2) {
    return Math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2);
}
console.log(pointDistance([1,1], [4,5]))
console.error("sex");
