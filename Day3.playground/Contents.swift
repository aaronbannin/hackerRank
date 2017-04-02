//: Playground - noun: a place where people can play

import Cocoa

let input = Int(readLine()!)!

switch input {
case _ where input % 2 != 0: print("Weird")
case _ where input >= 2 && input <= 5: print("Not Weird")
case _ where input >= 6 && input <= 20: print("Weird")
default: print("Not Weird")
}