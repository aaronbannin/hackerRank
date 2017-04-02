//: Playground - noun: a place where people can play

import Cocoa

var str = "Hello, playground"
var int = 5


//func convertToBinary(input: Int) -> (Int, String) {
//    let result:Int = input / 2
//    let remainder = String(input % 2)
//    return(result, remainder)
//}

func convertToBinary(input: Int, binaryString: String = "") -> (Int, String) {
    let result:Int = input / 2
    let remainder = String(input % 2)
    var newBinaryString = binaryString
    newBinaryString.appendContentsOf(remainder)
    return(result, newBinaryString)
}

var out = [Int]()
let a = arc4random_uniform(2)
for i in 0...10 {
    out.append(Int(arc4random_uniform(2)))
}
print(out)