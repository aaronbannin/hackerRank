//
//  main.swift
//  2d Array - DS
//
//  Created by Aaron Bannin on 4/25/16.
//  Copyright © 2016 Aaron Bannin. All rights reserved.
//

import Foundation

print("Hello, World!")

var inputValues = [[Int]]()

var rawInput = [["1 1 1 0 0 0"]]
rawInput.append(["0 1 0 0 0 0"])
rawInput.append(["1 1 1 0 0 0"])
rawInput.append(["0 0 0 0 0 0"])
rawInput.append(["0 0 0 0 0 0"])
rawInput.append(["0 0 0 0 0 0"])


func formatToArray(input: String) -> [Int] {
    let array = input.characters.split(" ").map(String.init)
    return array.map { Int($0)! }
}

for i in 0...5 {
    
}


var T = Int(readLine(stripNewline: true)!)!
